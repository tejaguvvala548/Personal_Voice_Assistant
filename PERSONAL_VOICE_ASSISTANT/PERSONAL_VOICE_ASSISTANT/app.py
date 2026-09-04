from flask import Flask, render_template, jsonify
import subprocess
import sys
import os

app = Flask(__name__)

assistant_process = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start-assistant")
def start_assistant():
    global assistant_process

    if assistant_process is not None and assistant_process.poll() is None:
        return jsonify({
            "message": "MAX Voice Assistant is already running.",
            "running": True
        })

    assistant_process = subprocess.Popen(
        [sys.executable, "assistant.py"],
        cwd=os.path.dirname(os.path.abspath(__file__))
    )

    return jsonify({
        "message": "MAX Voice Assistant started.",
        "running": True
    })


@app.route("/stop-assistant")
def stop_assistant():
    global assistant_process

    if assistant_process is not None and assistant_process.poll() is None:

        pid = assistant_process.pid

        # Force-stop MAX and its child processes on Windows
        subprocess.run(
            ["taskkill", "/PID", str(pid), "/T", "/F"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        assistant_process = None

        return jsonify({
            "message": "MAX Voice Assistant stopped.",
            "running": False
        })

    assistant_process = None

    return jsonify({
        "message": "MAX Voice Assistant is not running.",
        "running": False
    })


@app.route("/status")
def status():
    global assistant_process

    running = (
        assistant_process is not None
        and assistant_process.poll() is None
    )

    return jsonify({
        "running": running
    })


if __name__ == "__main__":
    app.run(debug=False)