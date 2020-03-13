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
        print(" Bienvenido al sistema  de Genisys Inc
                                Menu:
                1. Agreagar un Nuevo Vehiculo
                2. Buscar  Vehiculo
                3. Mostrar Ticket del vehiculo
                4. Mostrar reporte
                5. Salir
        )
        
    def enter_press():
        """ Al presionar una tecla se tomara el espacion """
        input("\n Presione una tecla para continuar")

    def limpiar_pantalla():
        """ Limpiara la panta
