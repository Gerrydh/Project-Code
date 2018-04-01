f = open('Iris.txt, 'r')
 
data = f.readlines()
data = data[0:]
f.close()
print(max(data), min(data))
