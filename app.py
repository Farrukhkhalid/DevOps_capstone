import random
from flask import Flask
from flask import render_template

# generate new background color
R = random.randint(0, 255)
G = random.randint(0, 255)
B = random.randint(0, 255)

#create new background html
HELLO = """
    <html style="background-color:rgb({}, {}, {});">
    <head>
    <title>Flask Tutorial</title>
    </head>
    <body>
    <h1> Hello World v2!</h1>
    </body>
    </html>  
""".format(R, G, B)

print(HELLO)

INDEX = open('index.html', 'w')
INDEX.write(HELLO)
INDEX.close()

APP = Flask(__name__)

@APP.route('/')
def index():
    return render_template('index.html')
APP.run(host='0.0.0.0', port=80)