#validacion de tipo de dato
# def validacionDato():


#una funcion para validar que las variables cantidad y precio tengan un valor minimo mayor a 0
def validacionMIN(valor, valMin):
  if (valor > valMin):
    return True
  else:
    return False

#una funcion para validar que se cumpla un rango!
def validacionMinMAX(valor, valMin, valMax):
  if ((valor >= valMin) and (valor <= valMax)):
    return True
  else:
    return False
  
#validar respuesta


#primero se busca ingresar y declarar las variables que almacenaran los datos solicitados.
print("Ingrese los datos del producto que va a comprar.")
produc = input("nombre: ")

#listado de posibles respuestas validas
respuestas = ["si","s","no","n"]

precioUni = float(input("precio unitario: "))
#serie de condiciones que llaman las validaciones
if (validacionMIN(precioUni, 0) == True):
  cantPro = int(input("cantidad: "))
  if (validacionMIN(cantPro, 0) == True):

    validDescuento = input("desea implementar descuento? Si/No.")#se toma el valor de la respuesta
    while validDescuento.lower() not in respuestas:#ciclo que valide que el valor este en la lista de respuestas
      validDescuento = input("Respuesta invalida, desea implementar descuento? Si/No.")

    if (validDescuento.lower() == "si" or validDescuento.lower() == "s"):
      try:
        percentOfert = float(input("porcentaje descuento: "))

        if (validacionMinMAX(percentOfert, 0, 100) == True):
          print("waaaa")
      except:
        print("Error de tipo de dato")        
  else:
    print("valor ingresado incorrecto, intentelo otra vez.")
else:
  print("valor ingresado incorrecto, intente de nuevo.")
