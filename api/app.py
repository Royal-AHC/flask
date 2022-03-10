from flask import Flask, render_template, request, send_from_directory, after_this_request, Response, stream_with_context, make_response
import os
import sys

root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-2])
sys.path.append(root_path)

app = Flask(__name__, static_folder="../static",
            template_folder="../templates")

@app.route('/', methods=['GET'])
def home():
    return "Hello"


@app.route('/world', methods=['GET'])
def world():
    return "World"

@app.route('/chill', methods=['GET'])
def chill():
    return "Chill Mar Be Tu"

if __name__ == "__main__":
    app.run()
