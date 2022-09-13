import speech_recognition as sr
import pyaudio
import time 


class Interrogation:
    """
        Convert speech recorded from mic and return the transcript of the speech using SpeechRecognizer module with Pocketsphinx API.
    """    
    def __init__(self, mic_index):
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
            print('adjusting the noise')
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print('Finished! count down in 5')\

            time.sleep(5)
            print('listening...')
            audio = self.recognizer.listen(source, timeout=20, phrase_time+)

        try:
            return self.recognizer.recognize_sphinx(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            print('API Unavailible')
        except sr.UnknownValueError:
            # Speech was unintelligible
            print("Fail to recognize the phrase!")
        

if __name__ == '__main__':
    print(Interrogation(mic_index=2).listen_from_mic())