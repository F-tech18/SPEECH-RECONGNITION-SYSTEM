import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe_audio(self, file_path):
        try:
            with sr.AudioFile(file_path) as source:
                audio = self.recognizer.record(source)

            text = self.recognizer.recognize_google(audio)

            return {
                "status": "success",
                "transcription": text
            }

        except sr.UnknownValueError:
            return {
                "status": "error",
                "message": "Could not understand audio"
            }

        except sr.RequestError:
            return {
                "status": "error",
                "message": "API unavailable"
            }
