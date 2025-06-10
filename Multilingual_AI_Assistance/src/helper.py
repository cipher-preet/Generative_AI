import speech_recognition as sr
import google.generativeai as genai

from dotenv import load_dotenv
import os
from gtts import gTTS


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


def voice_input():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))



def text_to_speech(text):
    tts=gTTS(text=text, lang="en")
    
    #save the speech from the given text in the mp3 format
    tts.save("speech.mp3")

def llm_model(user_text):
    try:
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        if not GOOGLE_API_KEY:
            raise ValueError("Google API key not found. Please set it in your .env file.")

        genai.configure(api_key=GOOGLE_API_KEY)

        model = genai.GenerativeModel('gemini-pro')
        print("Input text:", user_text)

        response = model.generate_content(user_text)
        result = getattr(response, "text", None)

        if result is None:
            raise ValueError("No text found in response.")

        print("Generated content:", result)
        return result

    except Exception as e:
        print("An error occurred:", str(e))
        return "Sorry, an error occurred while generating the response."
