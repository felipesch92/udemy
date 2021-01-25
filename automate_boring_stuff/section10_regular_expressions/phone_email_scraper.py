# Escavador de telefone e e-mail
import re

# Create a regex for phone numbers
phone_regex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
    
    ((\d\d\d)|((\\d\d\d)))? # area code (optional)
    (\s|-) # first separator
    \d\d\d  # first 3 digits
    # separator
    \d\d\d\d # last 4 digits
    ((ext(\.)?\s)|x) # extension word-part (optional)
    (\d(2,5))? # extension number-part (optional)
''', re.VERBOSE)


# Create a regex for email addresses
email_regex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

 [a-zA-Z0-9_.+]+ # name part
 @               # @ symbol
 [a-zA-Z0-9_.+]+ # domain name part

''', re.VERBOSE)

text = '051-999-9832 felipe@sicoobsmo.com.br tamara@vivo.com.br 932-983-3289'

phone = phone_regex.findall(text)
email = email_regex.findall(text)

print(phone, email)
# TODO = Get the text off the clipboard

# TODO: Extract the email/phone from this text

# TODO: Copy the extracted email/phone to the clipboard

