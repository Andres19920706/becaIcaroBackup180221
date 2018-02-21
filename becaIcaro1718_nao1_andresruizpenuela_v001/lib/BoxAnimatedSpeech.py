# -*- coding: utf-8 -*-
"""
@Nombre
    BoxAnimatedSpeech
@Descripción
    Clase que contiente los métodos para que el robot hable de una manera
    expresiva.

    Las opciones permitidas son:
        - Crear un discurso animado mediante:
            a) La anotaicón deL texto con alguans instrucciones.
            b) Agregando animaicones para alguans palabras mediante el módulo
                ALSpeakingMovement.
        - Desactivar el módulo ALSpeakingMovement, por la API de este módulo o
            llamando a la instruccion ^, para que el robot solo ejecute sus
            instrucciones y no se meuva fuera de ellas.
    
    El funcionamiento consiste:
        A: El módulo ALAnimatedSpeech recibe texto que puede anotarse con
            instrucciones.
        B: Divide el texto en pequeños trozs.
        C: Analiza el texto y anota las cosas que reconoce para elegir 
            movimiento contextuales.
        D: Caulqier parte del texto que no esté anotada con animaciones, esta 
            llena de animaicones lanzadas por ALSpeakingMovement.
        E: El robót prepara al robot para ejecutar cada instrucción, de modo 
            que pueda ejecutarse tan pronto sea neceario, permitiendo que el 
            habla y las instrucciones estén bien sincronizadas.
        F: El módulo ALAnimatedSpeech hace que el robot diga el texto y vigile
            el discurso para inicar las intruccioens en el momento correcto.
@API:
    NAOqi Audio
@autor
    Andres Ruiz Peñuela
@turor/es
    Raquel
    José Manuel
@version
    0.0.1
@Fuene
    http://doc.aldebaran.com/2-4/naoqi/audio/alanimatedspeech.html
"""

class BoxAnimatedSpeech():

    #Constructor
    def __init__(self):
        self.info()
        pass

    def info(self):
        print """Clase que contiente los métodos para que el robot 
        hable de una manera expresiva."""
        pass
    
    """
    @Función:
        Texto anotado o miTextoAnotado
    @Descripción:
        El texto anotado, consite en una cadena que comibna el texto que
        se debe deicr y las instruicones que gestionan los comportamienteos.
        
        Por ejemplo:
        "¡Hola! ^ start (animations/Stand/Gestures/Hey_1) Encantado de conocerte!"
        
        En este caso:
            -  El robot dice ¡Hola! al mismo teimpo que:
                * Inicia la ejecución de la animación Hey_1
            - Dice encantado de conocerte, terminando la animación abruptamente,
                tras decir el texto.
        Si, se desea que siga funcionando la animaicón, se puede insertar la
        instrucción ^wait al final, tal que asi:
        
        "¡Hola! ^ Start (animations/Stand/Gestures/Hey_1) Encantado de conocerte ^ wait (animations/Stand/Gestures/Hey_1)"
    """