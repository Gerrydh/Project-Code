https://stackoverflow.com/questions/46281738

with open("Realtime_Sep-2017.csv") as file:
    lines = file.read().split("\n")     #Read lines

num_list = []
for line in lines:
    try:
        item = line.split(",")[4][1:-1] #Choose 4th column and delete ""
        num_list.append(float(item))    #Try to parse 
    except:
        pass                            #If it can't parse, the string is not a number

print(max(num_list))                    #Prints maximum value
print(min(num_list))                    #Prints minimum value
