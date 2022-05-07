from urllib.parse import uses_netloc


user = {

    'basket' : {1,2,3},
    'greet' : 'hello',
    'age' : 20

}

user2 = user.copy()

print('basket' in user)


print('greet' in user.keys())

print({1,2,3} in user.values())

print(user.items())

print(user.clear())


print(user2)

#pops the key 'age' and returns the value
print(user2.pop('age'))


#pops the last key and value pair in the dictionary since Python 3.7 and before that it just pops any random item in the dictionary
print(user2.popitem())


#updates the "age" key with the assigned value
print(user.update({'age':55}))