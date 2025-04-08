from flask import Flask
import os
import datetime
import pytz
import subprocess
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Raghav"
    username = getpass.getuser()
    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = str(e)

    return f"""
    <h1>HTOP Info Page</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {time_now}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
