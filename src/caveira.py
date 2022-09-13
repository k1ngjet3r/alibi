import speech_recognition as sr
import pyaudio


class Interrogation:
    """
        Convert speech recorded from mic and return the transcript of the speech using SpeechRecognizer module with Pocketsphinx API.
    """    
    def __init__(self, mic_index=1):
        """ Initial Setup for recognizer and the mic

        Args:
            mic_index (int): index of mic listed in the computer
        """        
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone(device_index=mic_index)

    def listen_from_mic(self):
        """
            Listen the speech from the mic and return the transcript

        Returns:
            str: converted transcript of the speech
        """
        
        with self.mic as source:
            # Adjust the mic with teh ambinet noise
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source, timeout=10, phrase_time=20)

        try:
            return self.recognizer.recognize_sphinx(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            print('API Unavailible')
        except sr.UnknownValueError:
            # Speech was unintelligible
            print("Fail to recognize the phrase!")