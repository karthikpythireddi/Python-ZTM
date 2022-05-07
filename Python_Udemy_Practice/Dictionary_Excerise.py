#Scroll down to see the answers!
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

karthik = {
    'age' : 28,
    'username' : 'karthikpythireddi',
    'weapons' : ['no weapon'],
    'is_active' : 'yes',
    'clan' : 'Human Clan',

}


#2 iterate and print all the keys in the above user.
print(karthik.items())


#3 Add a new weapon to your user
karthik['weapons'].append('peace')

print(karthik.items())

#4 Add a new key to include 'is_banned'. Set it to false
karthik.update({'is_banned' : 'false'})


#5 Ban the user by setting the previous key to True
karthik.update({'is_banned' : 'true'})

#6 create a new user2 my copying the previous user and update the age value and username value. 
shravani = karthik.copy()

shravani.update({'age': 26, 'username':'shravanibalaraju'})


print(karthik.items())

print(shravani.items())