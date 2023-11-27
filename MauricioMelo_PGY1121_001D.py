import os
os.system ("cls")

menu = """
1. Grabar
2.Buscar
3.Imprimir Certificados
4.Salir 

"""
Grabar = []
Buscar = []
ImprimirCertificado = []
Certificados = []
indice = []
nombre_dueño = []
tipo_auto = []
marca_auto =[]
numero_patente = []
Salir = []




def tipo_auto():
      print("Menu")
      print("1 Auto")
      print("2.Camioneta")
      print("3.SUV")
      print("4. Salir")
      return input("Elija La opcion")

def Grabar():
      print("Ingrese los datos que desea grabar:")
      patente = int(input("Ingrese el numero de patente: {patente}"))
      tipo    = int(input("Ingrese el tipo de auto: {tipo}"))
      marca   = int(input("Ingrese la marca: {marca}"))
      precio  = int(input("Precio del vehicuulo: {precio}"))
      multas  = int(input("Cantidad de multas a la fecha: {multas}"))
     
def Buscar():
       print("Buscar:")
       try: 
           patente = int(input("Patente a buscar:  "))
        if buscar in patente:
           indice = patente.index(patente)
           print("Patente Encontrada: ")
           print(f" Nombre del dueño : {nombre_dueño}")
           print(f"tipo de auto      : {tipo_auto}")
           print(f"marca del auto    : {marca_auto}")
           print(f"Numero de patente : {numero_patente}")
        else:
            print("Datos no encontrados")
    except:
       print("Se a realizado una excepcion")

def ImprimirCertificado():
           print("   LISTA DE CERTIFICADOS")
           print("------------------------")
           for i in range (len(Certificados)):
           print ("------------------------")


def Salir():
      print("Salir")

#principal 


while True:
    try: 
          opcion = menu()
          if opcion == "1":
            Grabar()
            break
          elif opcion == "2":
               Buscar()
          elif opcion == "3":
                Buscar()
    else: 
        print("opcion incorrecta,porfavor vuelva a intentarlo")
        input("ENTER PARA CONTINUAR")
        os.system("cls")
except:
    print("Excepcion")