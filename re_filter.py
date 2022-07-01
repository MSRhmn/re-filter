import re

num_pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

with open('./data/data.txt', 'r') as rf:
  contents = rf.read()
  with open('./data/phone_numbers.txt', 'w') as wf:
    matches = num_pattern.finditer(contents)

    for match in matches:
      wf.write(match.group(0) + '\n')
  
  with open('./data/email_addresses.txt', 'w') as wf:
    matches = email_pattern.finditer(contents)

    for match in matches:
      wf.write(match.group(0) + '\n')
