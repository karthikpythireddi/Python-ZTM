#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
from curses.ascii import SO


friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

friends.append('Stanley')

friends.sort()

print(friends)