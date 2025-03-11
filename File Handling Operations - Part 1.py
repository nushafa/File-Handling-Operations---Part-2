#write in line using with() function
with open('Codingal.txt', 'w') as file:
    file.write('Hi! I am a Codingal student.')
file.close()

#split the file into words
with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print('Words in this file are...')
    for line in data:
       words = line.split()
       print (words)
file.close()   