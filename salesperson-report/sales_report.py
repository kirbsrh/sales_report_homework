"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""
#create empty lists to store names of sales people and melons sold
salespeople = []
melons_sold = []

#opens sales report file
f = open("sales-report.txt")
#using a for loop to iterate over each line of the text file
for line in f:
    #cleans up each line of the file by removing white space
    line = line.rstrip()
    #uses the pipe to split the lines and create a list for each line, entries
    entries = line.split("|")
    #creating variables for index 0, sales person and index 2, melons as integer
    salesperson = entries[0]
    melons = int(entries[2])

    #this conditional checks to see if a name is already in the list
    if salesperson in salespeople:
    #if the person is in the list then this assigns index of that name to position
        position = salespeople.index(salesperson)
    #this checks melons at the position in the list and adds to it
        melons_sold[position] += melons
    else:
    #if person is not in the list they are added to the list
        salespeople.append(salesperson)
    #if person is not in the list, their melons are added to the melon list
        melons_sold.append(melons)

#using a for loop to iterate over all of the salespeople
for i in range(len(salespeople)):
#printing name and number of melons sold in a formatted string
#identifying names and melons by indices from parallel lists
    print("{} sold {} melons".format(salespeople[i], melons_sold[i]))
