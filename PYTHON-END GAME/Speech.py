import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak a message
def speak(message):
    engine.say(message)
    engine.runAndWait()

# Define a function to listen for a command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("You said:", command)
            return command
        except:
            print("Sorry, I didn't catch that.")
            return ""

# Define some sample commands
commands = {
    "hello": "Harpal Sir! How can I help you?",
    "what is your name": "My name is Voice Assistant.",
    "how are you": "I'm doing well, thank you for asking.",
    "goodbye": "Goodbye! Have a nice day."
}

# Start the program
speak("Hello! How can I help you?")

while True:
    command = listen().lower()

    if command in commands:
        speak(commands[command])
    elif command == "stop":
        break
    else:
        speak("Sorry, I didn't understand that command. Can you please try again?")
