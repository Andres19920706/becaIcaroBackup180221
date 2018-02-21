# -*- coding: utf-8 -*-
"""
@Nombre
    BoxTextToSpeech
@Descripción
    Clase que contiente los métodos tts, es decir, permite:
        - Decir una oración.
        - Cambiar los efectos de voz.
        - Cambiar el idioma
        - Cambiar la voz del motor de síntesis.
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
    http://doc.aldebaran.com/2-4/naoqi/audio/altexttospeech.html
"""

class BoxTextToSpeech():

    #Paraámetros especificos
    TONO = "pitchShift"
    DUALVOZ = "doubleVoice"
    GDUALVOZ = "doubleVoiceLevel"
    TSDUALVOZ = "doubleVoiceTimeShift"
    VELOCIDAD = "speed"
    DVELOCIDADVOZ = "defaultVoiceSpeed"


    #Constructor
    def __init__(self):
        self.info()
        pass

    def info(self):
        print """Clase que contiente los métodos tts, es decir, permite:
        \t- Decir una oración.
        \t- Cambiar los efectos de voz.
        \t- Cambiar el idioma
        \t- Cambiar la voz del motor de síntesis."""
        pass

    """
    @Función:
        Say
    @Descripción:
        NAO dice una cadena de texto
    """
    def miSay(self, tts):
            #Obtenemos la cadena de texto a enviar
        frase = raw_input("Introduce la frase a decir (intro por defecto):")
        if frase == "":
            frase = "¡Hola Mundo!"
            pass
            #Enviamos la cadena de texto al módulo TextToSpeech.
        tts.say(frase)

    """
    @Función:
        Speed
    @Descripción:
        NAO modifica la velocidad con la que habla actual.
        El rango permitido de velocidad esta comprendido entre [50~400], siendo
        el valor por defecto el de 100.
    """
    def miSpeed(self, tts):
            #Capturamos la velocidad
        while True:
            try:
                vs = int(input("Introduce la velocidad de habla [50~400] (intro por defecto):"))
            except (SyntaxError, NameError, TypeError):
                vs = 100

            if (vs >= 50 and vs <= 400):
                break

            #Modificmaos el velocidad de voz actual
        tts.setParameter(self.VELOCIDAD, vs)
            #Aplicamos cambios
        tts.resetSpeed()
        pass

    """
    @Función:
        Speed Default
    @Descripción:
        NAO modifica la velocidad por defecto con la que habla.
        El rango permitido de velocidad esta comprendido entre [50~400], siendo
        el valor por defecto el de 100.
    """
    def miSpeedDefault(self, tts):
            #Capturamos la velocidad
        while True:
            try:
                vs = int(input("Introduce la velocidad de habla [50~400] (intro por defecto):"))
            except (SyntaxError, NameError, TypeError):
                vs = 100

            if (vs >= 50 and vs <= 400):
                break

            #Modificmaos el velocidad de voz por defecto
        tts.setParameter(self.DVELOCIDADVOZ, vs)
            #Aplicamos cambios
        tts.resetSpeed()
        pass

    """
    @Función:
        Cambiar el tono o miTono
    @Descripción:
        NAO aplica un cambio de tono a la voz, mediante el parametro "pitchSift"
        El valor indica la relación entre las nuevas frecuencias fundamentales
        y la original.
        El rango aceptalbe es de [1.0~4.0]. Siendo 0, el valor que deshabilita
        el efecto.
        Si por ejemplo, se inserta un valor de:
            - 2.0: indicamos que aumente una octava.
            - 1.5: indicamos que auemnte un quinto de octava.
    """
    def miTono(self,tts):
            #Capturamos la relación entre la fecuencia fundamental y la original
        while True:
            try:
                tn = float(input("Introduce el tono [1.0~4.0] (intro por defecto):"))
            except (SyntaxError, NameError, TypeError):
                tn = 0

            if (tn >= 1.0 and tn <= 4.0 or tn == 0):
                break
            #Modificmaos el velocidad de voz por defecto
        tts.setParameter(self.TONO, tn)
        print ("Comprobrar el nuevo tono del robot.")
        self.miSay(tts)
        pass

    """
    @Función:
        Segudna Voz o miDualVoz
    @Descripción:
        NAO aplica añade una segunda voz, utilizando los siguientes parámetros
        para configurarla:
            - doubleVoice: Agrega una segunda voz respecto a la primera, el rango
                            va entre [1.0 ~ 4.0], siendo el valor de 0 el que
                            deshabilita el efecto.
            - doubleVoiceLevel: Establece una ganancia a la voz adicional, con
                                respecto a la original. El rango va entre
                                [0 ~ 4], siendo el valor de 0, el que deshabilita
                                el efecto.
            - doubleVoiceTimeShift: Establece un retardo entre la segudna voz y
                                    la original. El rango va entre [0 ~ 0.5].
            - pitchShift: Aplica un cambio de tono, ver función "miTono".
        El valor indica la relación entre las nuevas frecuencias fundamentales
        y la original.
    """
    def miDualVoz(self, tts):
            #Voz robotica
        tts.setParameter(self.DUALVOZ, 1)
        tts.setParameter(self.GDUALVOZ, 0.5)
        tts.setParameter(self.TSDUALVOZ, 0.1)
        tts.setParameter(self.TONO, 1.1)
        print "Voz Robotica:"
        self.miSay(tts)
        pass

    """
    @Función:
        Cambiando Lenguaje o miLenguaje
    @Descripción:
        NAO establece un lenguaje del motor de síntesis.
        La lista de idomas disponibles se puede obtener con la función
        getAvailableLanguages .
        Ejemplo de listas de lenguajes:
            [‘French’, ‘Chinese’, ‘English’, ‘German’, ‘Italian’, ‘Japanese’,
            ‘Korean’, ‘Portuguese’, ‘Spanish’]
    """
    def miLenguaje(self,tts):
            #Lista de lenguajes soportados
        print "Lenguajes actual: \n",tts.getLanguage()
        print "Lista de lenguajes: \n",tts.getAvailableLanguages()
        tts.setLanguage('Spanish')
        pass

    """
    @Función:
        Cambiando la voz o miVoz
    @Descripción:
        NAO establece una voz del motor de síntesis.
        La lista de las voces disponibles puede obtener con la función
        getAvailableVoices .
        Ejemplo de listas de voces:
            ['Maria22Enhanced', 'naoenu']
    """
    def miVoz(self,tts):
        print "Voces instaladas: \n",tts.getAvailableVoices()
        tts.setVoice("Maria22Enhanced")
        print "Escuchadno la voz: Maria22Enhanced"
        self.miSay(tts)
        pass

    """
    @Función:
        Etiquetas o miEtiquetas
    @Descripción:
        Una etiqueta, esta disponible para todos los motores de sintonizaicón de
        voz, y permiten camibar la pronuncaicón con respecto al contexto de su
        aplicaicón.
        Etiquetas:
            - vct: Cambia el tono [ valor entre comprendido entre el 50% y el
                    200%, siendo el valor predetermianod el 100% ]
            - rspd: Cambia la velocidad de habla [ valor entre comprendido
                    entre el 50% y el 400%, siendo el valor predetermianod
                    el 100% ]
            - pau: Introduce una pausa de duración x mseg.
            - vol: Cambia el volumen [ valor entre comprendido entre el 0% y
                    el 100%, siendo el valor predetermianod el 80%, nótese, que
                    volumenes superiores al 80% pueden recortar la señal de
                    audio]
            - mrk: Permite insertar un marcador, el cual, puede ser utilizado
                    para sincronizar el habla con una acción específica del robot,
                    cuya acción ha podido ser generada por un evento de
                    "ALTextToSpeech/CurrentBookMark" de ALMemory.
                    [ El valor estra compendrido entre 0 y 64535 ]
            - rst: Permite restablecer las secuencias de control.
            - Etiqeutes de nuance, no estan disponibles para NAO.
            -
    """
    def miEtiquetas (self,tts):
            #Etiqueta de tono (valor = 150%)
        tts.say("\\ vct = 150 \\ Hola mis amigos.")
            #Etiqueta de velocidad de habla (valor = 50 %)
        tts.say("\\ rspd = 50 \\ Hola mis amigos.")
            #Etiqueta de pausa (valor = 3000 mseg.)
        tts.say("Hola mis amigos \\ pau = 3000 \\ ¿cómo están?")
            #Etiqueta de volumen (valor = 50 %)
        tts.say("\\ vol = 50 \\ Hola mis amigos \\vol = 80 \\,¿como están?")
            #Etiqueta para insertar un marcador (etiqeuta 0 y 1)
        tts.say("\\ mrk = 0 \\ Digo una oración. \\ mrk = 1 \\ Digo otra oración ")
            #Etiqueta para restablecer la secuenica de control predetermiando
        tts.say("\\ vct = 200 \\\\ rspd = 20 \\ Hola mis amigos.\\ rst \\ ¿Cómo estás?")
        pass