user = {}

name  = input('enter your name: ' )
age = input('enter your age: ' )
fav_movies = input('your fav movies separated by comma ').split(',')
fav_songs = input('your fav song separated by comma ').split(',')

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs

for key in user.items():
    print(f"{key} : {value}")

