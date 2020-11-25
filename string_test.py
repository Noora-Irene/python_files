string = input("Enter a string: ")

def main():
  print("This is what I found about that string:")
   
  if string.isalpha() and string.islower(): 
    print("The string is alphanumeric.\nThe string contains only alphabetic characters.\nThe letters in the string are all lowercase.")
  elif string.isalpha() and string.isupper(): 
    print("The string is alphanumeric.\nThe string contains only alphabetic characters.\nThe letters in the string are all uppercase.")
  elif string.isdigit(): 
    print("The string is alphanumeric.\nThe string contains only digits.")
  elif string.isdigit() and string.isupper(): 
    print("The string is alphanumeric.\nThe letters in the string are all uppercase.")
  else: 
    print("The string is alphanumeric.\nThe letters in the string are all lowercase.") 

main()