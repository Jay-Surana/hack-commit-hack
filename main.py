import os

for i in range(1,365):
    d = str(i) + ' day ago'

    with open('bot.txt', 'a') as file:
        file.write(d)

    os.system('git add bot.txt')
    os.system('git commit -am "first commit"')

os.system('git push -u origin master')
