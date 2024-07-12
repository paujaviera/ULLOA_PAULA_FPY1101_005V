import random
import csv
import math

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

sueldos = []

def sueldos_random():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados de manera aleatoria")

def clasificar_sueldos():
    print("Sueldos menores a $800.000 TOTAL:", len([s for s in sueldos if s < 800000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            print(f"Nombre empleado: {trabajador['nombre']} Cargo: {trabajador['cargo']} Sueldo: ${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000 TOTAL:", len([s for s in sueldos if 800000 <= s <= 2000000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if 800000 <= sueldo <= 2000000:
            print(f"Nombre empleado: {trabajador['nombre']} Cargo: {trabajador['cargo']} Sueldo: ${sueldo}")
    
    print("\nSueldos mayores a $2.000.000 TOTAL:", len([s for s in sueldos if s > 2000000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo > 2000000:
            print(f"Nombre empleado: {trabajador['nombre']} Cargo: {trabajador['cargo']} Sueldo: ${sueldo}")
    
    print("\nTOTAL SUELDOS:", sum(sueldos))

def ver_estadisticas():
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_prom = sum(sueldos) / len(sueldos)
    sueldo_geom = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))

    print(f"Sueldo mas alto: ${sueldo_max}")
    print(f"Sueldo mas bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${sueldo_prom:.2f}")
    print(f"Media geometrica de sueldos: ${sueldo_geom:.2f}")

def reporte_sueldos():
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre trabajador", "Cargo", "Sueldo base", "Descuento salud", "Descuento AFP", "Sueldo liquido"])
        for trabajador, sueldo in zip(trabajadores, sueldos):
            dscto_salud = sueldo * 0.07
            dscto_afp = sueldo * 0.12
            sueldo_liquido = sueldo - dscto_salud - dscto_afp
            writer.writerow([trabajador["nombre"], trabajador["cargo"], sueldo, dscto_salud, dscto_afp, sueldo_liquido])
            print(f"Nombre empleado: {trabajador['nombre']} Cargo: {trabajador['cargo']} Sueldo base: ${sueldo} Descuento salud: ${dscto_salud:.2f} Descuento AFP: ${dscto_afp:.2f} Sueldo liquido: ${sueldo_liquido:.2f}")

def salir_programa():
    print("Finalizando programa..")
    print("Desarrollado por PAULA ULLOA")
    print("Rut 20.654.043-5")

def menu():
    while True:
        print("\nMenú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opcion = int(input("Seleccionar opción: "))

        if opcion == 1:
            sueldos_random()
        elif opcion == 2:
            clasificar_sueldos()
        elif opcion == 3:
            ver_estadisticas()
        elif opcion == 4:
            reporte_sueldos()
        elif opcion == 5:
            salir_programa()
            break
        else:
            print("Opción inválida. Intentar nuevamente.")

if __name__ == "__main__":
    menu()
