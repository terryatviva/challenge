import re

# Used by RequestParser to make sure that argument is a string and not empty 
def valid_string(s):
    if not isinstance(s,str) or not s:
        raise ValueError('Must be a non-empty string')
    return s

# Used by RequestParser to make sure that argument is a string, not empty,
# and a valid email
def valid_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    if not isinstance(email,str) or not email or not re.search(regex, email):
        raise ValueError('Must be a valid email format')
    return email