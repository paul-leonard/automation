'''
Required Features:
- [x] Given a document potential-contacts, find and collect all email addresses and phone numbers.
- [x] Phone numbers may be in various formats.
- [x] (xxx) yyy-zzzz
- [x] yyy-zzzz
- [x] xxx-yyy-zzzz
- [x] etc.
- [x] phone numbers with missing area code should presume 206
- [x] phone numbers should be stored in xxx-yyy-zzzz format.
- [x] Once emails and phone numbers are found they should be stored in two separate documents.
- [x] The information should be sorted in ascending order.
- [x] Duplicate entries are not allowed.
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
  regex_phone = r'((\((\d{3})\)|\d{3})?[\s-]?(\d{3})[\s-]?(\d{4}))'

  # go through text and find each phone number using regex
  regex_finds = re.findall(regex_phone, text_to_search)

  for regex_find in regex_finds:
    #if area code was not included, say it is 206

    if not regex_find[1] and not regex_find[2]:
      this_number_in_correct_format = "206-" + regex_find[3] + "-" + regex_find[4]
    elif regex_find[2]:
      this_number_in_correct_format = regex_find[2] + "-" +  regex_find[3] + "-" + regex_find[4]
    else:
      this_number_in_correct_format = regex_find[1] + "-" + regex_find[3] + "-" + regex_find[4]
    
    if numbers_bst.root.value == None or not numbers_bst.contains(this_number_in_correct_format):
      numbers_bst.add(this_number_in_correct_format)

  return numbers_bst


def identify_emails(text_to_search):
  emails_bst = BinaryTreeSearch()
  regex_email = r'\S+@\S+'      #still to figure out
  regex_finds = re.findall(regex_email, text_to_search)

  for regex_find in regex_finds:
    if emails_bst.root.value == None or not emails_bst.contains(regex_find):
      emails_bst.add(regex_find)

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

emails_bst = identify_emails(text_to_search)
emails_text = text_to_write(emails_bst)
write_to_file(emails_text, "emails")
