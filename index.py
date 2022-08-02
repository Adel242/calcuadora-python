# quiero hacer una calculadora con un menu que me permita escoger eentre las siguientes operaciones matematicas:
# suma / resta / mult / div
# menu de salida de datos
# validar tipo de dato
# menu principal

import operation

def menu():

	while True:

		print("------------------------------------")
		print("*****WELCOME TO MENU CALCULATOR*****")
		print("seleccione una operacion matematica \n")
		print("1 = +")
		print("2 = -")
		print("3 = *")
		print("4 = /")
		print("presione 5 si desea salir")
		print("------------------------------------")

		try:
			ope = int(input("\nIngrese una opcion disponible: "))
		except UnboundLocalError:
			print("UnboundLocalError: algo salio mal")
		except ValueError:
			print("Value error: ingrese un tipo de dato valido (numerico)")

	# suma
		if ope == 1:
			a = int(input("ingrese el primer valor: "))
			b = int(input("ingrese el segundo valor: "))
			value = operation.sum(a, b)

			print("el resultado es: " , value)

	# resta
		if ope == 2:
			a = int(input("ingrse el primer valor: "))
			b = int(input("ingrese el segundo valor: "))
			value = operation.rest(a, b)

			print("el resultado es" , value)

	# mult
		if ope == 3:
			a = int(input("ingrese el primer valor: "))
			b = int(input("ingrese el segundo valor: "))
			value = operation.mult(a, b)

			print("el resultado es: ", value)

	# div 
		if ope == 4:
			a = int(input("ingrese el primer valor: "))
			b = int(input("ingrese el segundo valor: "))
			value = operation.div(a, b)

			print("el resultado es: " , value)

	# exit
		if ope == 5:
			print("has salido del menu")
			break		

		if ope < 1 or ope > 5:
					print("\n> eliga una opcion valida del menu <\n")

menu()

	





	


    







    





# mult
# div

