import requests
def recuperation(end):
    return requests.get('https://jsonplaceholder.typicode.com/'+end).json()



