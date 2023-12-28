from flask import Flask
from threading import Thread

app = Flask(__name__)

rate_limit = 10
remaining_requests = rate_limit

@app.route('/')
def home():
    return '''
    <body>
    <center><h1>Bot 24H ON!</h1></center>
    </body>
    '''

def run_flask_app():
    app.run(host='0.0.0.0', port=5000, threaded=True)

if __name__ == '__main__':
    flask_thread = Thread(target=run_flask_app)
    flask_thread.start()

import requests
import time

payload = {
    'content': 'ÃÂ§ÃÂÃÂ ÃÂÃÂÃÂ ÃÂÃÂ¨ÃÂ¶ÃÂª ÃÂ´ÃÂ§ÃÂ±ÃÂ¨ ÃÂÃÂÃÂ§ÃÂ¨ÃÂ ÃÂ¹ÃÂ ÃÂ§ÃÂÃÂÃÂÃÂ§ÃÂ¯ÃÂ ÃÂ ÃÂÃÂÃÂ ÃÂ¯ÃÂ'
}

header = {
    'authorization': 'MTE2MDYwNDE1OTU5OTQ1NjQ1MA.G9fwys.bkAFtWGWBLUaIJYwvgEbT5mCB3BsX6o6uzEKj4'
}

for i in range(1000000):
    r = requests.post('https://discordapp.com/api/v9/channels/1163475276882251798/messages', data=payload, headers=header)
    
    time.sleep(5)