import subprocess
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
    subprocess.call("ffmpeg -stream_loop 1 -re -i $line -vcodec libx264 -b:v 300k -f flv rtmp://ovsu.mycdn.me/input/226554909_226554909_43_za3kj6gvoa", shell=True)
if __name__ == '__main__':
    app.run()
