# Python String Methods Practice

# TODO: Use the capitalize() method to capitalize the first letter of the string
# Example: "python" -> "Python"
string1 = "python"
# Your code here
capitalized_string1 = string1.capitalize()
print(capitalized_string1)

# TODO: Use the center() method to center the string in a string of specified width
# Example: "python" -> "  python  "
string2 = "python"
# Your code here
centered_strings2 = string2.center(10)
print(centered_strings2)

# TODO: Use the endswith() method to check if the string ends with a specified substring
# Example: Check if "python" ends with "on"
string3 = "python"
# Your code here
ends_with_on = string3.endswith("on")
print(ends_with_on)

# TODO: Use the find() method to find the first occurrence of a substring in the string
# Example: Find the position of "th" in "python"
string4 = "python"
# Your code here
position_th = string4.find("th")
print(position_th)

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
# Example: Check if "python3" is alphanumeric
string5 = "python3"
# Your code here
is_alphanumeric = string5.isalnum()
print(is_alphanumeric)

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
# Example: Check if "python" is alphabetic
string6 = "python"
# Your code here
is_alphabetic = string6.isalpha()
print(is_alphabetic)

# TODO: Use the islower() method to check if all characters in the string are lowercase
# Example: Check if "python" is in lowercase
string7 = "python"
# Your code here
is_lowercase = string7.islower()
print(is_lowercase)

# TODO: Use the isspace() method to check if all characters in the string are whitespaces
# Example: Check if "   " is all whitespace
string8 = "   "
# Your code here
is_whitespace = string8.isspace()
print(is_whitespace)

# TODO: Use the isupper() method to check if all characters in the string are uppercase
# Example: Check if "PYTHON" is in uppercase
string9 = "PYTHON"
# Your code here
is_uppercase = string9.isupper()
print(is_uppercase)

# TODO: Use the join() method to join elements of an iterable with the string as the separator
# Example: Join ["Python", "is", "fun"] with "-" as separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
# Your code here
joined_string = separator.join(iterable1)
print(joined_string)

# TODO: Use the lower() method to convert all characters in the string to lowercase
# Example: Convert "PYTHON" to lowercase
string10 = "PYTHON"
# Your code here
lowercase_string10 = string10.lower()
print(lowercase_string10)

# TODO: Use the lstrip() method to remove leading characters (spaces by default)
# Example: Remove leading spaces from "  python"
string11 = "  python"
# Your code here
stripped_string11 = string11.lstrip()
print(stripped_string11)

# TODO: Use the rstrip() method to remove trailing characters (spaces by default)
# Example: Remove trailing spaces from "python  "
string12 = "python  "
# Your code here
stripped_string12 = string12.rstrip()
print(stripped_string12)

# TODO: Use the replace() method to replace all occurrences of a substring with another substring
# Example: Replace "python" with "snake" in "I love python"
string13 = "I love python"
# Your code here
replaced_string13 = string13.replace("python", "snake")
print(replaced_string13)

# TODO: Use the rfind() method to find the highest index of a substring
# Example: Find the highest index of "n" in "python"
string14 = "python"
# Your code here
highest_index_n = string14.rfind("n")
print(highest_index_n)

# TODO: Use the split() method to split the string at a specified separator
# Example: Split "python-is-fun" at "-"
string15 = "python-is-fun"
# Your code here
split_string15 = string15.split("-")
print(split_string15)

# TODO: Use the startswith() method to check if the string starts with a specified substring
# Example: Check if "python" starts with "py"
string16 = "python"
# Your code here
starts_with_py = string16.startswith("py")
print(starts_with_py)

# TODO: Use the strip() method to remove both leading and trailing characters (spaces by default)
# Example: Remove spaces from "  python  "
string17 = "  python  "
# Your code here
stripped_string17 = string17.strip()
print(stripped_string17)

# TODO: Use the swapcase() method to swap the case of all characters in the string
# Example: Swap case of "Python"
string18 = "Python"
# Your code here
swapped_case_string18 = string18.swapcase()
print(swapped_case_string18)

# TODO: Use the title() method to convert the first character of each word to uppercase
# Example: Convert "python is fun" to title case
string19 = "python is fun"
# Your code here
title_case_string19 = string19.title()
print(title_case_string19)

# TODO: Use the upper() method to convert all characters in the string to uppercase
# Example: Convert "python" to uppercase
string20 = "python"
# Your code here
uppercase_string20 = string20.upper()
print(uppercase_string20)