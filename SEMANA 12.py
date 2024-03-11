# Definir ciudades, días de la semana y semanas
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Crear matriz 3D para almacenar temperaturas
# (ciudades x días de la semana x semanas)
temperaturas = [[[0.0 for _ in range(len(dias_semana))] for _ in range(semanas)] for _ in range(len(ciudades))]

# Llenar la matriz con datos de temperaturas (simulados)
# Aquí puedes ingresar tus datos reales
# Por ahora, usaré valores aleatorios para demostración
import random
for ciudad_idx in range(len(ciudades)):
    for semana_idx in range(semanas):
        for dia_idx in range(len(dias_semana)):
            # Generar temperatura aleatoria entre 10°C y 30°C
            temperatura = random.uniform(10, 30)
            temperaturas[ciudad_idx][semana_idx][dia_idx] = temperatura

# Calcular el promedio de temperaturas por ciudad y semana
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas para {ciudad}:")
    for semana_idx in range(semanas):
        promedio_semana = sum(temperaturas[ciudad_idx][semana_idx]) / len(dias_semana)
        print(f"Semana {semana_idx + 1}: {promedio_semana:.2f}°C")
    print()