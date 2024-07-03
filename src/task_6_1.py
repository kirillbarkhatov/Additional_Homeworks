import re






text = '''
Visit my website at https://www.example.com
or you can check out https://www.someotherexample.com
'''

pattern = re.compile(r'[a-zA-Z0-9]+://[a-zA-Z0-9._-]+')

matches = pattern.finditer(text)

#
# for match in matches:
#     print(match)


urls = [match.group() for match in matches]
print(urls)

