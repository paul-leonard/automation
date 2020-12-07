# automation
Automation script to identify and capture phone numbers and emails from mixed text.

## Lab Submission Pull Requests
[Lab19: Automation](https://github.com/paul-leonard/automation/pull/1)

## Release Info
**Author**: Paul Leonard
**Version**: 0.9.0

## Overview
This automation script will comb through a long, boring, and jumbled mess of a text file in search for contact information including phone numbers and emails.

## Architecture
This script opens the target text file and uses regex to search for phone numbers and emails.  It then writes them to seperate text files in ascending order, while ensuring duplicates are not recorded.  The file opening and searching is done by a shared function of the two functions used for finding emails/contacts.  The found information is stored in a BST to provide the sorting function before being written to a new resulting text file.

## Change Log
**0.9.0** 12-3-2020 - Initial beta release
**1.0.0** 11-TBD-2020 - Initial release


## Credits and Collaborations
- Regex Fun with Mark Bell, Seth Mcfeeters, and Lee Thomas
- Regex pointer from Robert Radford
- Module structure with Lee Thomas
- [All the thanks to Regex101](regex101.com)
- [not a digit](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html#:~:text=In%20regex%2C%20the%20uppercase%20metacharacter,%5E0%2D9%5D%20)
- [read file](https://www.w3schools.com/python/python_file_open.asp)
- [regex re library](https://docs.python.org/3/library/re.html)
- [re.findall with groups](https://developers.google.com/edu/python/regular-expressions)
