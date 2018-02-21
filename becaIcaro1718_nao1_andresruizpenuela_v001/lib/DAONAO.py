# -*- coding: utf-8 -*-
"""
@Nombre
    DAONAO
@Descripción
    Clase para modelar las características principales de NAO
@autor
    Andres Ruiz Peñuela
@turor/es
    Raquel
    José Manuel
@version
    0.0.1
"""
class DAONAO():
    IP = ""
    Port = 0

    #Constructor con parámetros
    def __init__(self, IPnao=None, PORTnao=None):
        if (IPnao == None or PORTnao == None):
                #Valor por defecto
            self.IP = "127.0.0.1"
            self.Port = 9559
        else:
            self.IP = IPnao
            self.Port = PORTnao
        pass

