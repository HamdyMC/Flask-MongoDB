from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from fonctions import recuperation
from datetime import datetime,date
import json 
import pymongo
from wtforms import Form, StringField, TextAreaField, validators, SubmitField, PasswordField, BooleanField, SelectField, IntegerField, FloatField, DateField
from wtforms.validators import DataRequired 
import requests
from bson.objectid import ObjectId

def recuperation(end):
    return requests.get('https://jsonplaceholder.typicode.com/'+end).json()

class UserForm(Form):
    name = StringField('name', [validators.Length(min=1, max=50)],render_kw={"class":"form-control"})
    username = StringField('username', [validators.Length(min=4, max=25)],render_kw={"class":"form-control"})
    email = StringField('email', [validators.Length(min=6, max=50)],render_kw={"class":"form-control"})
    phone = StringField('phone', [validators.Length(min=7, max=14)],render_kw={"class":"form-control"})
    website = StringField('website', [validators.Length(min=4, max=50)],render_kw={"class":"form-control"})
    street = StringField('street', [validators.Length(min=4, max=50)],render_kw={"class":"form-control"})
    suite = StringField('suite', [validators.Length(min=4, max=50)],render_kw={"class":"form-control"})
    city = StringField('city', [validators.Length(min=4, max=50)],render_kw={"class":"form-control"})
    zipcode = StringField('zipcode', [validators.Length(min=4, max=50)],render_kw={"class":"form-control"})
    lng = StringField('lng', [validators.Length(min=4, max=50)],render_kw={"class":"form-control"})
    lat = StringField('lat', [validators.Length(min=4, max=50)],render_kw={"class":"form-control"})
    name_company=StringField('name_company',render_kw={"class":"form-control"})
    catchPrase=StringField('catchPrase',render_kw={"class":"form-control"})
    bs=StringField('bs',render_kw={"class":"form-control"})





client = MongoClient("mongodb://localhost:27017")


database = client.Ecole221Nosql

UsersCollect = database.get_collection("users")

PostsCollect = database.get_collection("posts")

CommentsCollect = database.get_collection("comments")
client = MongoClient('localhost', 27017)
db = client.Ecole221Nosql

app = Flask(__name__)
app.config['SECRET_KEY'] = "heyhey"



@app.route('/')
def index():
    Form=UserForm()

    Liste_users = list(db.users.find())
    # print(Liste_users)
    # Liste_users=recuperation('users')
    return render_template('index.html',ListeHt=Liste_users,form=Form)

@app.route('/ajout_user', methods=['POST', 'GET'])
def ajout_user():
    Form=UserForm()
    if request.method == 'POST':
    
        user = {
            'name': request.form.get('name'),
            'username': request.form.get('username'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'website': request.form.get('website'),
            "Address":{
                'street': request.form.get('street'),
                'suite': request.form.get('suite'),
                'city': request.form.get('city'),
                'zipcode': request.form.get('zipcode'),
                "geo":{
                    'lng': request.form.get('lng'),
                    'lat': request.form.get('lat')
                    }
                },
            'name_company': request.form.get('name_company'),
            'catchPrase': request.form.get('catchPrase'),
            'bs': request.form.get('bs')
        }
        db.users.insert_one(user)
        return redirect('/')
        return redirect(url_for('index'),message="Insertion réussie")
    return render_template('ajouter_user.html', form=Form)

@app.route('/posts/<id_user>', methods=['GET'])
def user_posts(id_user):
    posts = list(db.posts.find({'id_user': ObjectId(id_user)}))
    print(len(posts))
    return render_template('posts.html', posts=posts)


@app.route('/delete_user/<id_user>', methods=['GET'])
def delete_user(id_user):
    print('supreesion')
    # result= UsersCollect.find_one()

    user={'_id': ObjectId(id_user)}
    # ObjectId(_id)
    result=UsersCollect.delete_one(user)
    if result.deleted_count == 1:
        print('Utilisateur supprimé avec succès.')
    else:
        print('L\'utilisateur spécifié n\'a pas été trouvé.')
    Form=UserForm()

    Liste_users = list(db.users.find())
    # print(Liste_users)
    # Liste_users=recuperation('users')
    return render_template('index.html',ListeHt=Liste_users,form=Form)
if __name__ == '__main__':
    app.run(debug=True)