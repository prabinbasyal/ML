#building URL dynamically
# variable rule
# jinja2 template engine 
 


#jinja2 template engine
'''
{{ }} expression to print output in html
{%...%} conditions, for loops
{#...#} for single line comment
'''

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


@app.route('/submit',methods= ['GET','POST'])
def submit():
    if request.method =='POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

#variable rule
@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score > 50:
        res = "Passed"
    else:
        res = "Faled"
    return render_template('result.html', results = res)

#variable rule
@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score > 50:
        res = "Passed"
    else:
        res = "Failed"
    
    exp = {'score':score, 'res': res}
    return render_template('result.html', results = exp)


# Entry point of .py file is if __name__ == "__main__":
# In .py file first execture if __name__ == '__main__':
if __name__ == '__main__':
    app.run(debug=True)     # debug=True: help to restored serverand if we change any things it reload the update in web


