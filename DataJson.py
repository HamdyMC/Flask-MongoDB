# from models import Users, Posts, Todos, Albums
from fonctions import recuperation
# import motor.motor_asyncio
from datetime import datetime,date
import json 
import pymongo
from pymongo import MongoClient
import requests


# MONGO_DETAILS = "mongodb://localhost:27017"

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
client = MongoClient('mongodb://localhost:27017/')

database = client.Ecole221Nosql

UsersCollect = database.get_collection("users")

PostsCollect = database.get_collection("posts")

# CommentsCollect = database.get_collection("comments")

UsersList=recuperation('users')
PostsList=recuperation('posts')
# TodosList=recuperation('todos')
# AlbumsList=recuperation('albums')
# PhotosList=recuperation('photos')
# CommentsList=recuperation('comments')




def charger_donnees():


    for user in UsersList:
        id_user_api=user['id']
        user.pop('id')
        result = UsersCollect.insert_one(user)
        id_utilisateur = result.inserted_id


        PostUserList = requests.get(f'https://jsonplaceholder.typicode.com/posts?userId={id_user_api}').json()

        for post in PostUserList:
            post['id_user'] = id_utilisateur
            [post.pop(x, None) for x in ['id', 'userId']]
            PostsCollect.insert_one(post)

    return 'Utilisateurs chargés avec succès dans la base de données.'

print(charger_donnees())
