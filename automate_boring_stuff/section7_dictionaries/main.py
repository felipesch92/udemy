mycat = {'color': 'gray',
         'size': 'fat',
         'disposition': 'loud'}

if 'age' not in mycat:
    mycat['age'] = '3'

print(list(mycat.items()))
