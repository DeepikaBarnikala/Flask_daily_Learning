from flask import Flask
#create a Flask application instance
app=Flask(__name__)
#now we will start defining the routes
@app.route('/')
def home():
  """Default home page"""
  return "flask sounds interesting"
@app.route('/deepika')
def details():
  """details about deepika"""
  return "Deepika is a aspiring fullstack dev"
@app.route('/students')
def data():
  """details about students-->student info"""
  return "Students are from codegnan"
if __name__=='__main__':
  #if port is already in use chnage the port numberx
  app.run(host='0.0.0.0',
          port=5500,debug=True)

