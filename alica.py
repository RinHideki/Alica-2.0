import speech_recognition as sr 
import pyttsx3
import random *



def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

def listen_amd_save():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        talk('Чо, придурок что ли?')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        task = r.recognize_google(audio, language = 'ru-RU').lower()
    except sr.UnknownValueError:
        talk('Нарываешься?')
        task = listen_amd_save()
    return task

def peasant(task):
    if 'привет' in task:
        talk('Пока')
    else:
        talk('Фу фу фу')
    if 'а' in task:
        li = ['ты великорусский сервелат', 'осознай свою ничтожность', 'Чернила ты', 'я проломлюсь в твою жизнь', 'Катастрофичный выбор программы', 'Ровно', 'Засольный', 'Синонимика', 'Управляемый человек', 'Матка', 'Постреливать в твоё сознание', 'компьютер просветлел', 'Покладистый человек', 'перелив сил в программу', 'я выселяю тебя из твоей квартиры', 'я буду держать тебя взаперти']
        choice(li)
peasant(listen_amd_save())