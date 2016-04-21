import re
s = '4xv2xy2xqx'
p = re.compile(r"\dx[A-z]")
print re.match(p,s[:3])
#def parse_string(s):


