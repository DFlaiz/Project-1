# counts.txt output file
# by Doris Flaiz

# Functions to count number
# of words and lines in each file
# write to a new file and pulling in 3 different files

def counter(name):
    # variable to store total word count
    num_words = 0
    # variable to store total line count
    num_lines = 0
    with open(fname, 'r') as f:
        #counting lines in the file
        for line in f:
            num_lines += 1
            #starting the word count
            word = 'Y'
            for letter in line:
                if (letter != ' ' and word == 'Y'):
                    num_words += 1
                    word = 'N'
                elif (letter == ' '):
                    word = 'Y'
        #add the total words for the file to a list
        listword.append(num_words)
        #add the total lines for the file to a list
        listline.append(num_lines)
        # writing line to the file
        print(fname, num_lines, "lines, ", num_words, "words", file=datafile)


if __name__ == '__main__':
    #create the output file
    datafile = open("counts.txt", "w")
    #list of input files
    list=['text1.txt','text2.txt','text3.txt']
    #lists to hold the output of the file counts
    listline = []
    listword = []
    try:
        #running a for loop on the list of files
        for fname in list:
            counter(fname)
    except:
        print('File not found')
    #print the totals line at the end
    print("Total lines: ", sum(listline), "Total words",sum(listword), file=datafile)
    datafile.close()