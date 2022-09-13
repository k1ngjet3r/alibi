import pyttsx3 

class Text_2_speech:
    def __init__(self, sentence, rate=125, volumn=1.0, voices=1):
        """ Convert entered text to speech by using the pyttsx3 module

        Args:
            sentence (str): text you want the computer to speak.
            rate (int, optional): speaking rate. Defaults to 125.
            volumn (float, optional): volumn level. Defaults to 1.0.
            voices (int, optional): speaking voice, 0 for male and 1 for female. Defaults to 1.
        """        
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volumn', volumn)
        self.engine.setProperty('voices', voices)

        self.sentence = sentence

    def speak(self):
        self.engine.say(self.sentence)
        self.engine.runAndWait()
        self.engine.stop()