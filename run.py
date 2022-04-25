#!/usr/bin/env python3.9
from user import User
from credentials import Credentials
def create_user(Uname,password):
    new_user = User(Uname,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()

def logIn(name, password):
    '''
    Function that allows a user to log into their account
    '''
    if User.log_in(name, password) != False:
        return User.log_in(name, password)


def new_credentials(cName, cuName, cPassword):
    new_credentials = Credentials(cName, cuName,cPassword)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save new credentials
    '''
    credentials.save_credentials()

def display_cred():
    '''
    Fucntion that returns all the saved users
    '''
    return Credentials.display_cred()

def random_password():
    return Credentials.generate_password()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_cred()

def find_credential(credential_name):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_Credential(credential_name)

def main():
            print("Hello Welcome to your Password locker. What is your name?")
            user_name=input()

            print(f"Hello {user_name}.")
            print('\n')

            while True:
                    print("Use these short codes : \n ca - Create a new account \n lg - Login into existing account \n dc - Display existing accounts \n ex - Exit App")  
                    short_code = input().lower()

                    if short_code == 'ca':
                            print("New User")
                            print("-"*10)

                            print ("User name ....")
                            name = input()

                            print("Password ...")
                            password = input()

                            save_users(create_user(name,password)) # create and save new contact.
                            print ('\n')
                            print(f'''New User {name}. Welcome! In this application you can create credentials and save them here for later use.
                        Login to get started \n
                            ''')

                    elif short_code == 'dc':

                            if display_user():
                                    print("You have the following accounts:")
                                    print('\n')

                                    for user in display_user():
                                            print(f"Username: {user.user_name} Password: {user.user_password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any accounts saved yet")
                                    print('\n')

                    elif short_code == 'lg':
                        print("\n")
                        print("Log into Password Locker Account")
                        user_name = input('Enter the user name: ')
                        user_password = input('Enter Password: ')

                        if logIn(user_name,user_password) == None:
                          print("\n")
                          print("Please try again or create an account")
                          print("\n")

                        else:

                          logIn(user_name,user_password)
                          print("\n")
                          print(f"{user_name} welcome to your Credentials")
                          while True:
                              print('Use these short codes: \n cc - Create new credentials \n dc -Display credentials \n cg - Create crendentials with generated Password \n dl - Delete credential \n lg - Log out')
                              short_code = input().lower()

                              if short_code == 'cc':
                                   print("New User")
                                   print("-"*10)
                                   credential = input('Credentials name: ')
                                   user_name = input(f"{credential} Username: ")
                                   password = input("Password: ")

                                   save_credentials(new_credentials(credential,user_name,password))
                                   print(f"Credentials for {credential} succesfully created")
                                   print('\n')
                                      
                              elif short_code == 'dc':

                                  if display_cred():
                                    print("You have the following credentials saved:")
                                    print('\n')

                                    for credentials in display_cred():
                                        print(f"{credentials.credential_name} account")
                                        print(f"Username: {credentials.credential_user_name} Password: {credentials.credential_password}")

                                    print('\n')
                                  else:
                                    print('\n')
                                    print("You dont seem to have any Credentials saved yet")
                                    print('\n')
                              elif short_code == 'cg':

                                  name = input("Credential name: ")
                                  user_name =input("User name: ")
                                  print("Password succesfully generated")
                                  password = random_password()
                                  
                                  print(f"Password: {password}")
                                  print('\n')
                                  save_credentials(new_credentials(name,user_name,password))
                              elif short_code == 'dl':
                                   print("Enter the name of the Credential you want to delete")
                                   cred_name = input()

                                   if find_credential(cred_name) == None:
                                     print('Credentials does not exist')
                                   else:
                                     search_cred = find_credential(cred_name)
                                     search_cred.delete_cred()
                                     print('\n')
                                     print(f"Your stored credentials for : {search_cred.credential_name} successfully deleted!!!")
                                     print('\n')
                    

                              elif short_code == 'lg':
                                  print('You have successfully logged out.')
                                  print('\n')
                                  break
                                  



                          
        








                    elif short_code == 'ex':
                        print("See you next time!")
                        break

                            




if __name__ == '__main__':
    main()