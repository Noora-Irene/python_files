from collections import Counter

user_input = Counter(input("Enter input: "))

def main():

 letter_count = 0
 for letter in user_input:
   if letter in ['T', 't']:
       letter_count += user_input[letter]

print('Input contains T or t {} pieces.'.format(user_input['T'] + user_input['t']))
main()
