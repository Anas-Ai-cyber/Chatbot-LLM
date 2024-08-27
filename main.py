import openai
from apikey import api_data
import pyttsx3
import speech_recognition as sr 
import webbrowser

openai.api_key=api_data

completion = openai.Completion()

def Reply(question):
    prompt = f'Buddy: {question} \n Jarvis : '
    response = completion.create(
        prompt=prompt,
        engine="gpt-3.5-turbo",
        stop=['\Buddy'],
        temperature=0.8,
        max_tokens=200  
    )
    answer = response.choices[0].text.strip()
    return answer


# ans=Reply("What is deep learning?")
# print(ans)  

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("Hello , how are you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print("Buddy said : {}\n".format(query))
    except Exception as e:
        print("Please Say That Again..")
        return None
    return query

def open_google():
    webbrowser.open('https://www.google.com')

def open_youtube():
    webbrowser.open('https://www.youtube.com')

def search_google(query):
    search_url = f'https://www.google.com/search?q={query}'
    webbrowser.open(search_url)

def search_youtube(query):
    search_url = f'https://www.youtube.com/results?search_query={query}'
    webbrowser.open(search_url)

if __name__ == '__main__':
    # speak("Hello , how are you")
    while True:
        query = takeCommand()
        if query is not None:
            query = query.lower()
            print(query)
            if 'bye' in query:
                break
            elif 'open google' in query:
                open_google()
            elif 'open youtube' in query:
                open_youtube()
            elif 'search on google about' in query:
                search_query = query.replace('search on google about', '').strip()
                search_google(search_query)
            elif 'search on youtube about' in query:
                search_query = query.replace('search on youtube about', '').strip()
                search_youtube(search_query)
            else:
                ans = Reply(query)
                print(ans)
                speak(ans)