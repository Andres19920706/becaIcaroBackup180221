# -*- coding: utf-8 -*-
"""
@Descripción
    Conexión con NAO e integración de los servicios de voz e imagen
@autor
    Andres Ruiz Peñuela
@turor/es
    Raquel
    José Manuel
@version
    0.0.1
"""

"""
Importación de librerias
"""
#Libreias del sistema
import sys

#Liemerias de NAOqi para Python
from naoqi import ALProxy

#Librerias propias del sistema
    #Ruta de nuestras librerias
sys.path.append('./lib')
    #Clase con los atributos de NAO
import DAONAO
    #Clase con las constantes del proyecto
import CONSTANTES as cts
    #Clase con las operaciones tts
import BoxTextToSpeech
    #Clase con las operaiocnes de animaicón de texto
import BoxAnimatedSpeech
"""
Funciones auxiliares
"""
def saludo():
    print "Bienvenido!! :)"
    pass

"""
Función main
"""
if __name__ == '__main__':
    #Cargamos el saludo
    saludo()

    #Obtenemos los parámateros de conexión con NAO
        #Capturamos la IP y el peurto de NAO
    ip = raw_input("Introduce la ip (intro por defecto):")
    if ip == "":
        #ip = "127.0.0.1"
        ip = "192.168.1.39"
        pass
    try:
        puerto = int(input("Introude el puerto (intro por defecto):"))
    except (SyntaxError, NameError, TypeError):
        puerto = 9559
        #Intanciamos la clase DAONAO
    miNAO = DAONAO.DAONAO(ip, puerto)
    print "Conectado a: \n\t-IP:", miNAO.IP, "\n\t-Puerto:", miNAO.Port

    #Módulo TTS
        #CreaMos un proxy para utilizar los comandos TTS
    tts = ALProxy(cts.SPEECH, miNAO.IP, miNAO.Port)

        #Intanciamos una clase con las funcioens o comandos TTS
    miBoxSpeech = BoxTextToSpeech.BoxTextToSpeech()

        #Utilizmaos la funcion say del modulo TTS
    miBoxSpeech.miSay(tts)

        #Utilizamos la funcion speech
    miBoxSpeech.miSpeed(tts)

        #Modificmaos el tono
    miBoxSpeech.miTono(tts)

        #Añadiendo una segunda voz
    miBoxSpeech.miDualVoz(tts)

        #Cambiando el lenguaje
    miBoxSpeech.miLenguaje(tts)

        #Cambiando la voz
    miBoxSpeech.miVoz(tts)

        #Utilizando etiquetas
    miBoxSpeech.miEtiquetas(tts)
    
        #FIN de las funicones del modulo
    print "Fin del modulo TTS"
    
    #Módulo Habla animada
    miBoxAnimado = BoxAnimatedSpeech.BoxAnimatedSpeech()
    pass

#version eclipse nueva: C:\Users\Andres\eclipse-workspace