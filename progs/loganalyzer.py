import re

fh = open('error.log')
p = r'^\[(?P<day>[a-zA-Z]{3}) (?P<month>[a-zA-z]{3}) (?P<date>[\d]{1,2}) (?P<timestamp>\b[\d:\.]+\b) (?P<year>[\d]{4})\] \[(?P<error>[\w:]+)\] \[(?P<who>[\w: ]+)\] (?P<msg>.+)$'
reo = re.compile(p)

e_list = []
for line in fh:
    m = reo.search( line)
    if m:
        e_list.append(m['error'])

print(len(e_list))

errors = { item:e_list.count(item) for item in e_list}

print(errors)
fh.close()        