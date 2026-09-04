# MAX – Personal Voice Assistant

MAX is a desktop-based personal voice assistant developed using Python. It accepts voice commands, processes them, performs different tasks, and provides voice responses.

The project also includes a Flask-based web interface that allows the user to start and stop MAX from a web browser.

## Features

- Voice command recognition
- Text-to-speech responses
- Wake word activation using "MAX"
- Current time and date
- Wikipedia information
- Current weather information
- Latest news headlines
- Jokes
- YouTube music and video playback
- Google voice search
- Open websites such as Google, YouTube, Gmail, and Wikipedia
- Open desktop applications such as Calculator, Notepad, Chrome, and VS Code
- Set reminders
- Set alarms with sound
- Add tasks to a To-Do List
- View To-Do List tasks
- Remove tasks from the To-Do List
- Flask-based web interface
- Start and stop MAX through the web interface
- Basic microphone and error handling

## Technologies Used

- Python
- Flask
- SpeechRecognition
- pyttsx3
- PyAudio
- PyWhatKit
- Requests
- DDGS
- PyJokes
- HTML
- CSS
- JavaScript

## Project Structure

```text
PERSONAL_VOICE_ASSISTANT/
│
├── templates/
│   └── index.html
│
├── app.py
├── assistant.py
├── requirements.txt
├── README.md
├── .gitignore
└── todo.txt
```

## Installation

### 1. Clone or download the project

Download the project and open the project folder in VS Code.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

## Running MAX

Start the Flask application:

```bash
python app.py
```

The Flask server will run locally at:

```text
http://127.0.0.1:5000
```

Open this address in a web browser.

Click **Start Assistant** to start MAX.

The web interface will display whether MAX is running or stopped.

## Using MAX

After starting the assistant, say:

```text
MAX
```

MAX will respond:

```text
Yes, how can I help you?
```

Then give a voice command.

For every new command, say **MAX** first to activate the assistant.

### Example Commands

```text
MAX → What is the time?

MAX → What is the date?

MAX → Tell me a joke

MAX → Who is Sundar Pichai?

MAX → Weather in Hyderabad

MAX → Play Believer

MAX → Open YouTube

MAX → Open Calculator

MAX → Search Google for Python tutorials

MAX → Give me the latest news

MAX → Add complete project to my to do list

MAX → Show my to do list
```

## Stopping MAX

MAX can be stopped using the **Stop Assistant** button on the web interface.

The Flask server itself can be stopped from the terminal using:

```text
Ctrl + C
```

## Requirements

- Python 3
- Microphone
- Speaker or headphones
- Internet connection for online services such as speech recognition, weather, news, Wikipedia, Google Search, and YouTube

## Future Improvements

- More natural conversational responses
- Improved wake-word detection
- Graphical voice animations
- Additional desktop automation
- User customization
- More advanced AI-based question answering

## Conclusion

MAX demonstrates how Python can be used to build a voice-controlled personal assistant by combining speech recognition, text-to-speech, web services, desktop automation, task management, and a Flask-based web interface.