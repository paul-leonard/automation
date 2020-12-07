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


# ******  IMPORTS  ******
import re
from tree import BinaryTreeSearch

# ******  DEFINITIONS  ******
class InvalidOperationError(Exception):
  pass


def get_file_contents():
  with open("potential-contacts.txt", "r") as input_file:
    input_file_contents = input_file.read()
  return input_file_contents
  

def identify_numbers(text_to_search):
  numbers_bst = BinaryTreeSearch()
  regex_phone = r'\d{3}[-\s]?\d{4}\D'  #only get's 7 digits so far

  # go through text and find each phone number using regex
  regex_finds = re.findall(regex_phone, text_to_search)

  for find in regex_finds:
    # if not numbers_bst.contains(find):
    numbers_bst.add(find)


  # edit each number to correct format
    # correct dashes
    # add 206 if needed

  # if number not already in BST using the contain method
  # if not numbers_bst.contains(number):
    # add each number to BST


  return numbers_bst


def identify_emails(text_to_search):
  emails_bst = BinaryTreeSearch()
  regex_email = re.compile(r'^\S+@\S+.\w{3}')      #still to figure out
  # will be similar to numbers
  # go through text and find each phone number using regex
  # edit each number to correct format (add 206 if needed)
  # if number not already in BST using the contain method 
    # add each number to BST
  return emails_bst
  

def text_to_write(contact_bst):
  # convert bst to list using method to get in ascending order
  contact_list = contact_bst.inOrder()
  text_string_to_write = ""
  
  # iterate through list to add each contact followed by a new line
  for contact in contact_list:
    text_string_to_write += contact + "\n"

  return text_string_to_write


def write_to_file(text_to_write, contact_type):
  if contact_type == "numbers":
    file_to_write_to = "phone_numbers.txt"
  elif contact_type == "emails":
    file_to_write_to = "emails.txt"
  else:
    raise InvalidOperationError("Invalid contact data type.")

  # open file
  with open(file_to_write_to, "wt") as file:
    file.write(text_to_write)



# ******  FUNCTION CALLS  ******
text_to_search = get_file_contents()

numbers_bst = identify_numbers(text_to_search)
numbers_text = text_to_write(numbers_bst)
write_to_file(numbers_text, "numbers")

# emails_bst = identify_emails(text_to_search)
# emails_text = text_to_write(emails_bst)
# write_to_file(emails_text, "emails")




    