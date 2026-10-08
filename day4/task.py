from flask import Flask
import uuid
app=Flask(__name__)
#we will generate UUID using python module
#Build a student routing app
#student default page
#student id
#course
#student attendance
#file path
#student uuid

@app.route('/')
def home():
  return f'Welcome to the Student page'

#student name
@app.route('/name/<name>') #dynamic route
def student_name(name):
  return f'hello {name}'

#student id
@app.route('/students/<int:student_id>')
def studentid(student_id):
  return f'The ID of the Student is {student_id}'

#now we want to create related to course names
@app.route('/courses/<course_name>')
def courses(course_name):
  return f'This Course is:<b>{course_name}</b>'

@app.route('/skills/<s1>/<s2>')
def skills(s1,s2):
  return f'Student has {s1} and {s2} skills'

#student attendance
@app.route('/attendance/<float:attendance_per>')
def itemPrice(attendance_per):
  return f'The attendance is {attendance_per}'

#file path
#str converter
@app.route('/path/<path:name>')
def Name(name):
  return f'name of the student is {name}'

#UUID --> universal unique identifiers
@app.route('/search_student/')
def generate():
  id=uuid.uuid4().hex
  print(id)
  return f'The student id is:{id}'

if __name__=="__main__":
  app.run(host='0.0.0.0',
            port=5001,debug=True)