# Git Workshop
import os
import codecs

teilnehmer = []

# Import the first line of all text files inside this directory and assign it to a variable
for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        print(file)
        with codecs.open(file, 'r', encoding='utf-8',
                         errors='ignore') as fdata:
            first_line = fdata.readline()
            teilnehmer.append(first_line)

print(teilnehmer)

for name in teilnehmer:
    print(f'Hallo {name} und willkommen im Git Workshop!')
