# --- coding utf-8 ---

import sys
import platform
from datetime import datetime, timedelta
from Ticket import Ticket


# Clase menu donde se realiza el menu principal y donde se reazalira lcada evento segun 
# la opcion que tomo del menu

class Menu:
    """ Clase de inicio, donde se mostrara las opciones del menu 
        y se realizaran las funciones para determinada opcio.
    """
     def __init__(self):
         """ Se asignara una lista los valores que se obtengan  de la clase anterios TICKET"""
         self.vehiculo = Ticket()
         self.opciones = {
                            "1": self.agregar_vehiculo,
                            "2": self.buscar_vehiculo,
                            "3": self.mostrar_ticket,
                            "4": self.mostrar_reporte,
                            "5": self.close
         }

    def menu_desplegable(self):
        """ Se desplegara el menu de opciones del programa. """
        print(""" Bienvenido al sistema  de Genisys Inc

                1. Agreagar un Nuevo Vehiculo
                2. Buscar  Vehiculo
                3. Mostrar Ticket del vehiculo
                4. Mostrar reporte
                5. Salir
        """)
        
    def enter_press():
        """ Al presionar una tecla se tomara el espacion """
        input("\n Presione una tecla para continuar")

    def limpiar_pantalla():
        """ Limpiara la pantalla del programa. """
        if platform.system == "Windows"
            os.system("cls")
         elif plataform.sys == "Darwin" or platform.system == "Linux"
            os.system("clear")
    
     def agregar_vehiculo(self):
         """ se agregara un vehiculo y se crearan las asignaciones de mismo. """
         numero_placa = input("Ingrese el numero de placa")
         marca = input("Ingrese la marca del vehiculo")
         modelo = input("Ingrese el modelo del vehiculo")
         tipo_vehiculo = input("Ingrese el tipo de vehiculo")
         fecha_ingreso = datetime.date
         hora_ingreso = datetime.time
         estado = True

         self.vehiculo.agregar(numero_placa,marca,modelo,tipo_vehiculo,fecha_ingreso,hora_ingreso,estado)
    
    def crear_ticket(self, numero_placa,tipo_vehiculo, fecha_ingreso, hora_ingreso):
        """ se creara el cargo para el vehiculo ingresado"""
        if tipo_vehiculo == "Automovil" and hora_ingreso > 1:
            cargo= 20 * 0.20
        elif tipo_vehiculo == "Motocicleta" and hora_ingreso > 1:
            cargo = 10 * 0.10
        
        return cargo
    
    def mostrar_ticket(self, vehiculos = None):
        """  Muestra los vehiculos ingresados """
        if not vehiculos:
            vehiculos = self.vehiculo.vehiculos
        
        for vehiculo in vehiculos:
            print("Placa:{0}\n Marca : {1}\nModelo: {2}\n Tipo de Vehiculo {3}\n Fecha Ingreso:{4}\nHora de ingreso: {5}\n Estado {6} , cargo {7}"
                    .format(vehiculo.plca, vehiculo.marca, vehiculo.modelo, vehiculo.tipo_vehiculo, vehiculo.fecha_ingreso, vehiculo.hora_ingreso,
                    vehiculo.estado = False, crear_ticket(cargo)))

    def run(self):
        """ funcion para iniciar el programa"""
        while True:
            self.display_menu()
            choise = input("Ingrese una opción: ")
            action = self.options.get(choise)

            if action:
                action()
            else:
                print("¡{0} Esta no es un opcion !".format(choise))

    def buscar_vehiculo(self):
        """ Buscamos un vehiculo en especifico"""
        filter = input("ingrese el texto")
        vehiculo = self.vehiculo.buscar_vehiculo(filter)
        self.mostrar_ticket(vehiculo)
    
if __name__ == "__main__":
    menu = Menu()
    menu.run()




        
