# Reading and writing files
# by Doris Flaiz

# datafile = open("add1.txt", "r")
# for line in datafile:
#     print(line.rstrip())
# datafile.close

# PROMPT = "Ente the next line in the file: "
# writefile = input("What is the name of your file? ")
# numlines = eval(input("How many lines do you want to write? "))

# dataFile = open(writefile, "w")
#
# for x in range(numlines):
#     userinput = input(PROMPT)
#     # write the users's input to the file
#     print(userinput, file=dataFile)

#dataFile.close()

# datafile = open("read_file.txt", "r")
# outputfile = open("out_file.txt","w")
#
# for line in datafile:
#     print("-"+line.rstrip(), file=outputfile)
#
# datafile.close
# outputfile.close


PROMPT = "Enter the next line in the file: "
writefile = input("What is the name of your file? ")
#numlines = eval(input("How many lines do you want to write? "))
userinput =1

dataFile = open(writefile, "w")

while userinput != 0:
    userinput = eval(input(PROMPT))
    # write the users's input to the file
    if userinput == 0:
        break
    else:
        print(userinput, file=dataFile)
dataFile.close()