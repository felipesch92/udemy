import re

bat_regex = re.compile(r'Bat(wo)*man')
mo = bat_regex.search('The Adventures of Batwowowoman')
print(mo.group())

bat_regex = re.compile(r'Bat(wo)+man')
mo = bat_regex.search('The adventures of Batwowoman')
print(mo.group())
