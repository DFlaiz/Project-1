# ok so lets learn how to read files...
# by Doris Flaiz
# Case study: Word Play

fin = open('read_file.txt')
fin.read()
for line in fin:
    print("-",line.strip())

