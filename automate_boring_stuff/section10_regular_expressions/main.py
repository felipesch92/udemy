import re

message = 'Call me on 49-99199-9899 if u can'
phone_num_regex = re.compile(r'\d\d-\d\d\d\d\d-\d\d\d\d')
mo = phone_num_regex.search(message)
print(mo.group())
