'''is_in_str(str_obj, sub_string)'''

def is_in_str(string, isInStr):
    if  isInStr in string:
        return True
    else:
        return False


string = 'hi world'
isInStr = str(input("isInStr = "))

result = is_in_str(string, isInStr)
if result:
    print("True")
else:
    print("False")