# Flask App Skeleton
# Requirenment : ipkernel , numpy, pandas, matplotlib, seaborn, flask

from flask import Flask, render_template,request
# initializing flask app (WSGI(Web server gateway configuration) Application)
'''
it create flask class which will be WSGI application
'''
app = Flask(__name__)

@app.route('/')
def home():
    return "<html><H1>Welcome to this Flask course</H1></html>"

@app.route('/index',methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods= ['GET','POST'])
def form():
    if request.method =='POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

@app.route('/submit',methods= ['GET','POST'])
def submit():
    if request.method =='POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

# Entry point of .py file is if __name__ == "__main__":
# In .py file first execture if __name__ == '__main__':
if __name__ == '__main__':
    app.run(debug=True)     # debug=True: help to restored serverand if we change any things it reload the update in web


