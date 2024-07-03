import re


text = 'Цвет неба - синий.'

print(re.sub(r'синий', 'blue', text))
