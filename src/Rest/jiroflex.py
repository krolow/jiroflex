from config import CONFIG
from flask import Flask, jsonify
from jira import jira

app = Flask(__name__)
client = jira.Jira(CONFIG['url'], CONFIG['username'], CONFIG['password'])

app.debug = True

@app.route("/progress/<username>")
def progress(username):
    return jsonify(progress=client.has_task_in_progress(username))

if __name__ == "__main__":
    app.run()