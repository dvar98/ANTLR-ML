import numpy as np
import matplotlib.pyplot as plt
import math
from generated.MyLangVisitor import MyLangVisitor
from generated.MyLangParser import MyLangParser
import os
import pandas as pd
import csv

class MyLangInterpreter(MyLangVisitor):

    def __init__(self):
        self.variables = {}

    def visitAssign_stmt(self, ctx):
        var_name = ctx.IDENT().getText()
        value = self.visit(ctx.expr())
        #print(f"Asignando: {var_name} = {value}")  # Depuración
        self.variables[var_name] = value
        return value

    def visitExpr(self, ctx):
        # Caso de cadenas de texto
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')  # Eliminar las comillas alrededor de la cadena
        
        # Caso de funciones matemáticas
        if ctx.math_func():
            return self.visitMath_func(ctx.math_func())

        # Caso de operaciones aritméticas
        if ctx.getChildCount() == 3:  # expr op expr
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            #print(f"Evaluando: {left} {op} {right}")  # Depuración

            if left is None or right is None:
                raise ValueError("Una de las subexpresiones no pudo evaluarse correctamente.")

            # Operaciones aritméticas
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '%':
                return left % right
            # Comparaciones condicionales
            elif op == '>':
                return left > right
            elif op == '<':
                return left < right
            elif op == '==':
                return left == right
            elif op == '!=':
                return left != right
        elif ctx.getChildCount() == 2 and ctx.getChild(1).getText() == 'T':  # Caso de transposición
            matrix = self.visit(ctx.expr(0))  # Obtener la matriz
            return np.transpose(matrix).tolist()  # Usar numpy para transponer
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == 'inv':  # Caso de inversa
            matrix = self.visit(ctx.expr(0))  # Obtener la matriz
            try:
                return np.linalg.inv(matrix).tolist()  # Usar numpy para la inversa
            except np.linalg.LinAlgError:
                raise ValueError("La matriz no es invertible.")
        elif ctx.array_expr():  # Array expression
            return self.visit(ctx.array_expr())
        elif ctx.NUMBER():  # Número
            return float(ctx.NUMBER().getText())
        elif ctx.IDENT():  # Variable
            var_name = ctx.IDENT().getText()
            if var_name not in self.variables:
                raise ValueError(f"Variable '{var_name}' no definida.")
            return self.variables.get(var_name)
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

    def visitPlot_stmt(self, ctx):
        x_var_name = ctx.IDENT(0).getText()
        y_var_name = ctx.IDENT(1).getText()

        # Obtener valores
        x = self.variables.get(x_var_name)
        y = self.variables.get(y_var_name)

        # Manejo de errores
        if x is None or y is None:
            raise ValueError(f"Variables no definidas: {x_var_name}, {y_var_name}")
        if len(x) != len(y):
            raise ValueError(f"Las listas deben tener el mismo tamaño: {len(x)} != {len(y)}")

        # Obtener configuraciones opcionales
        title = ctx.STRING(0).getText().strip('"') if ctx.STRING(0) else ""
        xlabel = ctx.STRING(1).getText().strip('"') if ctx.STRING(1) else x_var_name
        ylabel = ctx.STRING(2).getText().strip('"') if ctx.STRING(2) else y_var_name
        style = ctx.STRING(3).getText().strip('"') if ctx.STRING(3) else "b-"

        # Crear gráfica
        plt.plot(x, y, style)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()

    def visitFile_stmt(self, ctx):
            action = ctx.getChild(0).getText()
            filename = ctx.STRING(0).getText().strip('"')
            if action == 'write':
                content = ctx.STRING(1).getText().strip('"')
                content = content.replace('\\n', '\n')  # Reemplazar \n por nuevas líneas
                with open(filename, 'w') as f:
                    f.write(content)
            elif action == 'read':
                if filename.endswith('.csv'):
                    with open(filename, 'r') as f:
                        reader = csv.reader(f)
                        content = [row for row in reader]
                        print(content)  # Imprimir el contenido leído
                elif filename.endswith('.xlsx') or filename.endswith('.xls'):
                    df = pd.read_excel(filename)
                    content = df.to_dict(orient='list')
                    print(content)  # Imprimir el contenido leído
                else:
                    with open(filename, 'r') as f:
                        content = f.read()
                        print(content)  # Imprimir el contenido leído
            else:
                raise ValueError(f"Acción de archivo desconocida: {action}")

    def visitRegression_stmt(self, ctx):
        x_var_name = ctx.IDENT(0).getText()
        y_var_name = ctx.IDENT(1).getText()
        slope_var_name = ctx.IDENT(2).getText()
        intercept_var_name = ctx.IDENT(3).getText()

        x = np.array(self.variables.get(x_var_name))
        y = np.array(self.variables.get(y_var_name))

        if x is None or y is None:
            raise ValueError(f"Variables no definidas: {x_var_name}, {y_var_name}")

        if len(x) != len(y):
            raise ValueError(f"Las listas deben tener el mismo tamaño: {len(x)} != {len(y)}")

        A = np.vstack([x, np.ones(len(x))]).T
        slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]

        self.variables[slope_var_name] = slope
        self.variables[intercept_var_name] = intercept

        print(f"Regresión lineal: y = {slope}x + {intercept}")
    
    def visitPrint_stmt(self, ctx):
        values = []
        for expr_ctx in ctx.expr():
            value = self.visit(expr_ctx)
            
            #print(f"Evaluando expresión: {expr_ctx.getText()} -> {value}")  # Debugging
            if isinstance(value, str):
                values.append(f'"{value}"')
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
        #print(f"Visitando array: {ctx.getText()}")  # Depuración
        if ctx.getChildCount() == 3:  # IDENT '[' expr ']'
            array_name = ctx.IDENT().getText()
            index = self.visit(ctx.expr(0))
            return self.variables[array_name][index]
        else:  # '[' expr (',' expr)* ']'
            return [self.visit(expr) for expr in ctx.expr()]

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
            return (left * right).tolist()
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
        # Evaluamos la condición
        condition = self.visit(ctx.condition())  # La condición que se evalúa
        
        #print(f"Evaluando condición: {condition}")  # Depuración
        
        if condition:  # Si la condición es verdadera
            #print("Ejecutando bloque 'if'")
            for stmt in ctx.stmt()[:ctx.stmt().index(ctx.getChild(ctx.getChildCount() - 1))]:  # Ejecutar las sentencias dentro del 'if'
                self.visit(stmt)
        elif ctx.getChildCount() > 4 and ctx.getChild(4).getText() == 'else:':  # Verifica si hay un bloque 'else'
            #print("Ejecutando bloque 'else'")
            for stmt in ctx.stmt()[ctx.stmt().index(ctx.getChild(ctx.getChildCount() - 1)):]:  # Ejecutar las sentencias dentro del 'else'
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
        """
        Ejecuta un bucle 'for', donde var_name es la variable de iteración y el rango es especificado
        por la expresión de inicio, fin y paso, o una lista.
        """
        var_name = ctx.IDENT().getText()  # Nombre de la variable de iteración
    
        # Obtener el rango o la lista
        range_or_list_expr = ctx.getChild(3)
    
        # Verificar si es un rango o una lista
        if isinstance(range_or_list_expr, MyLangParser.Range_Context):
            # Evaluar los valores del rango (start, end y step)
            range_expr = range_or_list_expr
            start_expr = range_expr.expr(0)
            end_expr = range_expr.expr(1)
            
            start = self.visit(start_expr)
            end = self.visit(end_expr)
            
            # Asegurarse de que start y end sean numéricos
            if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
                raise ValueError(f"El rango debe contener valores numéricos: start={start}, end={end}")
    
            # Paso opcional
            step = 1  # Paso por defecto
            if len(range_expr.expr()) == 3:  # Si se especifica un paso
                step_expr = range_expr.expr(2)
                step = self.visit(step_expr)
                
                # Asegurarse de que el valor de 'step' sea numérico
                if not isinstance(step, (int, float)):
                    raise ValueError(f"El paso debe ser un valor numérico: {step}")
    
            # Ajustar el rango para incluir el límite superior (para bucles ascendentes)
            if step > 0:
                end += 1
            else:
                end -= 1
    
            # Iterar sobre el rango ajustado
            for i in range(int(start), int(end), int(step)):
                self.variables[var_name] = i  # Asignar el valor de la variable de iteración
                for stmt in ctx.stmt():  # Ejecutar las sentencias dentro del bloque del 'for'
                    self.visit(stmt)
        else:
            # Evaluar la lista
            iterable = self.visit(range_or_list_expr)
            
            # Asegurarse de que sea una lista
            if not isinstance(iterable, list):
                raise ValueError(f"Se esperaba una lista para iterar: {iterable}")
    
            # Iterar sobre la lista
            for item in iterable:
                self.variables[var_name] = item  # Asignar el valor de la variable de iteración
                for stmt in ctx.stmt():  # Ejecutar las sentencias dentro del bloque del 'for'
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








