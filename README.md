# Manual de Operaciones de MyLang

## Operaciones Aritméticas
```my
# Suma
a = 5 + 3
cout("5 + 3 =", a)

# Resta
b = 10 - 4
cout("10 - 4 =", b)

# Multiplicación
c = 7 * 2
cout("7 * 2 =", c)

# División
d = 20 / 4
cout("20 / 4 =", d)

# Módulo
e = 10 % 3
cout("10 % 3 =", e)
```
## Funciones Matemáticas
```my
# Seno
seno = sin(45)
cout("sin(45) =", seno)

# Coseno
coseno = cos(45)
cout("cos(45) =", coseno)

# Tangente
tangente = tan(45)
cout("tan(45) =", tangente)

# Raíz cuadrada
raiz = sqrt(16)
cout("sqrt(16) =", raiz)

# Logaritmo natural
logaritmo = log(2.71828)
cout("log(2.71828) =", logaritmo)

# Exponencial
exponencial = exp(1)
cout("exp(1) =", exponencial)

# Potencia
potencia = pow(2, 3)
cout("pow(2, 3) =", potencia)

# Valor absoluto
absoluto = fabs(-5)
cout("fabs(-5) =", absoluto)

# Techo
techo = ceil(4.2)
cout("ceil(4.2) =", techo)

# Piso
piso = floor(4.8)
cout("floor(4.8) =", piso)

# Truncamiento
truncado = trunc(4.8)
cout("trunc(4.8) =", truncado)

# Factorial
factorial = factorial(5)
cout("factorial(5) =", factorial)

# Máximo común divisor
mcd = gcd(48, 18)
cout("gcd(48, 18) =", mcd)

# Combinaciones
combinaciones = comb(5, 2)
cout("comb(5, 2) =", combinaciones)

# Es finito
esfinito = isfinite(1.0)
cout("isfinite(1.0) =", esfinito)

# Es infinito
esinfinito = isinf(1.0 / 0.0)
cout("isinf(1.0 / 0.0) =", esinfinito)

# Es NaN
esnan = isnan(0.0 / 0.0)
cout("isnan(0.0 / 0.0) =", esnan)

# Grados
grados = degrees(1)
cout("degrees(1) =", grados)
```
## Operaciones con Arrays

```my
# Definición de array
array = [1, 2, 3, 4, 5]
cout("Array:", array)

# Acceso a elementos
elemento = array[2]
cout("Elemento en posición 2:", elemento)

# Suma de arrays
array1 = [1, 2, 3]
array2 = [4, 5, 6]
suma_arrays = array1 + array2
cout("Suma de arrays:", suma_arrays)

# Resta de arrays
resta_arrays = array1 - array2
cout("Resta de arrays:", resta_arrays)

# Multiplicación de arrays
multiplicacion_arrays = array1 * array2
cout("Multiplicación de arrays:", multiplicacion_arrays)

# División de arrays
division_arrays = array1 / array2
cout("División de arrays:", division_arrays)

# Transposición
matriz = [[1, 2], [3, 4]]
transpuesta = matriz T
cout("Transpuesta:", transpuesta)

# Inversa
inversa = inv matriz
cout("Inversa:", inversa)

# Append
array.append(6)
cout("Array después de append:", array)
```
## Sentencias de Control
```my
# Asignación
x = 10
cout("x =", x)

# Impresión
cout("Hola, mundo!")

# Condicionales
if x > 5:
    cout("x es mayor que 5")
else:
    cout("x no es mayor que 5")
end

# Bucles for
for i in range(0, 5, 1):
    cout("Valor de i:", i)
end

# Bucles while
i = 0
while i < 5:
    cout("Valor de i:", i)
    i = i + 1
end
```

## Funciones
```my
# Definición de funciones
funcion suma(a, b) {
    return a + b
}

# Llamada a funciones
resultado = suma(3, 4)
cout("Resultado de suma(3, 4):", resultado)
```

## Manejo de Archivos
```my
# Abrir archivo
archivo = open("mi_archivo.txt", "w")

# Escribir archivo
archivo.write("Hola, este es un archivo de prueba.\nSegunda línea.")

# Cerrar archivo
archivo.close()

# Leer archivo
archivo = open("mi_archivo.txt", "r")
contenido = archivo.read()
cout("Contenido del archivo:", contenido)
archivo.close()
```

## Importaciones
```my
# Importar módulos
import numpy, matplotlib.pyplot

# Uso de módulos importados
plt = matplotlib.pyplot
plt.figure(10)
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```
## Declaraciones de Variables
```my
# Identificadores
variable = 10
cout("Variable:", variable)

# Números
numero = 3.14
cout("Número:", numero)

# Cadenas
cadena = "Hola, mundo!"
cout("Cadena:", cadena)
```
## Operaciones de Regresión Lineal
```my
# Datos de entrenamiento
X = [1, 2, 3, 4, 5]
y = [2.1, 4.2, 6.1, 8.3, 10.2]

# Ajustar modelo
modelo = fit_linear(X, y)

# Hacer predicciones
X_nuevos = [6, 7, 8]
predicciones = predict_linear(modelo, X_nuevos)

# Imprimir resultados
cout("Predicciones:", predicciones)
```
