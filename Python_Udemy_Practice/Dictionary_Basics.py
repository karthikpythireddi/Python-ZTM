#Dictionary - Unordered key value pairs, each key value pairs are scattered allover the memory

dictionary = {

'a': [1,2,3],
'b': 'hello',
'x': True
}

my_list = [
    {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
    },

    {
    'a': [4,5,6],
    'b': 'hello',
    'x': False
    }
]

print(my_list[1]['b'])