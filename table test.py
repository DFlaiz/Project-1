from tabulate import tabulate

# create data
data = [["Mavs", 99],
        ["Suns", 91],
        ["Spurs", 94],
        ["Nets", 88]]

# define header names
col_names = ["Team", "Points"]

# display table
print(tabulate(data, headers=col_names))
# display table - add frame around it
print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
#display table - add the index
print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex="always"))