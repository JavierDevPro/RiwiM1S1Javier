unitPrice = 0
productQty = 0
percentDiscount = 0
discount = False
#listado de posibles respuestas validas
answersList = ["si","s","no","n"]
#funcion que valide valores numericos que sean numeros y valida que las variables cantidad y precio tengan un valor minimo mayor a 0
def validacionValNumMinMax(value, process):  
  while True:
    try:#ejecutamos un try para que en caso de error no se detenga el programa
      match(process):
        case 1:
          value = input("Precio unitario: ").strip()
          newValue = float(value)
        case 2:
          value = input("Cantidad: ").strip()
          newValue = int(value)
        case 3:
          value = input("Porcentaje descuento de (0-100)%: ").strip()
          newValue = float(value)
        case _:
          print("watafak chavales")
    except:
        print("ERROR: El valor ingresado no debe poseer valores alfanumericos.")    
    try:
      # if not(value.isalpha()):
        if (process == 1 or process == 2):
          if newValue > 0:
             break
          else:
             print("ERROR: El valor ingresado debe ser positivo.")
        elif (process == 3):
          if (newValue > 0 and newValue <= 100):
            break
          else:          
            print("ERROR: El valor ingresado debe estar en el rango de (0-100)")
    except:
      continue
  return newValue
#Funcion que calcule el total
def totalCalculation(prodQty, unitP, percent):
  sub = prodQty * unitP
  discValue = sub * (percent / 100)
  tot = sub - discValue
  return tot
print("Ingrese los datos del producto que va a comprar.")
productName = input("nombre: ")
unitPrice = validacionValNumMinMax(unitPrice, 1)
productQty = validacionValNumMinMax(productQty, 2)
validDiscount = input("desea implementar descuento? Si/No.")#se toma el valor de la respuesta
while validDiscount.lower() not in answersList:#ciclo que valide que el valor este en la lista de respuestas
  validDiscount = input("Respuesta invalida, desea implementar descuento? Si/No: ")
if (validDiscount.lower() == "si" or validDiscount.lower() == "s"):
  discount = True
  percentDiscount = validacionValNumMinMax(percentDiscount, 3)
print("**********************************************************")
print("Nuevo producto adquirido!")
print("producto: ", productName)
print("cantidad: ", productQty)
if (discount==True):
  print("porcentaje descontado: ", percentDiscount,"%")
  #print("valor descontado: ")
print("TOTAL: $",totalCalculation(productQty, unitPrice, percentDiscount))
print("**********************************************************")
  