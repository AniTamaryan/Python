'''startswith(str_obj, sub_string)'''

def starts_with(string, startswith):
    if string[:len(startswith)] == startswith:
        return True
    else:
        return False


string = 'hi world'
startswith = str(input("startswith = "))

result = starts_with(string, startswith)
if result:
    print("True")
else:
    print("False")
    
