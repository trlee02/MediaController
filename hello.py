#https://dev.to/sahilrajput/use-qr-code-to-transfer-files-from-laptop-to-mobile-28l7

#import cv2
import pyqrcode
import socket
from flask import Flask

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print("Your computer IP is: {0}".format(IP))

url = pyqrcode.create(f'http://{IP}:5000')
url.png("team.png", scale=8)
url.show()


app = Flask(__name__)
@app.route("/")

def index():
    print("This is a print")
    return "The Server is up and running, and is printing"


app.run(debug=True, host='0.0.0.0')