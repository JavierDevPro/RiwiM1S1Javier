precioUni = 0
cantProduc = 0
percentDescuento = 0
#listado de posibles respuestas validas
respuestas = ["si","s","no","n"]
#funcion que valide valores numericos que sean numeros y valida que las variables cantidad y precio tengan un valor minimo mayor a 0
def validacionValNumMinMax(valor, proceso):  
  while True:
    try:#ejecutamos un try para que en caso de error no se detenga el programa
      match(proceso):
        case 1:
          valor = input("Precio unitario: ").strip()
          nuevoValor = float(valor)
        case 2:
          valor = input("Cantidad: ").strip()
          nuevoValor = int(valor)
        case 3:
          valor = input("Porcentaje descuento de (0-100)%: ").strip()
          nuevoValor = float(valor)
        case _:
          print("watafak chavales")
    except:
        print("ERROR: El valor ingresado no debe poseer valores alfanumericos.")    
    try:
      if not(valor.isalpha()):
        if (proceso == 1 or proceso == 2):
          if nuevoValor > 0:
             break
          else:
             print("ERROR: El valor ingresado debe ser positivo.")
        elif (proceso == 3):
          if (nuevoValor > 0 and nuevoValor <= 100):
            break
        else:          
          print("ERROR: El valor ingresado debe estar en el rango de (0-100)")
    except:
      continue
  return nuevoValor
print("Ingrese los datos del producto que va a comprar.")
produc = input("nombre: ")
precioUni = validacionValNumMinMax(precioUni, 1)
cantProduc = validacionValNumMinMax(cantProduc, 2)
validDescuento = input("desea implementar descuento? Si/No.")#se toma el valor de la respuesta
while validDescuento.lower() not in respuestas:#ciclo que valide que el valor este en la lista de respuestas
  validDescuento = input("Respuesta invalida, desea implementar descuento? Si/No: ")
if (validDescuento.lower() == "si" or validDescuento.lower() == "s"):
  percentDescuento = validacionValNumMinMax(percentDescuento, 3)