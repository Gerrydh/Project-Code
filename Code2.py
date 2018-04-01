data = []
with open('Iris.txt') as f:
    for line in f:                   # loop over the rows
        fields = line.split()        # parse the columns
        rowdata = fields # convert text to numbers
        data.extend(rowdata)         # accumulate the results
print('Minimum:', min(data[:12]))
print('Maximum:', max(data))
