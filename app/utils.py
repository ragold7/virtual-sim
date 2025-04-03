import nltk
from nltk.tokenize import word_tokenize

def respond_to_user(message):
    if "hello" in message.lower():
        response = "Hi there! How can I assist you today?"
    elif "call" in message.lower():
        response = "Simulating a call... Ring... Ring..."
    else:
        response = "I'm still learning, please try rephrasing that."

    save_to_database(message, response)
    speak_text(response)  # Speak the bot's response
    return response


import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a voice input...")
        try:
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Sorry, I'm having trouble connecting to the speech service."

import pyttsx3

def speak_text(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()


import sqlite3

# Save user input and bot response to the database
def save_to_database(user_input, bot_response):
    conn = sqlite3.connect('database/database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chat_history
                 (id INTEGER PRIMARY KEY, user_input TEXT, bot_response TEXT)''')
    c.execute("INSERT INTO chat_history (user_input, bot_response) VALUES (?, ?)", 
              (user_input, bot_response))
    conn.commit()
    conn.close()

# Retrieve conversation history
def get_conversation_history():
    conn = sqlite3.connect('database/database.db')
    c = conn.cursor()
    c.execute("SELECT user_input, bot_response FROM chat_history ORDER BY id DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return rows
