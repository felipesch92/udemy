import re
phone_regex = re.compile(r'\d\d-\d\d\d\d\d-\d\d\d\d')
resume = 'My cell phone is 49-99199-9899 and my girlfriend number is 51-98175-0510'
print(phone_regex.findall(resume))
