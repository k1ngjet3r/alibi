import pyttsx3 

class Text_2_speech:
    """
        Convert entered text to speech by using the pyttsx3 module
    """    
    def __init__(self, rate=125, volumn=1.0, voices=1):
        """
            Setup for the class
        Args:
            rate (int, optional): speaking rate. Defaults to 125.
            volumn (float, optional): volumn level. Defaults to 1.0.
            voices (int, optional): speaking voice, 0 for male and 1 for female. Defaults to 1.
        """        
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volumn', volumn)
        self.engine.setProperty('voices', voices)


    def speak(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
        self.engine.stop()

if __name__ == '__main__':
    Text_2_speech().speak('This is a test')