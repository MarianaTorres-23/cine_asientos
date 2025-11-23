# cine_asientos
El dueño de un cine quiere un sistema que muestre qué asientos están ocupados y cuáles están libres en una sala. Tu tarea será crear una matriz que represente los asientos de una sala de cine y permitir que el usuario consulte y reserve lugares.

📌 Instrucciones
Crea en Python un archivo llamado:

cine_asientos.py

Tu programa debe realizar lo siguiente:

🟦 A) Crear la matriz de asientos
Preguntar al usuario:

Número de filas del cine

Número de columnas (asientos por fila)

Crear una matriz donde:

Un asiento libre se representa con "L"

Un asiento ocupado se representa con "X"

Ejemplo inicial si hay 3x4:

L L L L
L L L L
L L L L

🟦 B) Funciones del sistema
Tu programa debe tener un menú con opciones:

1. Mostrar sala
2. Reservar asiento
3. Liberar asiento
4. Contar asientos ocupados y libres
5. Salir

📍 Opción 1: Mostrar sala
Imprime la matriz completa con formato bonito.

📍 Opción 2: Reservar asiento
Pedir fila y columna

Si está libre, convertir "L" → "X"

Si ya está ocupado, mostrar mensaje

📍 Opción 3: Liberar asiento
Igual que en reservar, pero convierte "X" → "L"

📍 Opción 4: Mostrar estadísticas
Mostrar:

Asientos libres

Asientos ocupados

🟦 C) Validaciones mínimas
Incluye:

Verificar que el asiento exista

Mostrar mensajes adecuados

No permitir reservar asientos ya ocupados
