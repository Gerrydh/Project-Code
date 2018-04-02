# Ger Hanlon, 02.04.2018
# This scripts returns the max and min Sepal Lenghts (Column 0)
# https://stackoverflow.com/questions/46281738

with open("Iris data2.csv") as file:
    lines = file.read().split("\n")     #Read lines

num_list = []
for line in lines:
    try:
        item = line.split(",")[1] #Choose 4th column and delete ""
        num_list.append(float(item))    #Try to parse 
    except:
        pass  #If it can't parse, the string is not a number

print("The smallest Sepal Length is : ", min(num_list)) #Prints the minimum value
print("The tallest Sepal Length is : ", max(num_list)) #Prints the maximum value
