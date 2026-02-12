from pyscript import display, document

def passwordChecker(e):

    password = document.getElementById("input").value
    special_characters = "!@#$%^&*()-+"
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_characters for c in password)

    if len(password) < 8:
        display("Password must be at least 8 characters long.")
    elif not has_upper:
        display("Password must contain at least one uppercase letter.")
    elif not has_lower:
        display("Password must contain at least one lowercase letter.")
    elif not has_digit:
        display("Password must contain at least one digit.")
    elif not has_special:
        display("Password must contain at least one special character: " + special_characters)
    else:
        display("Password is strong and meets all criteria.", target="output")

    





