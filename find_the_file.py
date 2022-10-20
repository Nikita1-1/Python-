
import os

path = '//Users//nikitasazonov//Documents//test'

file = open('files.rtf', 'w')

for x in os.listdir(path):
    file.write(x + '\n')

##
##for x in os.listdir(path):
##    if x.endswith('.rtf'):
##        print(x)
