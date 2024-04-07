import pandas as pd
import google.generativeai as genai
from flask import Flask, render_template, url_for, request, redirect,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz



# pd.read_csv('data.csv')

GOOGLE_API_KEY="AIzaSyDjzoVQZvqPHgv9mD9dyRXUcQoMXQ1yAmo"

genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "temperature": 1.0,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_NONE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_NONE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_NONE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_NONE"
    },
]
model=genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config,safety_settings=safety_settings)
chat=model.start_chat(history=[])
# print((chat.send_message("hello")).text)
data=pd.read_csv('data.csv')
def responce(item):
      for i in data.iloc[:,0]:
          if i==item:
              break
      # return("hello")
      return((chat.send_message(f" {item} has {data.iloc[i,1]}as which warehuse its stored in  ,{data.iloc[i,4]} as custumer rating out of 5,{data.iloc[i,5]} as cost per product, {data.iloc[i,7]} as importance of product, {data.iloc[i,9]} as discount on porduct,,  {data.iloc[i,5]} as weight in grams add extra detail condencing it to 50 words report and report is necessery no matter the circumstance make responce neet whithout special characters")).text)




app = Flask(__name__)
app.secret_key='password'
'''most secure password'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=(datetime.utcnow))

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            searchitem=int(task_content)
            chatresponce=("%r" % responce(searchitem))
            
            db.session.add(new_task)
            db.session.commit()
            flash(chatresponce)
            return (redirect('/'))
        except:
            return 'There was an issue adding your input'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            
            searchitem=int(task.content)
            chatresponce=("%r" % responce(searchitem))
            
            flash(chatresponce)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)
