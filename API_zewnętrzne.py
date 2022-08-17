import requests

#https://www.youtube.com/watch?v=Pa23kKiGHH8

#nadanie zmiennej wartości z linka
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if  (response.status_code != requests.codes.ok): #sprawdzenie czy wszystko jest ok
    print('coś poszło nie tak')
else:
    print(response.json()) #wyświetla jeśli jest ok

#dodawanie przy wykorzystaniu post
requestBody = {
    'title' : 'Nasz tytuł',
    'body' : 'Treść posta',
    'userId' : 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=requestBody)
if  (response.status_code != requests.codes.created): #jeśli nie doda/created requestBody to wywala błąd
    print('coś poszło nie tak')
else:
    print(response.json())