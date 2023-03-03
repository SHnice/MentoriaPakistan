# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template,request, redirect, url_for,session
from pymongo import MongoClient



app = Flask(__name__)
client = MongoClient("mongodb+srv://arsal0344:03444800061@cluster0.u6h8hwf.mongodb.net/?retryWrites=true&w=majority")
db = client.mentoria
collection = db.users
app.secret_key = 'admin4321'
try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print("Unable to connnect to MongoDB:", e)



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')



# fulldata=[]
@app.route('/submitData',methods=['post'])
def submitData():
    data = request.get_json()
    # fulldata.append(data)
    session['key'] = data
# result = collection.insert_one({'name': data['name'],'email':data['email'],'phone':data['phone']})
    return render_template('quiz.html',modal=True)

@app.route('/mcqs')
def mcqs():
    return render_template('mcqs.html')

@app.route('/mcqsData',methods=['post'])
def mcqsData():
    data = request.get_json()
    data.append(session.get('key'))
    answers = data[:-1]
    result = collection.insert_one({'answers':answers,'info':data[-1]})
    return 'done'

@app.route('/end')
def end():
    return render_template('end.html')

@app.route('/admin4321')
def admin():
    solution = ['option2','option2','option3','option1','option3','option3','option3','option2','option4','option3',
               'option3','option4','option4','option2','option2','option3','option2','option3','option4','option3',
               'option3','option4','option1','option2','option2','option3','option4','option3','option3','option4',
               'option2','option2','option3','option2','option4','option3','option2','option4','option3','option1']
    last = []
    data = list(collection.find())

    quantitative = iq = physics = chemistry = 0
    for i in range(len(data)):
        info = data[i]['info']
        info['answers'] = []
        for j in range(40):
            if data[i]['answers'][j]['value'] == solution[j]:
                info['answers'].append(True)
                if j<10 : quantitative = quantitative+1
                elif j<20: iq = iq+1
                elif j<30: physics = physics+1
                else: chemistry = chemistry+1
            else:
                info['answers'].append(False)
        
        info["quantitative"] = quantitative
        info["iq"] = iq
        info["physics"] = physics
        info["chemistry"] = chemistry
        info["total"] = quantitative+iq+physics+chemistry
        last.append(info)
        quantitative = iq = physics = chemistry = 0
    print(last)
    return render_template('admin.html',data=last)


if __name__ == '__main__':
	app.run(debug=True)
