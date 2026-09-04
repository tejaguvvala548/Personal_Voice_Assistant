import threading
import time
import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes
import requests
import pywhatkit
from ddgs import DDGS
import os
import webbrowser
from urllib.parse import quote
import xml.etree.ElementTree as ET
import winsound

recognizer = sr.Recognizer()
engine = pyttsx3.init()
speech_lock = threading.Lock()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen(message="Listening..."):
    with sr.Microphone() as source:
        if message:
            print(message)

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:
            return ""

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return ""

def get_wikipedia_summary(topic):
    search_url = "https://en.wikipedia.org/w/api.php"

    headers = {
        "User-Agent": "PersonalVoiceAssistant/1.0"
    }

    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": topic,
        "format": "json"
    }

    search_response = requests.get(
        search_url,
        headers=headers,
        params=search_params
    )

    if search_response.status_code != 200:
        return None

    search_data = search_response.json()
    results = search_data["query"]["search"]

    if not results:
        return None

    best_title = results[0]["title"]

    summary_url = (
        "https://en.wikipedia.org/api/rest_v1/page/summary/"
        + best_title.replace(" ", "_")
    )

    summary_response = requests.get(
        summary_url,
        headers=headers
    )

    if summary_response.status_code == 200:
        data = summary_response.json()
        return data.get("extract")

    return None

def get_news():
    try:
        url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            root = ET.fromstring(response.content)

            items = root.findall(".//item")

            headlines = []

            for item in items[:5]:
                title = item.find("title")

                if title is not None:
                    headlines.append(title.text)

            return headlines

        return []

    except Exception:
        return []

def search_web(question):
    results = DDGS().text(question, max_results=3)

    for result in results:
        body = result.get("body")

        if body:
            return body

    return None

def answer_question(question):
    try:
        answer = search_web(question)

        if answer:
            return answer
        else:
            return "Sorry, I could not find an answer to that question."

    except Exception:
        return "Sorry, I could not search for that information right now."

def set_reminder(message, seconds):
    def reminder_task():
        time.sleep(seconds)
        speak("Reminder. " + message)

    thread = threading.Thread(target=reminder_task)
    thread.daemon = True
    thread.start()

def set_alarm(alarm_time):
    def alarm_task():
        while True:
            current_time = datetime.datetime.now().strftime("%I:%M %p")

            if current_time == alarm_time:
                speak("Alarm. It is " + alarm_time)

                for i in range(5):
                    winsound.Beep(1000, 1000)

                break
        time.sleep(1)
    thread = threading.Thread(target=alarm_task)
    thread.daemon = True
    thread.start()

def add_todo(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
def show_todo():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()

        return tasks

    except FileNotFoundError:
        return []

def remove_todo(task_to_remove):
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()

        new_tasks = []

        for task in tasks:
            if task.strip().lower() != task_to_remove.lower():
                new_tasks.append(task)

        with open("todo.txt", "w") as file:
            file.writelines(new_tasks)

        return len(tasks) != len(new_tasks)

    except FileNotFoundError:
        return False

speak("Assistant is ready. Say Max to activate me.")

while True:
    command = listen("")

    if "max" not in command:
        continue

    speak("Yes, how can I help you?")

    command = listen("Listening for command...")

    if command == "":
        continue

    if "exit" in command or "bye" in command:
        speak("Goodbye.")
        break

    elif "hello" in command:
        speak("Hello. How can I help you?")

    elif "how are you" in command:
        speak("I am working fine.")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    elif "who is" in command:
        person = command.replace("who is", "").strip()

        try:
            info = get_wikipedia_summary(person)

            if info:
                speak(info)
            else:
                speak("Sorry, I could not find information about that person.")

        except Exception:
            speak("Sorry, I could not connect to Wikipedia.")

    elif "what is the name of" in command:
        answer = answer_question(command)
        speak(answer)

    elif "weather in" in command:
        city = command.split("weather in", 1)[1].strip()

        if city:
            try:
                speak("Checking the weather in " + city)

                city_url = quote(city)
                url = f"https://wttr.in/{city_url}?format=j1"

                response = requests.get(url, timeout=10)

                if response.status_code == 200:
                    data = response.json()

                    current = data["current_condition"][0]

                    temperature = current["temp_C"]
                    condition = current["weatherDesc"][0]["value"]

                    speak(
                    "The temperature in "
                    + city
                    + " is "
                    + temperature
                    + " degrees Celsius with "
                    + condition
                )

                else:
                    speak("Sorry, I could not get the weather information.")

            except Exception:
                speak("Sorry, I could not check the weather right now.")

        else:
         speak("Please tell me the city name.")
        
    elif "what is" in command:
        topic = command.replace("what is", "").strip()

        try:
            info = get_wikipedia_summary(topic)

            if info:
                speak(info)
            else:
                speak("Sorry, I could not find information about that topic.")

        except Exception:
            speak("Sorry, I could not connect to Wikipedia.")

    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "play" in command:
        song = command.replace("play", "").strip()

        if song:
            try:
                speak("Playing " + song)
                pywhatkit.playonyt(song)

            except Exception:
                speak("Sorry, I could not open YouTube right now.")

        else:
            speak("Please tell me what you want to play.")

    elif "open calculator" in command:
        speak("Opening Calculator.")
        os.system("calc")

    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad")

    elif "open chrome" in command:
        speak("Opening Google Chrome.")

        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        if os.path.exists(chrome_path):
            os.startfile(chrome_path)
        else:
            speak("Google Chrome was not found on this computer.")

    elif "open vs code" in command or "open visual studio code" in command:
        speak("Opening Visual Studio Code.")
        os.system("code")

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open gmail" in command:
        speak("Opening Gmail.")
        webbrowser.open("https://mail.google.com")

    elif "open wikipedia" in command:
        speak("Opening Wikipedia.")
        webbrowser.open("https://www.wikipedia.org")

    elif "search google for" in command:
        query = command.replace("search google for", "").strip()

        if query:
            speak("Searching Google for " + query)

            search_url = "https://www.google.com/search?q=" + query
            webbrowser.open(search_url)

        else:
            speak("Please tell me what you want to search for.")

    elif "news" in command:
        speak("Getting the latest news.")

        headlines = get_news()

        if headlines:
            speak("Here are the top five headlines.")

            for headline in headlines:
                speak(headline)

        else:
            speak("Sorry, I could not get the news right now.")

    elif "exit" in command:
        speak("Goodbye.")
        break

    elif command == "":
        continue

    elif "remind me to" in command and "in" in command and "seconds" in command:
        try:
            reminder_part = command.replace("remind me to", "").strip()

            message, time_part = reminder_part.rsplit(" in ", 1)

            seconds = int(time_part.replace("seconds", "").strip())

            set_reminder(message, seconds)

            speak(
            "Okay. I will remind you to "
            + message
            + " in "
            + str(seconds)
            + " seconds."
        )

        except Exception:
            speak("Sorry, I could not set that reminder.")

    elif "remind me to" in command and "in" in command and "minutes" in command:
        try:
            reminder_part = command.replace("remind me to", "").strip()

            message, time_part = reminder_part.rsplit(" in ", 1)

            minutes = int(time_part.replace("minutes", "").strip())

            seconds = minutes * 60

            set_reminder(message, seconds)

            speak(
            "Okay. I will remind you to "
            + message
            + " in "
            + str(minutes)
            + " minutes."
        )

        except Exception:
            speak("Sorry, I could not set that reminder.")

    elif "set alarm for" in command:
        try:
            alarm_time = command.replace("set alarm for", "").strip()

            alarm_time = alarm_time.replace("a.m.", "AM")
            alarm_time = alarm_time.replace("p.m.", "PM")
            alarm_time = alarm_time.replace("am", "AM")
            alarm_time = alarm_time.replace("pm", "PM")

            alarm_time = datetime.datetime.strptime(
            alarm_time, "%I:%M %p"
            ).strftime("%I:%M %p")

            set_alarm(alarm_time)

            speak("Alarm set for " + alarm_time)

        except ValueError:
            speak("Sorry, I could not understand the alarm time.")

    elif "add" in command and "to my to do list" in command:
        task = command.replace("add", "").replace("to my to do list", "").strip()

        if task:
            add_todo(task)
            speak(task + " added to your to do list.")
        else:
            speak("Please tell me the task you want to add.")

    elif "show my to do list" in command:
        tasks = show_todo()

        if tasks:
            speak("Here are your tasks.")

            for task in tasks:
                speak(task.strip())

        else:
            speak("Your to do list is empty.")
    elif "remove" in command and "from my to do list" in command:
        task = command.replace("remove", "").replace(
            "from my to do list", ""
        ).strip()

        if task:
            removed = remove_todo(task)

            if removed:
                speak(task + " removed from your to do list.")
            else:
                speak("I could not find that task in your to do list.")

        else:
            speak("Please tell me which task you want to remove.")

    else:
        speak("Sorry, I do not know that command yet.")