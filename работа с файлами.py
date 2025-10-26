file = open("data/text.txt", 'a')

file.write('Hello\n')
file.write('!!!')

file.close()



file = open("data/text.txt", 'r')

# print(file.read())

for line in file:
    print(line, end="")

file.close