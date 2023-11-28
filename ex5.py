'''Check Palindrome Number'''

number = '12321'
is_polindrome = False

for i in range(len(number) // 2):
    if number[i] == number[len(number) - i - 1]:
        is_polindrome = True
        break

if is_polindrome:
    print("True")
else:
    print("False")
    