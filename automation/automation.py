'''
Required Features:
- [ ] Given a document potential-contacts, find and collect all email addresses and phone numbers.
- [ ] Phone numbers may be in various formats.
- [ ] (xxx) yyy-zzzz
- [ ] yyy-zzzz
- [ ] xxx-yyy-zzzz
- [ ] etc.
- [ ] phone numbers with missing area code should presume 206
- [ ] phone numbers should be stored in xxx-yyy-zzzz format.
- [ ] Once emails and phone numbers are found they should be stored in - [ ] two separate documents.
- [ ] The information should be sorted in ascending order.
- [ ] Duplicate entries are not allowed.
'''

import re
from automation.tree import BinaryTreeSearch

regex_phone = re.compile(r'\d{3}[-\s]?\d{4}\D')  #only get's 7 digits so far
regex_email = re.compile(r'^\S+@\S+.\w{3}')      #still to figure out

phone_bst = BinaryTreeSearch()
email_bst = BinaryTreeSearch()




with open("potential-contacts.txt", "r") as input_file:
  input_file_contents = input_file.read()
  
  mo_phone = regex_phone.search(input_file_contents)

#pseudo code
#  with open("outputfilename", "w") as output_file_phone:
#    for match in match_list:
#      if match not in output_file_phone already:
#        add it
#  
    