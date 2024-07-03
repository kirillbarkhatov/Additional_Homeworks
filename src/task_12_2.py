import re

text = "ladjvfdvf #jjfj #dfkjvndfkv7765 lkfjvfkl; #009ij"

pattern = re.compile(r'#\w+')

matches = pattern.findall(text)

print(matches)