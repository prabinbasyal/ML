# Flask App Skeleton
# Requirenment : ipkernel , numpy, pandas, matplotlib, seaborn, flask

from flask import Flask
# initializing flask app (WSGI(Web server gateway configuration) Application)
'''
it create flask class which will be WSGI application
'''
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to this Flask course"

@app.route('/index')
def index():
    return "welcome to the index page"

# Entry point of .py file is if __name__ == "__main__":
# In .py file first execture if __name__ == '__main__':
if __name__ == '__main__':
    app.run(debug=True)     # debug=True: help to restored serverand if we change any things it reload the update in web


