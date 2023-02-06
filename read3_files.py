# counts.txt output file
# by Doris Flaiz

#Functions to count number
#of words and lines in file
#3 with a list and a function!

# def count_lines(filename):
#     total = 0
#     for line in open(filename):
#         total += 1
#     return filename + " : " + str(total)
#
# list = ["text1.txt", "text2.txt", "text3.txt"]
# out = open("counts2.txt", "w")
# for file in list:
#     print(count_lines(file),file=out)
# out.close()

#4. list is slightly simpler here
#   can also make a function, but need to return
#   a list/tuple with the number of lines and words

list = ["text1.txt", "text2.txt", "text3.txt"]
out = open("counts3.txt","w")
tot_lines = 0
tot_words = 0
for file in list:
    lines = 0
    words = 0
    for line in open(file):
        lines += 1
        words += len(line.split(" "))
    tot_lines += lines
    tot_words += words
    print(file, ':', lines, "lines", words, "words", file=out)

print("TOTAL:", tot_lines, "lines", tot_words, "words", file=out)
out.close()

