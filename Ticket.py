# -- coding utf-8 ---

from Vehiculo import Vehiculo

# Se crea una segunda class ticket que es donde se data todo los datos y se crearan las listas del mismo

class Ticket:
    """ En esta clase de le daran valores o se utilizaran los metodos para crear
        para darte inicilizacion a los valores del vehiculo procedente del cliente.
    """

    def __init__(self):
        """ Representa el inicio de los valore del programa en este caso del vehiculo."""
        self.vehiculo = list()
    
    def agregar_vehiculo(self):
        """ Se Creara la funcion para ingresar los valores del vehiculo. """"
        self.vehiculo.append(Vehiculo(numero_de_placa,marca,modelo,tipo_vehiculo,fecha_ingreso,hora_ingreso, estado))
    
    def buscar_vehiculo(self, filter):
        """ Se buscara o se encontraran todos los valores del vehiculo.""""
    


