from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
  return f'welcome to day3 today we are learning about static vs dynamicroutes'
@app.route('/profile/')
def details():
  return f'hello im deepika'

#static routing-->/name/deepika
#dynamic routing-->/name/<name>
@app.route('/name/deepu')
def data():
  return f'welcome deepika...' #static route

@app.route('/name/<name>') #dynamic route
def student_name(name):
  return f'hello {name}'

#now we want to create related to course names
@app.route('/courses/<course_name>')
def courses(course_name):
  return f'This Course is:<b>{course_name}</b>'

#multiple routes to one view function
@app.route('/')
@app.route('/home/')
def sample():
  return f'daddy is home...'

#converters-->int,str,float,path,uuid
#integer converter
@app.route('/students/<int:student_id>')
def studentid(student_id):
  return f'The ID of the Student is {student_id}'

#float converter
@app.route('/price/<float:item_price>')
def itemPrice(item_price):
  return f'The price of the item is {item_price}'

#str converter
@app.route('/path/<path:name>')
def Name(name):
  return f'name of the student is {name}'

#UUID --> universal unique identifiers
@app.route('/student_id/<uuid:stu_id>')
def student_id(stu_id):
  return f'the search for the student is {stu_id}'

if __name__=="__main__":
  app.run(host='0.0.0.0',
            port=5001,debug=True)