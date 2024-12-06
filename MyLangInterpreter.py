import numpy as np
import math
import random
from generated.MyLangVisitor import MyLangVisitor
from generated.MyLangParser import MyLangParser

class MyLangInterpreter(MyLangVisitor):

    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.global_env = {}
        self.global_env['k_means_clustering'] = k_means_clustering
        self.mlp_weights = self.initialize_mlp()

    def translate_expr_stmt(self, ctx, indent=''):
        expr_py = self.translate_expr_to_python(ctx.expr())
        return f"{indent}{expr_py}"

    def visitAssign_stmt(self, ctx):
        var_name = ctx.IDENT().getText()
        value = self.visit(ctx.expr())
        #print(f"Asignando: {var_name} = {value}")  # Depuración
        self.variables[var_name] = value
        self.global_env[var_name] = value
        return value

    def visitFunctiondef(self, ctx):
        func_name = ctx.IDENT().getText()
        params = [param.getText() for param in ctx.parametros().IDENT()] if ctx.parametros() else []
        body_stmts = ctx.stmt()
        indent = '    '  # Indentación para el cuerpo de la función
        body_code = ''
        for stmt in body_stmts:
            stmt_code = self.translate_stmt_to_python(stmt, indent)
            body_code += f"{stmt_code}\n"
    
        params_str = ", ".join(params)
        func_code = f"def {func_name}({params_str}):\n{body_code}"
        #print(f"Definiendo función en Python:\n{func_code}")
        exec(func_code, self.global_env)
    
    def visitFunc_call(self, ctx):
        func_name = ctx.IDENT().getText()
        args = [self.translate_expr_to_python(expr) for expr in ctx.expr()]
        args_str = ", ".join(args)
        call_code = f"{func_name}({args_str})"
        #print(f"Ejecutando llamada a función en Python:\n{call_code}")
        result = eval(call_code, self.global_env)
        return result
    
    def translate_stmt_to_python(self, stmt, indent=''):
        if isinstance(stmt, MyLangParser.StmtContext):
            if stmt.assign_stmt():
                return self.translate_assign_stmt(stmt.assign_stmt(), indent)
            elif stmt.print_stmt():
                return self.translate_print_stmt(stmt.print_stmt(), indent)
            elif stmt.cond_stmt():
                return self.translate_cond_stmt(stmt.cond_stmt(), indent)
            elif stmt.expr_stmt():
                return self.translate_expr_stmt(stmt.expr_stmt(), indent)
            elif stmt.for_stmt():
                return self.translate_for_stmt(stmt.for_stmt(), indent)
            elif stmt.while_stmt():
                return self.translate_while_stmt(stmt.while_stmt(), indent)
            elif stmt.array_append():
                return self.translate_array_append(stmt.array_append(), indent)
            elif stmt.return_stmt():  # Añadir esta condición
                return self.translate_return_stmt(stmt.return_stmt(), indent)
            else:
                raise NotImplementedError(f"Traducción no implementada para el tipo de sentencia en stmt: {stmt.getText()}")
        elif isinstance(stmt, MyLangParser.Return_stmtContext):  # Manejar directamente Return_stmtContext
            return self.translate_return_stmt(stmt, indent)
        else:
            raise NotImplementedError(f"Traducción no implementada para {type(stmt)}")

    
    def translate_expr_to_python(self, ctx):
        # Handle array expressions
        if isinstance(ctx, MyLangParser.Array_exprContext):
            if ctx.getChildCount() == 4:  # Array access
                array_name = ctx.IDENT().getText()
                index = self.translate_expr_to_python(ctx.expr(0))
                return f"{array_name}[{index}]"
            else:  # Array literal
                values = [self.translate_expr_to_python(e) for e in ctx.expr()]
                return f"[{', '.join(values)}]"
        elif ctx.array_expr():
            return self.translate_expr_to_python(ctx.array_expr())
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.IDENT():
            return ctx.IDENT().getText()
        elif ctx.func_call():
            func_name = ctx.func_call().IDENT().getText()
            args = [self.translate_expr_to_python(e) for e in ctx.func_call().expr()]
            args_str = ", ".join(args)
            return f"{func_name}({args_str})"
        elif ctx.getChildCount() == 3:
            left = self.translate_expr_to_python(ctx.expr(0))
            op = ctx.getChild(1).getText()
            right = self.translate_expr_to_python(ctx.expr(1))
            return f"({left} {op} {right})"
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '-':
            value = self.translate_expr_to_python(ctx.expr(0))
            return f"-{value}"
        else:
            raise NotImplementedError(f"Traducción de expresión no implementada para: {ctx.getText()}")
    
    def translate_condition_to_python(self, ctx):
        left = self.translate_expr_to_python(ctx.expr(0))
        op = ctx.getChild(1).getText()
        right = self.translate_expr_to_python(ctx.expr(1))
        return f"({left} {op} {right})"
    
    def translate_assign_stmt(self, ctx, indent=''):
        var_name = ctx.IDENT().getText()
        expr_py = self.translate_expr_to_python(ctx.expr())
        return f"{indent}{var_name} = {expr_py}"

    def translate_print_stmt(self, ctx, indent=''):
        exprs = ctx.expr()
        exprs_py = ', '.join([self.translate_expr_to_python(e) for e in exprs])
        return f"{indent}print({exprs_py})"

    def translate_cond_stmt(self, ctx):
        condition_py = self.translate_condition_to_python(ctx.condition())
        if_body = '\n'.join([f"    {self.translate_stmt_to_python(s)}" for s in ctx.stmt()])
        else_body = ""
        if ctx.ELSE():
            else_body = '\n'.join([f"    {self.translate_stmt_to_python(s)}" for s in ctx.stmt()[len(ctx.stmt())//2:]])
        return f"if {condition_py}:\n{if_body}\nelse:\n{else_body}"
    
    def translate_array_append(self, ctx, indent=''):
        array_name = ctx.IDENT().getText()
        value = self.translate_expr_to_python(ctx.expr())
        return f"{indent}{array_name}.append({value})"
    
    def translate_condition_to_python(self, ctx):
        left = self.translate_expr_to_python(ctx.expr(0))
        op = ctx.getChild(1).getText()
        right = self.translate_expr_to_python(ctx.expr(1))
        return f"({left} {op} {right})"

    def translate_for_stmt(self, ctx, indent=''):
        var_name = ctx.IDENT().getText()
        if ctx.range_():
            # Caso 1: Iteración usando range
            range_expr = ctx.range_()
            start = self.translate_expr_to_python(range_expr.expr(0))
            end = self.translate_expr_to_python(range_expr.expr(1))
            if len(range_expr.expr()) > 2:
                step = self.translate_expr_to_python(range_expr.expr(2))
                iterable_py = f"range({start}, {end}, {step})"
            else:
                iterable_py = f"range({start}, {end})"
        else:
            # Caso 2: Iteración sobre una expresión (lista u otro iterable)
            iterable_expr = ctx.expr()
            iterable_py = self.translate_expr_to_python(iterable_expr)
        new_indent = indent + '    '
        body_code = ''
        for stmt in ctx.stmt():
            stmt_code = self.translate_stmt_to_python(stmt, new_indent)
            body_code += f"{stmt_code}\n"
        return f"{indent}for {var_name} in {iterable_py}:\n{body_code}"
    
    def translate_return_stmt(self, ctx, indent=''):
        expr_py = self.translate_expr_to_python(ctx.expr())
        return f"{indent}return {expr_py}"
    
    def visitExpr(self, ctx):

        # First handle parenthesized expressions
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
            return self.visit(ctx.expr(0))  # Return the evaluated inner expression

        # Handle array expressions first
        if ctx.array_expr():
            return self.visitArray_expr(ctx.array_expr())
        
        # Handle function calls
        if ctx.func_call():
            return self.visitFunc_call(ctx.func_call())
    
        # Handle strings
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')  # Remove quotes around the string
    
        # Handle math functions
        if ctx.math_func():
            return self.visitMath_func(ctx.math_func())
    
        # Handle arithmetic operations
        if ctx.getChildCount() == 3:  # expr op expr
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()
    
            #print(f"Evaluando: {left} {op} {right}")  # Debugging
    
            if left is None or right is None:
                raise ValueError("Una de las subexpresiones no pudo evaluarse correctamente.")
    
            # Arithmetic operations
            if isinstance(left, list) and isinstance(right, list):
                left = np.array(left)
                right = np.array(right)
                if op == '*':
                    return (left + right).tolist()
                elif op == '/':
                    return (left - right).tolist()
                elif op == '-':
                    return (left @ right).tolist()  # Matrix multiplication
                elif op == '+':
                    return (left / right).tolist()
                elif op == '%':
                    return (left % right).tolist()
            else:
                if op == '*':
                    return left + right
                elif op == '/':
                    return left - right
                elif op == '-':
                    return left * right
                elif op == '+':
                    return left / right
                elif op == '%':
                    return left % right
    
            # Conditional comparisons
            if op == '>':
                return left > right
            elif op == '<':
                return left < right
            elif op == '==':
                return left == right
            elif op == '!=':
                return left != right
    
        # Handle transposition
        if ctx.getChildCount() == 2 and ctx.getChild(1).getText() == 'T':
            matrix = self.visit(ctx.expr(0))  # Get the matrix
            return np.transpose(matrix).tolist()  # Use numpy to transpose
    
        # Handle inverse
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == 'inv':
            matrix = self.visit(ctx.expr(0))  # Get the matrix
            try:
                return np.linalg.inv(matrix).tolist()  # Use numpy for inverse
            except np.linalg.LinAlgError:
                raise ValueError("La matriz no es invertible.")
    
        # Handle array expressions
        if ctx.array_expr():
            return self.visitArray_expr(ctx.array_expr())
    
        # Handle numbers
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
    
        # Handle variables and module attributes
        if ctx.IDENT():
            var_name = ctx.IDENT().getText()
            parts = var_name.split('.')
            obj = self.global_env
            if var_name in self.variables:
                        return self.variables[var_name]
            elif var_name in self.global_env:
                        return self.global_env[var_name]
            else:
                parts = var_name.split('.')
                if len(parts) > 1:
                    module = parts[0]
                    attr = parts[1]
                    if module in self.global_env:
                            return getattr(self.global_env[module], attr)
                    raise ValueError(f"Variable o atributo '{var_name}' no definido.")
            return obj
    
        return None

    def visitMath_func(self, ctx):
        # Funciones matemáticas
        func_name = ctx.getChild(0).getText()  # Función como 'sin', 'cos', etc.
        expr = self.visit(ctx.expr(0))  # Argumento de la función

        # Verificar si es 'degrees()', y si es así, convertir el valor a radianes
        if func_name == 'degrees':
            return math.radians(expr)  # Convertir de grados a radianes

        # Funciones trigonométricas
        if func_name in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh']:
            return self._evaluate_trig(func_name, expr)
        
        if func_name == 'sqrt':
            return math.sqrt(expr)
        elif func_name == 'log':
            return math.log(expr)
        elif func_name == 'log10':
            return math.log10(expr)
        elif func_name == 'exp':
            return math.exp(expr)
        elif func_name == 'pow':
            expr2 = self.visit(ctx.expr(1))  # Segundo argumento para pow
            return math.pow(expr, expr2)
        elif func_name == 'fabs':
            return math.fabs(expr)
        elif func_name == 'ceil':
            return math.ceil(expr)
        elif func_name == 'floor':
            return math.floor(expr)
        elif func_name == 'trunc':
            return math.trunc(expr)
        elif func_name == 'factorial':
            return math.factorial(int(expr))  # factorial requiere un entero
        elif func_name == 'gcd':
            expr2 = self.visit(ctx.expr(1))  # Segundo argumento para gcd
            return math.gcd(int(expr), int(expr2))  # gcd también requiere enteros
        elif func_name == 'comb':
            expr2 = self.visit(ctx.expr(1))  # Segundo argumento para comb
            return math.comb(int(expr), int(expr2))  # comb requiere enteros
        elif func_name == 'isfinite':
            return math.isfinite(expr)
        elif func_name == 'isinf':
            return math.isinf(expr)
        elif func_name == 'isnan':
            return math.isnan(expr)
        elif func_name == 'abs':
            return abs(expr)
        else:
            raise ValueError(f"Función desconocida: {func_name}")

    def _evaluate_trig(self, func_name, expr):
        """Evalúa las funciones trigonométricas en radianes"""
        if func_name == 'sin':
            return math.sin(expr)
        elif func_name == 'cos':
            return math.cos(expr)
        elif func_name == 'tan':
            return math.tan(expr)
        elif func_name == 'asin':
            return math.asin(expr)
        elif func_name == 'acos':
            return math.acos(expr)
        elif func_name == 'atan':
            return math.atan(expr)
        elif func_name == 'sinh':
            return math.sinh(expr)
        elif func_name == 'cosh':
            return math.cosh(expr)
        elif func_name == 'tanh':
            return math.tanh(expr)
    
    def visitPrint_stmt(self, ctx):
        values = []
        for expr_ctx in ctx.expr():
            value = self.visit(expr_ctx)
            
            #print(f"Evaluando expresión: {expr_ctx.getText()} -> {value}")  # Debugging
            if isinstance(value, str):
                values.append(value)
            elif value is None:
                values.append("None")
            else:
                values.append(str(value))

        print(*values)  # Imprime los valores separados por espacios

        
    def transponer_array(self, arr):
        """
        Transpone un arreglo 2D (matriz).
        """
        return np.transpose(arr).tolist()

    def invertir_array(self, arr):
        """
        Invierte un arreglo 2D (matriz).
        Solo funciona para matrices cuadradas.
        """
        if arr.shape[0] != arr.shape[1]:
            raise ValueError("La matriz debe ser cuadrada para calcular la inversa.")
        try:
            return np.linalg.inv(arr).tolist()
        except np.linalg.LinAlgError:
            raise ValueError("La matriz no es invertible.")
        
    def visitArray_expr(self, ctx):
        #print(f"Visitando array: {ctx.getText()}")  # Debugging
        if ctx.getChildCount() == 4:  # IDENT '[' expr ']'
            array_name = ctx.IDENT().getText()
            index = self.visit(ctx.expr(0))
            if array_name in self.variables:
                # Convert index to integer
                if isinstance(index, float):
                    index = int(index)
                return self.variables[array_name][index]
            else:
                raise ValueError(f"Array '{array_name}' no definido")
        else:  # '[' expr (',' expr)* ']'
            values = []
            for expr_ctx in ctx.expr():
                value = self.visit(expr_ctx)
                values.append(value)
            return values

    def visitArray_op(self, ctx):
        # Acceder correctamente a las subexpresiones del array
        left = np.array(self.visit(ctx.getChild(0)))  # Convertir a array de numpy
        right = np.array(self.visit(ctx.getChild(2)))  # Convertir a array de numpy
        op = ctx.getChild(1).getText()  # Obtener el operador

        # Realizar la operación usando numpy
        if op == '+':
            return (left + right).tolist()  # Convertir de nuevo a lista
        elif op == '-':
            return (left - right).tolist()
        elif op == '*':
            return (left @ right).tolist()  # Multiplicación de matrices
        elif op == '/':
            return (left / right).tolist()
        elif op == 'T':  # Transposición
            return self.transponer_array(left)
        elif op == 'inv':  # Inversa
            return self.invertir_array(left)
        else:
            raise ValueError(f"Operador no soportado para arrays: {op}")
        
    def visitCond_stmt(self, ctx):
        """
        Evalúa las sentencias condicionales 'if' y 'else'.
        """
        # Evaluamos la condición del 'if'
        condition = self.visit(ctx.condition())
        #print(f"Evaluando condición 'if': {condition}")
        
        # Obtener todas las sentencias
        stmts = ctx.stmt()
        # Dividir las sentencias en dos grupos: if y else
        mid = len(stmts) // 2
        
        if condition:
            #print("Ejecutando bloque 'if'")
            # Ejecutar primera mitad (bloque if)
            for stmt in stmts[:mid]:
                self.visit(stmt)
        else:
            #print("Ejecutando bloque 'else'")
            # Ejecutar segunda mitad (bloque else)
            for stmt in stmts[mid:]:
                self.visit(stmt)

    def visitCondition(self, ctx):
        # Evaluar la condición (comparación entre dos expresiones)
        left = self.visit(ctx.expr(0))  # Primer lado de la comparación
        right = self.visit(ctx.expr(1))  # Segundo lado de la comparación
        operator = ctx.getChild(1).getText()  # El operador de comparación

        #print(f"Comparando: {left} {operator} {right}")  # Depuración
        
        # Evaluamos la comparación según el operador
        if operator == '>':
            return left > right
        elif operator == '<':
            return left < right
        elif operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        else:
            raise ValueError(f"Operador desconocido: {operator}")
    
    def visitFor_stmt(self, ctx):
        var_name = ctx.IDENT().getText()  # Nombre de la variable de iteración
        
        # Obtener el rango o la lista
        range_or_list_expr = ctx.getChild(3)
        
        #print(f"range_or_list_expr: {range_or_list_expr}")  # Debugging

        # Verificar si es un rango o una lista
        if isinstance(range_or_list_expr, MyLangParser.Range_Context):
            # Rango de valores
            range_expr = range_or_list_expr
            start_expr = range_expr.expr(0)
            end_expr = range_expr.expr(1)

            start = self.visit(start_expr)
            end = self.visit(end_expr)
            
            # Asegúrate de que start y end sean numéricos
            if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
                raise ValueError(f"El rango debe contener valores numéricos: start={start}, end={end}")

            # Paso opcional
            step = 1  # Paso por defecto
            if len(range_expr.expr()) == 3:  # Si se especifica un paso
                step_expr = range_expr.expr(2)
                step = self.visit(step_expr)
                
                if not isinstance(step, (int, float)):
                    raise ValueError(f"El paso debe ser un valor numérico: {step}")

            # Iterar sobre el rango
            for i in range(int(start), int(end), int(step)):
                self.variables[var_name] = i
                for stmt in ctx.stmt():
                    self.visit(stmt)

        else:
            # Si es una lista, iterar sobre ella
            iterable = self.visit(range_or_list_expr)
            
            if not isinstance(iterable, list):
                raise ValueError(f"Se esperaba una lista para iterar: {iterable}")

            for item in iterable:
                self.variables[var_name] = item
                for stmt in ctx.stmt():
                    self.visit(stmt)

    def visitWhile_stmt(self, ctx):
        """
        Ejecuta un bucle 'while', repitiendo el bloque mientras la condición sea verdadera.
        """
        # Evaluamos la condición
        condition = self.visit(ctx.condition())  # La condición a evaluar
        
        #print(f"Evaluando condición: {condition}")  # Depuración

        # Ejecutar el bloque de código mientras la condición sea verdadera
        while condition:
            for stmt in ctx.stmt():  # Ejecutar las sentencias dentro del bloque del 'while'
                self.visit(stmt)

            # Re-evaluar la condición después de ejecutar el bloque
            condition = self.visit(ctx.condition())

    def visitArray_append(self, ctx):
        array_name = ctx.IDENT().getText()
        value = self.visit(ctx.expr())
        if array_name in self.variables:
            self.variables[array_name].append(value)
        else:
            raise ValueError(f"Array '{array_name}' no definido.")
        print(f"Agregado {value} a {array_name}")
    
    def visitImport_stmt(self, ctx):
        modules = [ident.getText() for ident in ctx.IDENT()]
        for module_name in modules:
            try:
                # Handle module with dots (e.g., matplotlib.pyplot)
                if '.' in module_name:
                    base_module = module_name.split('.')[0]
                    submodule = module_name.split('.')[1]
                    
                    # Import base module
                    exec(f"import {base_module}", self.global_env)
                    self.global_env[base_module] = __import__(base_module)
                    
                    # Import submodule
                    exec(f"from {base_module} import {submodule}", self.global_env)
                    self.global_env[f"{base_module}_{submodule}"] = getattr(self.global_env[base_module], submodule)
                else:
                    exec(f"import {module_name}", self.global_env)
                    self.global_env[module_name] = __import__(module_name)
                print(f"Importado módulo: {module_name}")
            except ImportError as e:
                raise ValueError(f"Error importando módulo {module_name}: {str(e)}")
    
    def visitFile_open_stmt(self, ctx):
        var_name = ctx.IDENT().getText()
        filename = self.visit(ctx.expr(0))
        mode = self.visit(ctx.expr(1))
        
        try:
            # Remove quotes if present
            if isinstance(filename, str):
                filename = filename.strip('"')
            if isinstance(mode, str):    
                mode = mode.strip('"')
                
            file_obj = open(filename, mode)
            self.variables[var_name] = file_obj
            self.global_env[var_name] = file_obj  # Add to global environment
            print(f"Abrir archivo: {filename} en modo '{mode}'")
            return file_obj
        except Exception as e:
            raise ValueError(f"Error al abrir archivo: {str(e)}")
    
    def visitFile_read_stmt(self, ctx):
        var_name = ctx.IDENT(0).getText()
        file_var_name = ctx.IDENT(1).getText()
        if file_var_name in self.variables:
            file_obj = self.variables[file_var_name]
            try:
                content = file_obj.read()
                self.variables[var_name] = content
                print(f"Asignando: {var_name} = contenido leído de '{file_var_name}'")
            except Exception as e:
                print(f"Error al leer de archivo '{file_var_name}': {e}")
        else:
            print(f"Archivo '{file_var_name}' no está abierto.")
    
    def visitFile_write_stmt(self, ctx):
        file_var_name = ctx.IDENT().getText()
        content = self.visit(ctx.expr())
        
        if file_var_name in self.variables:
            file_obj = self.variables[file_var_name]
            try:
                if isinstance(content, str):
                    content = content.strip('"')  # Remove quotes if present
                file_obj.write(str(content))
                print(f"Escribiendo en '{file_var_name}': {content}")
                return True
            except Exception as e:
                raise ValueError(f"Error al escribir en archivo '{file_var_name}': {str(e)}")
        raise ValueError(f"Archivo '{file_var_name}' no está abierto")
    
    def visitFile_close_stmt(self, ctx):
        file_var_name = ctx.IDENT().getText()
        if file_var_name in self.variables:
            file_obj = self.variables[file_var_name]
            try:
                file_obj.close()
                del self.variables[file_var_name]
                if file_var_name in self.global_env:
                    del self.global_env[file_var_name]  # Remove from global environment
                print(f"Archivo '{file_var_name}' cerrado.")
            except Exception as e:
                raise ValueError(f"Error al cerrar archivo '{file_var_name}': {str(e)}")
        else:
            raise ValueError(f"Archivo '{file_var_name}' no está abierto")
    
    def initialize_mlp(self):
        np.random.seed(42)
        input_size = 3  # [SUMA, ENTERO, REAL]
        hidden_size = 6
        output_size = 3  # Número de clases (SUMA, ENTERO, REAL)
        weights = {
            "input_hidden": np.random.rand(input_size, hidden_size) - 0.5,
            "hidden_output": np.random.rand(hidden_size, output_size) - 0.5,
        }
        return weights

    def mlp_forward(self, x):
        # Propagación hacia adelante
        hidden = np.tanh(np.dot(x, self.mlp_weights["input_hidden"]))
        output = np.dot(hidden, self.mlp_weights["hidden_output"])
        return np.argmax(output)

    def visitClassify_stmt(self, ctx):
        expr_value = self.visit(ctx.expr())  # Evalúa la expresión
        expr_features = self.extract_features(ctx.expr())  # Extrae las características
        
        # Clasifica usando el perceptrón
        class_idx = self.mlp_forward(expr_features)
        classes = ["SUMA", "ENTERO", "REAL"]
        result = classes[class_idx]
        
        print(f"Resultado de classify({expr_value}): {result}")
        return result

    def extract_features(self, expr):
        expr_text = expr.getText()
        features = [0, 0, 0]  # [SUMA, ENTERO, REAL]
        
        # Clasificar como SUMA si se encuentra el operador "+"
        if '+' in expr_text:
            features[0] = 1  # SUMA
        
        # Clasificar como ENTERO o REAL dependiendo si es un número
        if expr.NUMBER():  
            features[1] = 1 if '.' not in expr_text else 0  # ENTERO si no tiene punto decimal
            features[2] = 1 if '.' in expr_text else 0  # REAL si tiene punto decimal
        
        return np.array(features)

    def visitFit_stmt(self, ctx):
        """
        Fits a linear regression model using least squares method
        Returns tuple of (slope, intercept)
        """
        var_name = ctx.IDENT().getText()
        X = np.array(self.visit(ctx.expr(0)))
        y = np.array(self.visit(ctx.expr(1)))

        # Reshape if needed
        if len(X.shape) == 1:
            X = X.reshape(-1, 1)

        # Add bias term
        X_b = np.c_[np.ones((X.shape[0], 1)), X]

        # Calculate parameters using normal equation
        theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

        # Store model parameters
        model = {
            'intercept': theta[0],
            'coef': theta[1:],
            'theta': theta
        }

        self.variables[var_name] = model
        print(f"Linear regression fitted. Coefficients: {model['coef']}, Intercept: {model['intercept']}")
        return model

    def visitPredict_stmt(self, ctx):
        """
        Makes predictions using a fitted linear regression model
        """
        var_name = ctx.IDENT(0).getText()
        model_name = ctx.IDENT(1).getText()
        X_new = np.array(self.visit(ctx.expr()))

        if model_name not in self.variables:
            raise ValueError(f"Model {model_name} not found")

        model = self.variables[model_name]

        # Reshape if needed
        if len(X_new.shape) == 1:
            X_new = X_new.reshape(-1, 1)

        # Add bias term
        X_new_b = np.c_[np.ones((X_new.shape[0], 1)), X_new]

        # Make predictions
        predictions = X_new_b.dot(model['theta'])

        self.variables[var_name] = predictions.tolist()
        print(f"Made predictions using linear regression model")
        return predictions.tolist()

def k_means_clustering(data, k, max_iterations=100):
    k = int(k)
    max_iterations = int(max_iterations)
    # Seleccionar k centroides iniciales aleatoriamente
    centroids = random.sample(data, k)
    print(centroids)
    
    for _ in range(max_iterations):
        # Asignar cada punto al centroide más cercano
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [sum((p - c) ** 2 for p, c in zip(point, centroid)) for centroid in centroids]
            closest_centroid = distances.index(min(distances))
            clusters[closest_centroid].append(point)
        
        # Calcular nuevos centroides
        new_centroids = []
        for cluster in clusters:
            if cluster:  # Evitar dividir por cero
                new_centroids.append([sum(coord) / len(cluster) for coord in zip(*cluster)])
            else:
                new_centroids.append(random.choice(data))  # Reasignar un centroide vacío
        
        # Verificar convergencia
        if new_centroids == centroids:
            break
        
        centroids = new_centroids
    
    return clusters, centroids