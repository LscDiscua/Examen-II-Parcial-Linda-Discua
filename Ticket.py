# -- coding utf-8 ---

from Vehiculo import Vehiculo

# Se crea una segunda class ticket que es donde se data todo los datos y se crearan las listas del mismo

class Ticket:
    """ En esta clase de le daran valores o se utilizaran los metodos para crear
        para darte inicilizacion a los valores del vehiculo procedente del cliente.
    """

    def __init__(self):
        """ Representa el inicio de los valore del programa en este caso del vehiculo."""
        self.vehiculos = list()
    
    def agregar(self):
        """ Se Creara la funcion para ingresar los valores del vehiculo. """"
        self.vehiculos.append(Vehiculo(numero_de_placa,marca,modelo,tipo_vehiculo,fecha_ingreso,hora_ingreso, estado))
    
    def _buscar_vehiculo(self, numero_de_placa):
        """ Buscar un vehiculo en especicfico se creara una clase privada para ello """
         for vehiculo in self.vehiculos:
             if numero.placa == numero_de_placa:
                 return vehiculo
        return None
    
    
    def buscar_vehiculo(self, filter):
        """ Se buscara o se encontraran todos los valores del vehiculo.""""
        return [vehiculo for vehiculo in self.vehiculos if note.buscar(filter)]

    


