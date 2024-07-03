import re


text = "djfnvk 11-12-2021 kbhhhh21-11-2003 lhlbhh11-03-2011nbjhh"

pattern = re.compile(r'\d{2}-\d{2}-\d{4}')

matches = pattern.findall(text)

print(matches)

