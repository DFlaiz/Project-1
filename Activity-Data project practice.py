# Data Projct Practice
# by Doris Flaiz

import statistics

def output_stats(list):  # calculate the mean, median and STD and adding lines between sections
    print("-"*20)
    print("mean:    ", round(statistics.mean(list), 2))
    print("median:  ", statistics.median(list))
    print("STD:     ", round(statistics.pstdev(list), 2))
    print("-" * 20)
    print()

def input_file(csv):
    file = open(csv)
    for line in file:
        list = line.rstrip().split(",")   # the rstrip will remove white space to the right
        # print(list)
        if list[1] == "Spring 2016":
            spring.append(eval(list[2]))
        else:
            fall.append(eval(list[2]))
    file.close()

spring = []  # initializing the two lists that are used
fall = []
input_file("sample_grades.csv")  #pulling in the csv file
print("Spring 2016")
output_stats(spring)
print("Fall 2016")
output_stats(fall)



