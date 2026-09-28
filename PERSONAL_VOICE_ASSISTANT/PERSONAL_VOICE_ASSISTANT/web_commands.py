import datetime
import requests
import pyjokes
from urllib.parse import quote
import xml.etree.ElementTree as ET


# ---------------- WIKIPEDIA ----------------

def get_wikipedia_summary(topic):
    try:
        search_url = "https://en.wikipedia.org/w/api.php"

        headers = {
            "User-Agent": "MAX-PersonalVoiceAssistant/1.0"
        }

        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": topic,
            "format": "json"
        }

        response = requests.get(
            search_url,
            headers=headers,
            params=search_params,
            timeout=10
        )

        if response.status_code != 200:
            return None

        results = response.json()["query"]["search"]

        if not results:
            return None

        title = results[0]["title"]

        summary_url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + title.replace(" ", "_")
        )

        response = requests.get(
            summary_url,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            return response.json().get("extract")

        return None

    except Exception:
        return None


# ---------------- WEATHER ----------------

def get_weather(city):
    try:
        city_url = quote(city)

        url = f"https://wttr.in/{city_url}?format=j1"

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return "Sorry, I could not get the weather information."

        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_C"]
        condition = current["weatherDesc"][0]["value"]

        return (
            f"The temperature in {city} is "
            f"{temperature} degrees Celsius with {condition}."
        )

    except Exception:
        return "Sorry, I could not check the weather right now."


# ---------------- NEWS ----------------

def get_news():
    try:
        url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return "Sorry, I could not get the news right now."

        root = ET.fromstring(response.content)

        items = root.findall(".//item")

        headlines = []

        for item in items[:5]:
            title = item.find("title")

            if title is not None:
                headlines.append(title.text)

        if not headlines:
            return "Sorry, I could not find any news."

        return "Here are the top headlines. " + ". ".join(headlines)

    except Exception:
        return "Sorry, I could not get the news right now."


# ---------------- COMMAND PROCESSOR ----------------

def process_command(command):

    command = command.lower().strip()

    if "hello" in command:
        return "Hello. How can I help you?"

    elif "how are you" in command:
        return "I am working fine."

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return "The current time is " + current_time

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        return "Today's date is " + current_date

    elif "weather in" in command:
        city = command.split("weather in", 1)[1].strip()

        if city:
            return get_weather(city)

        return "Please tell me the city name."

    elif "play" in command:
        song = command.replace("play", "").strip()

        if song:
            return {
                "message": "Playing " + song,
                "action": "open_url",
                "url": "https://www.youtube.com/results?search_query=" + quote(song)
        }

        return "Please tell me what you want to play."

    elif "who is" in command:
        person = command.replace("who is", "").strip()

        info = get_wikipedia_summary(person)

        if info:
            return info

        return "Sorry, I could not find information about that person."

    elif "what is" in command:
        topic = command.replace("what is", "").strip()

        info = get_wikipedia_summary(topic)

        if info:
            return info

        return "Sorry, I could not find information about that topic."

    elif "joke" in command:
        return pyjokes.get_joke()

    elif "news" in command:
        return get_news()

    elif "open google" in command:
        return {
            "message": "Opening Google.",
            "action": "open_url",
            "url": "https://www.google.com"
        }

    elif "open youtube" in command:
        return {
            "message": "Opening YouTube.",
            "action": "open_url",
            "url": "https://www.youtube.com"
        }

    elif "open wikipedia" in command:
        return {
            "message": "Opening Wikipedia.",
            "action": "open_url",
            "url": "https://www.wikipedia.org"
        }

    elif "search google for" in command:
        query = command.replace("search google for", "").strip()

        if query:
            return {
                "message": "Searching Google for " + query,
                "action": "open_url",
                "url": "https://www.google.com/search?q=" + quote(query)
            }

        return "Please tell me what you want to search for."

    return "Sorry, I do not know that command yet."