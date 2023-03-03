# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template,request, redirect, url_for
from pymongo import MongoClient



app = Flask(__name__)
client = MongoClient("mongodb+srv://arsal0344:03444800061@cluster0.u6h8hwf.mongodb.net/?retryWrites=true&w=majority")
db = client.mentoria
collection = db.users
try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print("Unable to connect to MongoDB:", e)



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')



fulldata=[]
@app.route('/submitData',methods=['post'])
def submitData():
    data = request.get_json()
    fulldata.append(data)
    print('full: '+fulldata[0]['name'])
# result = collection.insert_one({'name': data['name'],'email':data['email'],'phone':data['phone']})
    return render_template('quiz.html',modal=True)

@app.route('/mcqs')
def mcqs():
    return render_template('mcqs.html')

@app.route('/mcqsData',methods=['post'])
def mcqsData():
    data = request.get_json()
    data.append(fulldata[-1])
    answers = data[:-1]
    result = collection.insert_one({'answers':answers,'info':data[-1]})
    return 'done'

@app.route('/end')
def end():
    return render_template('end.html')

@app.route('/admin4321')
def admin():
    answers = []
    info = []
    data = list(collection.find())
    for i in range(len(data)):

          
        answers.append(data[i]['answers'])
        info.append(data[i]['info'])
     
    
          
    return render_template('admin.html',data=info)


if __name__ == '__main__':
	app.run(debug=True)
