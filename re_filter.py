import re

pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')

with open('./data/data.txt', 'r') as rf:
  contents = rf.read()
  with open('./data/phone_numbers.txt', 'w') as wf:
    matches = pattern.finditer(contents)

    for match in matches:
      wf.write(match.group(0) + '\n')
