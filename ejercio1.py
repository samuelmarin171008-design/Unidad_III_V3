#nombres: Samuel Marin C.i = 32.761.682
#nombres: Angelo Sanchez C.i: 33.107.803
   
lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))


if lado1 > 0 and lado2 > 0 and lado3 > 0:
    
    
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        print("Los lados ingresados forman un triángulo válido.")
        
        
        if lado1 == lado2 and lado2 == lado3:
            print("Tipo de triángulo: equilátero.")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Tipo de triángulo: isósceles.")
        else:
            print("Tipo de triángulo: escaleno.")
            
    else:
        print("Los lados ingresados no forman un triángulo.")

else:
    print("Error: todos los lados deben ser mayores que cero.")
    

     
        
        




