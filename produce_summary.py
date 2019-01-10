
files ="um-deliveries-20140519.txt","um-deliveries-20140520.txt","um-deliveries-20140521.txt"
#creating a tuple to store the logs with the indices as keys 


# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]
#     #corrected the variables so that the splits are correct
#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
#     print()
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
#     print()
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
#     print()
# the_file.close()
def print_delivery_log(files):
    for i,file_name in enumerate(files):
        #looping through the text files in the tuple
        print("Day "+ str(i+1))
        #getting the day by adding 1 to the key associated with the value in the tuple
        the_file=open(file_name)
        #opening the file
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')
            #stripping the data to make it easy to move and read

            melon = words[0]
            count = words[1]
            amount = words[2]
            #assigning the order with which the values should be passed based on their indices

            print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
            print()
            #added an extra print statement to make the data easier to read
        the_file.close()

print_delivery_log(files)        

