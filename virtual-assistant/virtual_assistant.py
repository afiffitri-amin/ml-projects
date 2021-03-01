import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from random import randint
import smtplib
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                print(command)
                command = command.replace('alexa', '')
                print()
            else:
                pass
    except:
        pass
    
    return command

greetings = ['Hello sir! How can I help you?',
            'Good day sir! How may I serve you today?',
            'Greetings sir! Need help with anything?',
            'Happy to see you sir. I am at your service',
            'Hi sir. How can I be of service?']

def greeting():
    
    num = randint(0, len(greetings)-1)
    greet = greetings[num]
    
    return greet

def send_email(receiver, subject, message):
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('xxxxx@gmail.com', 'password')
    email = EmailMessage()
    email['From'] = 'sender_email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'myself': 'myself@gmail.com',
    'my girlfriend': 'xxxxxxx@gmail.com',
    'best friend': 'bestfriend@yahoo.com',
    'mum': 'mum@hotmail.com',
    'dad': 'dad@rocketmail.com'
}

def email_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass
    
def get_email_info():
    
    talk('To Whom you want to send email')
    name = email_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = email_info()
    talk('Tell me the text in your email')
    message = email_info()
    talk('Do you want to send this email?')
    confirm_send = email_info()
    
    if 'yes' in confirm_send:
        send_email(receiver, subject, message)
        
        talk('email sent.')
        
def run_alexa():
    
    command = take_command()
    #print(command)
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person).split('. ')[0:2]
        print(info)
        talk(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
        
    elif 'search' in command:
        search = command.replace('search for', '')
        print('Searching for', search)
        talk('Searching for:' + search)
        pywhatkit.search(search)
        
    elif 'email' in command:
        
        get_email_info()
        
    elif 'go to bed' in command:
        
        talk('Goodbye sir')
        exit()
        
    else:
        talk('Please say the command again.')


talk('Initialization complete. Virtual assistant running.')
start_greet = greeting()
talk(start_greet)
        
while True:
    try:
        run_alexa()
    except:
        pass