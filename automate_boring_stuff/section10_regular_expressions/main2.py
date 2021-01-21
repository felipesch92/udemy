import re

bat_regex = re.compile((r'Bat(man|mobile|copter|bat)'))
mo = bat_regex.search(('Batmobile lost a wheel'))
print(mo.group())
