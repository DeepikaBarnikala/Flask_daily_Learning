from flask import Flask,render_template,url_for,request,redirect
import uuid
app=Flask(__name__)
#we will generate UUID using python module

@app.route('/')
def home():
  return redirect(url_for('indexPage'))  #in url we only give the endpoint/view function(ie func name)
  #return "u are almost there dont quit now...u can do this!!"
@app.route('/generate')
def generate():
  id=uuid.uuid4().hex
  print(id)
  return f'The generated id is:{id}'

@app.route('/index')
def indexPage():
  return render_template('index.html')

@app.route('/about')
def aboutPage():
  return render_template('about.html')

if __name__=='__main__':
  app.run(host='0.0.0.0', #local server
          port=5002,
          debug=True) #always recommanded in local not in production
