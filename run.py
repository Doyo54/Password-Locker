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


def new_credentials(Cname, Cpassword):
    new_credentials = Credentials(Cname,Cpassword)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save new credentials
    '''
    credentials.save_credentials()

def display_cred():
    '''
    Function that returns all the saved users
    '''
    return Credentials.display_cred()

def main():
            print("Hello Welcome to your Password locker. What is your name?")
            user_name=input()

            print(f"Hello {user_name}.")
            print('\n')

            while True:
                    print("Use these short codes : ca - create a new User, lg - login into existing account, dc - display Existing accounts, ex -EXIT app")  
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
                              print('Use these short codes to get around: cc - Create new credentials, dc -Display credentials, cg - Create crendentials with generated Password, ex -Exit')
                              short_code = input()
                              if short_code == 'cc':
                                   print("New User")
                                   print("-"*10)

                                   print ("User name ....")
                                   name = input()

                                   print("Password ...")
                                   password = input()

                                   save_credentials(new_credentials(name,password))
                                  
                                   




                          
        








                    elif short_code == 'ex':
                        print("bye")
                        break

                            




if __name__ == '__main__':
    main()