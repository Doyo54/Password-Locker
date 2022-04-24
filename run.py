#!/usr/bin/env python3.9
from user import User

def create_user(Uname,password):
    new_user =User(Uname,password)
    return new_user

def save_users(user):
    '''
    Function to save contact
    '''
    user.save_user()

def display_user():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_user()

def main():
            print("Hello Welcome to your Password locker. What is your name?")
            user_name=input()

            print(f"Hello {user_name}.")
            # print("Use these short codes : ca - create a new User, dc - display Existing user, ex - Delete user")
            print('\n')

            while True:
                    print("Use these short codes : ca - create a new User, dc - display Existing user, ex -EXIT user")  
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
                            # print(f"New User {name}. Welcome! In this application you can create credentials and save them here for later use")
                            print(f"Name:{name}")
                            print(f"Password:{password}")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_user():
                                    print("Here is a list of all your Users")
                                    print('\n')

                                    for user in display_user():
                                            print(f"Username: {user.user_name} Password: {user.user_password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any Users saved yet")
                                    print('\n')

                    elif short_code == 'ex':
                            print("bye")
                            break

                            




if __name__ == '__main__':
    main()