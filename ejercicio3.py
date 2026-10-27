import math

print("\n--- CALCULADORA GEOMÉTRICA ---")
print("1. Área de un círculo")
print("2. Calcular hipotenusa")
print("3. Resolver ecuación cuadrática")
print("4. Salir")
    
opcion = int(input("Seleccione una opción: "))
    
    # Opción 1: Área de un círculo
if opcion == 1:
        radio = float(input("Ingrese el radio: "))
        if radio >= 0:
            area = math.pi * (radio ** 2)
            print("Área del círculo:", area)
        else:
            print("Error: El radio debe ser mayor o igual que cero.")
            
    
elif opcion == 2:
        a = float(input("Ingrese el cateto a: "))
        b = float(input("Ingrese el cateto b: "))
        if a > 0 and b > 0:
            hipotenusa = math.sqrt((a ** 2) + (b ** 2))
            print("Hipotenusa:", hipotenusa)
        else:
            print("Error: Los dos catetos deben ser mayores que cero.")
            
    
elif opcion == 3:
        a = float(input("Ingrese el coeficiente a: "))
        b = float(input("Ingrese el coeficiente b: "))
        c = float(input("Ingrese el coeficiente c: "))
        
        if a == 0:
            print("No es una ecuación cuadrática.")
        else:
            
            discriminante = (b ** 2) - (4 * a * c)
            
            if discriminante > 0:
                solucion1 = (-b + math.sqrt(discriminante)) / (2 * a)
                solucion2 = (-b - math.sqrt(discriminante)) / (2 * a)
                print("Primera solución:", solucion1)
                print("Segunda solución:", solucion2)
            elif discriminante == 0:
                solucion = -b / (2 * a)
                print("La única solución real es:", solucion)
            else:
                print("No existen soluciones reales.")
                
    # Opción 4: Salir
elif opcion == 4:
        print("Programa finalizado.")

        
else:
 print("Opción inválida. Intente de nuevo.")
