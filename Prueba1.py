contraseña_correcta = "Luna2008"
contraseña_ingresada = input ("Ingrese su contraseña: ")

if contraseña_ingresada == contraseña_correcta:
  print("CONTRASEÑA INGRESADA CON EXITO!")
else: 
  print("CONTRASEÑA ERRONEA. Intentelo de nuevo .\n")
  contraseña_ingresada = input("Ingrese su contraseña: ")

  if contraseña_ingresada != contraseña_correcta:
   print("CONTRASEÑA ERRONEA .\n INTENTOS RESTANTES: 0 .\n INTENTE MÁS TARDE")