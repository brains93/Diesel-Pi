from flask import Flask, render_template
from flask_cors import CORS
import logging
import socket

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def get_ip_address():
    #gets the IP address of the pi, this is to pass to the html page so API calls can be made without worrying about dynamic IPS
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # connect() for UDP doesn't send packets
    s.connect(('8.8.8.8', 80))  
    logging.info(s.getsockname()[0])
    return s.getsockname()[0]


@app.route('/')
def home():
    ip = get_ip_address()
    return render_template('index.html', server_ip=ip)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')