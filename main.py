from pyscript import display
from js import document

def passwordChecker(e):
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    document.getElementById("output").innerHTML = ""
    
   
    nume = any(char.isdigit() for char in password)
    
   
    limit = len(password) > 12 or len(password) == 0
    
    if nume:
        display("Password must contain at least one number", target="output")
    elif limit:
        display("Password cannot exceed 12 characters or be empty", target="output")
    else:
        display(f"you made an account welcome {username}", target="output")

#groupmate assistance especially on the elif parts and the addiitonal js import document




