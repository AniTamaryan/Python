'''Print characters from a string that are present at an even index number'''

input_string = 'test_text'

for i in range(0, len(input_string), 2):
    print(input_string[i])
