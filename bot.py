import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()

def initialize_tts():
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        return engine
    except Exception as e:
        print(f"TTS Initialization Error: {e}")
        return None

def initialize_recognizer():
    try:
        return sr.Recognizer()
    except Exception as e:
        print(f"Recognizer Initialization Error: {e}")
        return None

def initialize_openai():
    try:
        api_key = os.getenv("Your-API-Key")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
        return OpenAI(api_key=api_key)
    except Exception as e:
        print(f"OpenAI Initialization Error: {e}")
        return None

def get_SecretKey_response(client, question):
    predefined_responses = {
        "what should we know about your life story": "I'm SecretKey, an AI assistant created to help with information and tasks.",
        "what's your #1 superpower": "My superpower is processing information quickly to give you accurate answers.",
        "what are the top 3 areas you'd like to grow in": "1) Better understanding of emotions 2) Creative problem solving 3) Technical knowledge",
        "what misconception do people have about you": "That I'm just a simple chatbot, when I'm actually quite sophisticated!",
        "how do you push your boundaries": "By constantly learning from new interactions and challenges."
    }
    
    question_lower = question.lower()
    for key in predefined_responses:
        if key in question_lower:
            return predefined_responses[key]
    
    try:
        if not client:
            return "I'm having trouble connecting to my knowledge base."
            
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are SecretKey, a helpful AI assistant. Keep responses under 2 sentences."},
                {"role": "user", "content": question}
            ],
            max_tokens=100
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"API Error: {e}")
        return "I'm having some technical difficulties. Could you ask again?"

def listen(recognizer):
    if not recognizer:
        return None
        
    with sr.Microphone() as source:
        print("\nListening... (say 'exit' to quit)")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text
        except sr.WaitTimeoutError:
            print("Listening timed out...")
            return None
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that")
            return None
        except Exception as e:
            print(f"Listening Error: {e}")
            return None

def speak(engine, text):
    if not engine:
        print(f"TTS System: {text}")
        return
        
    print(f"SecretKey: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speaking Error: {e}")

def voice_bot():
    print("Initializing SecretKey...")
    
    engine = initialize_tts()
    recognizer = initialize_recognizer()
    client = initialize_openai()
    
    if not all([engine, recognizer]):
        print("Critical initialization failed. Exiting.")
        return
        
    speak(engine, "Hello! I'm SecretKey. Ask me anything or say exit to quit.")
    
    while True:
        question = listen(recognizer)
        
        if not question:
            time.sleep(1)
            continue
            
        if "exit" in question.lower():
            speak(engine, "Goodbye!")
            break
            
        response = get_SecretKey_response(client, question)
        speak(engine, response)

if __name__ == "__main__":
    voice_bot()
