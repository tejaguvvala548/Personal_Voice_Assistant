from flask import Flask, render_template, request, jsonify
from web_commands import process_command

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Receive command from browser
@app.route("/command", methods=["POST"])
def command():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "message": "No command received."
            })

        user_command = data.get("command", "").strip()

        if not user_command:
            return jsonify({
                "message": "Please say or enter a command."
            })

        # Send command to web_commands.py
        result = process_command(user_command)

        # Some commands return extra actions,
        # such as opening Google or YouTube
        if isinstance(result, dict):
            return jsonify(result)

        return jsonify({
            "message": result
        })

    except Exception as error:
        print("Command error:", error)

        return jsonify({
            "message": "Sorry, something went wrong while processing your command."
        }), 500


# Used to check whether the web server is working
@app.route("/status")
def status():
    return jsonify({
        "online": True,
        "message": "MAX web assistant is online."
    })


if __name__ == "__main__":
    app.run(debug=True)