import shelve
shelv_file = shelve.open('mydata')
shelv_file['cats'] = ['Zophie', 'Malvo', 'Simon', 'Cleo']
shelv_file.close()

shelv_file = shelve.open('mydata')
print(shelv_file['cats'])
shelv_file.close()
