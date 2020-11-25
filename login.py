
def get_login_name():
    
 f_name = input("Enter your first name: ")
 l_name = input("Enter your last name: ")
 id = input("Enter your student ID number: ")
 print("Your system login name is:\n" + f_name[0:3]  + l_name[0:3] + id[-3:])

get_login_name()