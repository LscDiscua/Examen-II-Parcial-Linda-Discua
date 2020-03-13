# -- coding utf-8 ----
# Examen II Parciall
# Autora: Linda Sarahi Carranza Discua

from datetime import datetime, timedelta
# Primera clase o objeto Vehiculo

class Vehiculo:
    """ En esta clase se hara la inicializacion de valores  del objeto dandole l
        las caracteristicas necesarias del vehiculo.
    """

    def __init__(self, numero_de_placa, marca, modelo, tipo_vehiculo, fecha_ingreso, hora_ingreso, estado):
        """ Se inicializara y se declaran los valores dependientes de este objeto en este 
            el vehiculo.
        """
        self.numero_de_placa = numero_de_placa
        self.marca = marca
        self.modelo = modelo
        self.tipo_vehiculo = tipo_vehiculo
        self.fecha_ingreso = datetime.date.fecha_ingreso
        self.hora_ingreso = datetime.time.hora_ingreso
        self.estado = True
    
    def search(self, filter):
        """ Buscara un vehiculo especifico en la con sun filtro """
         return filter in self.numero_de_placa or filter self.tipo_vehiculo
    
    




