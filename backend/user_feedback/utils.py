import re

def valid_string(s):
    if not isinstance(s,str) or not s:
        raise ValueError("Must be a non-empty string")
    return s

def valid_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    if not isinstance(email,str) or not email or not re.search(regex, email):
        raise ValueError("Must be a valid email format")
    return email
