print("PassGuard, the ultimate password assistant. Secure and easy to use!")



print("v-9.7.4")
def generate():
    
    import uuid
    password = uuid.uuid4()

    password = str(password)
    print("PASSGUARD: " +password)

def generate_in_notebook():
    import uuid
    passwordnote = uuid.uuid4()
    print("Password Purpose: ")
    purpose = input("")
    passwordnote = str(passwordnote)
    
    print("Saving Password To passnote.txt")
    filename = ("Passnote.txt")
    a = (purpose+ ":\n\n " +passwordnote+"\n\n")
    f = open(filename, "a")
    f.write(a)
    f.close()

def onlyp():
    import uuid
    passwordnote = uuid.uuid4()
    passwordnote = str(passwordnote)
        
    print("Saving Password To passnote.txt")
    filename = ("Passnote.txt")
    a = (":\n\n " +passwordnote+"\n\n")
    f = open(filename, "a")
    f.write(a)
    f.close()

def newbook():
    filename = ("Newbook.txt")
    a = ("Newbook.txt, made from PassGuard")
    f = open(filename, "a")
    f.write(a)
    f.close()
    print("Made new book")

def https():
    import webbrowser
    https = input("https://www." )
    webbrowser.open("https://" +https)
