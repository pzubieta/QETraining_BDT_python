def print_messages(age):
    if age < 12:
        return 'you are a child'
    if 13 < age < 17:
        return 'you are a teenager'
    if 18 < age < 29:
        return 'you are young'
    if age > 30:
        return 'you are adult'