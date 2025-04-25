#Declaracion e iniciacion de variables para evitar errores en las condiciones y procesos que evaluen o tomen estos valores
unitPrice = 0
productQty = 0
percentDiscount = 0
discount = False
#listado de posibles respuestas validas
answersList = ["si","s","no","n"]
#funcion que valide valores numericos que sean numeros y valida que las variables cantidad y precio tengan un valor minimo mayor a 0
def validacionValNumMinMax(value, process):  
  while True:#ciclo que busca validar y corregir errores en el ingreso de datos segun el proceso en el que va el codigo
    valid = True#Bandera para evitar que se ejecuten 2 errores seguidos
    try:#ejecutamos un try para que en caso de error no se detenga el programa
      match(process):#estructura match muy similar al switch case en otros lenguajes que evalua si se cumple una condicion de un valor exacto
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
        valid = False  
    try:
      if (not(value.isalpha()) and valid == True): #and value.isdigit()
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
#Funcion que calcule el total y devuelve una lista de la cual expondres mis valores obtenidos
def totalCalculation(prodQty, unitP, percent):
  listValues = []
  sub = prodQty * unitP
  discValue = (sub * (percent / 100))
  tot = sub - discValue
  listValues.append(sub)
  listValues.append(discValue)
  listValues.append(tot)
  return listValues
#La siguiente seccion es el punto de salida y ejecucion de la funciones anteriores
print("Ingrese los datos del producto que va a comprar.")
productName = input("nombre: ")
unitPrice = validacionValNumMinMax(unitPrice, 1)
productQty = validacionValNumMinMax(productQty, 2)
validDiscount = input("desea implementar descuento? Si/No.")#se toma el valor de la respuesta
while validDiscount.lower() not in answersList:#ciclo que valide que el valor este en la lista de respuestas
  validDiscount = input("Respuesta invalida, desea implementar descuento? Si/No: ")
if (validDiscount.lower() == "si" or validDiscount.lower() == "s"):#si la respuesta fue si se calcula el descuento
  discount = True
  percentDiscount = validacionValNumMinMax(percentDiscount, 3)
listFinal = totalCalculation(productQty, unitPrice, percentDiscount)#se llama la funcion de calculo
#se imprimen los datos finalmente calculados
print("**********************************************************")
print("Nuevo producto adquirido!")
print("producto: ", productName)
print("valor unitario: $ ", unitPrice)
print("cantidad: ", productQty)
if (discount==True):
  print("porcentaje descontado: ", percentDiscount,"%")
  print(f"valor descontado: $ {round(listFinal[1])} ")#se redondea el resultado
  print("subtotal: $ ", listFinal[0])
print("TOTAL: $ ", listFinal[2])
print("**********************************************************")