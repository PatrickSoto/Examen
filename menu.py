# -*- coding: UTF8 -*-
#nombre:menu
#funcion:programa de estacionamiento
#autor: PATRICK DAVID SOTO
#Repositorio: https://github.com/PatrickSoto/Examen.git
#fecha:03/13/2020
import sys
import platform
import datetime
import random


class Menu:
    """
    Desplegando El Menu De Opciones
    """

    def __init__(self):
            """ Muestra La Lista  """
            self.Vehiculo = list()
        
            self.options = {"1":self.ingreso,
                            "2":self.totalVehiculos,
                            "3":self.salidas,
                            "4":self.gananciasDia,
                            "5":self.salir
                            }

    def display_menu(self):
        """ 
        
         Inicializa el meno
        
        
         """
        print("""
             Menú principal

            1:Ingreso
            2:Vehiculos registrados
            3:Salida
            4:Ganancias En El dia
            5:salir
             """)
    def ingreso(self):
        placa = input("placa: ")
        marca = input("vehiculo: ")
        modelo = input("Modelo: ")
        tipo_de_vehiculo = input(" tipo de  vehiculo: ")
        hora_ingreso = input("hora de entrada: ")
        estado = input("estado: ")
        print("La actualizacion se ha generado correctamente")
        pass

    def totalVehiculos(self):
 
        for vehi in vehiculos:
            print("placa: {0}\nMarca: '{1}'\nModelo: {2}\nTipo: {3}"
                  .format())



    def salida(self):
         pass

    def gananciasDia(self):
         pass

    def salir(self):
          """ 
          manda a cerrar la aplicacion

          """
        print("la aplicacion se cerro")
        sys.exit(0)




    def horas(self):
        horas_vehiculo=random(1,5)
        print(horas_vehiculo)

