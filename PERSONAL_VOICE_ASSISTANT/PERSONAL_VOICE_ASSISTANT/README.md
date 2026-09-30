# MAX – Personal Voice Assistant

MAX is a desktop and web-based personal voice assistant developed using Python, Flask, HTML, CSS, and JavaScript.

The desktop version uses voice commands to perform everyday tasks such as searching for information, checking weather and news, playing YouTube videos, opening desktop applications and websites, setting reminders and alarms, managing a To-Do List, and providing voice responses.

The web version allows users to interact with MAX directly through a web browser using voice commands. It uses a Flask backend for command processing and browser-based speech recognition and speech synthesis for voice interaction.

The web version is deployed online using Vercel.

## Live Demo

Try the web version of MAX:

https://personal-voice-assistant-orcin.vercel.app

## Features

### Desktop Assistant

- Voice command recognition
- Wake-word activation using "MAX"
- Text-to-speech responses
- Current time and date
- Wikipedia information search
- Current weather information
- Latest news headlines
- Jokes
- YouTube music and video playback
- Google search
- Open websites such as Google, YouTube, Gmail, and Wikipedia
- Open desktop applications such as Calculator, Notepad, Chrome, and VS Code
- Set reminders in seconds or minutes
- Set alarms with sound
- Cancel active alarms
- Add tasks to a To-Do List
- View To-Do List tasks
- Remove tasks from the To-Do List
- Help command using "What can you do?"
- Basic error handling

### Web Assistant

- Browser-based voice recognition
- Browser-based text-to-speech responses
- Current local time with AM/PM
- Current date
- Wikipedia information search
- Weather information
- Latest news
- Jokes
- Google search
- YouTube search and playback
- Open Google, YouTube, and Wikipedia
- Continuous voice interaction
- Start and stop assistant controls
- Flask backend for command processing
- Online deployment using Vercel

## Technologies Used

### Backend

- Python
- Flask

### Voice Processing

- SpeechRecognition
- PyAudio
- pyttsx3
- Web Speech API (Web Version)

### Libraries and Services

- Requests
- PyWhatKit
- PyJokes
- DDGS
- Wikipedia API
- Google News RSS
- wttr.in Weather Service

### Frontend

- HTML
- CSS
- JavaScript

### Deployment

- GitHub
- Vercel

## Project Structure

```text
PERSONAL_VOICE_ASSISTANT/
│
├── templates/
│   └── index.html
│
├── app.py
├── assistant.py
├── web_commands.py
├── requirements.txt
├── requirements-desktop.txt
├── vercel.json
├── README.md
├── .gitignore
└── todo.txt
```

### Main Files

- `assistant.py` - Runs the desktop version of MAX.
- `app.py` - Flask application for the web version.
- `web_commands.py` - Processes commands for the web assistant.
- `templates/index.html` - Contains the web interface and browser voice interaction.
- `requirements.txt` - Contains dependencies required for the deployed web version.
- `requirements-desktop.txt` - Contains dependencies required for the desktop version.
- `vercel.json` - Contains the Vercel deployment configuration.
- `todo.txt` - Stores To-Do List tasks locally.

## Installation

### 1. Clone or Download the Project

Clone the GitHub repository or download the project files and open the project folder in VS Code.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the virtual environment again.

### 4. Install Desktop Dependencies

To run the desktop version of MAX:

```bash
pip install -r requirements-desktop.txt
```

### 5. Run the Desktop Assistant

```bash
python assistant.py
```

MAX will start and wait for the wake word:

```text
Assistant is ready. Say Max to activate me.
```

### 6. Run the Web Version Locally

Install the web dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python app.py
```

Open the local Flask address shown in the terminal in your browser.

## Running and Using MAX

### Desktop Version

Start the desktop assistant:

```bash
python assistant.py
```

MAX will display:

```text
Assistant is ready. Say Max to activate me.
```

Say:

```text
Hello Max
```

MAX will respond:

```text
Yes, how can I help you?
```

Then give a command such as:

```text
What is the time?
Weather in Hyderabad
Play Believer
Set alarm for 10:30 AM
Cancel alarm
What can you do?
```

Say "Max" again whenever you want to activate the assistant for another command.

To stop the desktop assistant, say:

```text
Exit
```

or:

```text
Bye
```

### Web Version

Start the Flask application locally:

```bash
python app.py
```

Open the local Flask address shown in the terminal in a supported browser.

Click **Start Assistant** and allow microphone permission when requested.

You can then use commands such as:

```text
What is the time?
What is the date?
What is artificial intelligence?
Who is Sundar Pichai?
Weather in Hyderabad
Tell me a joke
Search Google for Python tutorial
Play Believer
Open Google
Open YouTube
Open Wikipedia
News
```

The web assistant automatically continues listening after processing a command.

Click **Stop Assistant** when you want to stop browser voice interaction.

The Flask development server can be stopped from the terminal using:

```text
Ctrl + C
```

## Example Desktop Commands

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

MAX → Set alarm for 10:30 AM

MAX → Cancel alarm

MAX → What can you do?
```

## Requirements

### Desktop Version

- Python 3
- Windows operating system
- Microphone
- Speaker or headphones
- Internet connection
- Required Python packages from `requirements-desktop.txt`

An internet connection is required for features such as speech recognition, Wikipedia, weather, news, Google Search, and YouTube.

### Web Version

- Modern web browser with microphone support
- Microphone permission
- Internet connection
- Required Python packages from `requirements.txt`

## Future Improvements

- Improved wake-word detection
- More natural conversational responses
- Support for additional reminder time formats
- Multiple alarm management
- Improved graphical voice animations
- More desktop automation commands
- User customization and preferences
- Advanced AI-based question answering

## Conclusion

MAX is a desktop and web-based personal voice assistant that demonstrates the integration of voice recognition, text-to-speech, web services, desktop automation, reminders, alarms, task management, and browser-based voice interaction.

The project provides practical experience with Python, Flask, APIs, frontend technologies, multithreading, deployment, and voice-based human-computer interaction.
