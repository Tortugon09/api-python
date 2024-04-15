import re

def validate_account_number(account_number):
    """Valida que el número de cuenta tenga 16 dígitos y comience con '7490'."""
    return bool(re.match(r'^7490\d{12}$', account_number))

def validate_nip(nip):
    """Valida que el NIP tenga 4 dígitos."""
    return bool(re.match(r'^\d{4}$', nip))
