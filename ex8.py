'''endswith(str_obj, sub_string'''

def ends_with(string, endswith):
    if len(endswith) <= len(string) and string[-len(endswith):] == endswith:
        return True
    else:
        return False


string = 'hi world'
endswith = str(input("endswith = "))

result = ends_with(string, endswith)
if result:
    print("True")
else:
    print("False")