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