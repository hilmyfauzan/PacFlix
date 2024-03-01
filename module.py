"""
file name   : module.py
description : This file contains all the necessary function used in main.py. 
"""

from msilib import Table
from random import randint
from tabulate import tabulate

def convert(price:float)->str:
    """
    convert float into a currency styled string

    Parameters
    ----------
    price : float
        any numbers of IDR currency

    Returns
    -------
    price : str
        the numbers of IDR currency already in format Rp. x,xxx,xxx.xx
    """
    price = f'{price:,.2f}'
    price = price.replace('.','`').replace(',','.').replace('`', ',')
    return f'Rp. {price}'

def generate_referral_code(username:str) -> str:
    """Generate referral code based on username.

    Parameters
    ----------
    username : str

    Returns
    -------
    referral_code: str
        referral code in format : USERNAME+5_RANDOM_NUMBER
    """
    # Generate referral code
    referral_code = username.upper() + ''.join(str(randint(0, 9)) for _ in range(5))
    
    return referral_code

def ask_plan(message:str, plan_database:list):
    """this function will prompt user for a plan_name and check wether
       the plan_name exist in plan_database

    Parameters
    ----------
    message : str
        message that will appear to ask the user for new_plan
    plan_database : list
        a list containing all the details regarding the plan

    Returns
    -------
    list
        This function will return a list containing
        [plan_name, plan_code]
    """
    while True:
        new_plan = input(f'{message}')

        # Check wheter the new_plan existed in plan_database
        for plan in plan_database:
            if new_plan.lower().strip() == plan['plan_name'].lower():
                plan_code = plan_database.index(plan)
                return new_plan, plan_code

        print("Your selected plan doesn't exist, choose another plan.")

def check_username(username:str, new_user_database:list,
                                 old_user_database:list) -> str:    
    """This function will check wether the username have already
       been used. If the username already been used, ask for new
       username. 

    Parameters
    ----------
    username : str
    new_user_database : list
        username database of a user that haven't purchase their first plan
    old_user_database : list
        username database of a user that already have purchase history

    Returns
    -------
    username: str
    """
    while True:
        if (username in new_user_database) or (username in old_user_database):
            print(f'Username {username} is already used, '
                'Try again with different username!\n')
            username = input('Input new username : ')
            
        else:
            # Assign username to the user and add it to the new_user_database
            new_user_database.append(username)
            print(f"You've sucessfully registered as {username}")
            return username

def benefit_table()->Table:
    """This function will generate table for all plans benefit.

    Returns
    -------
    benefit_table : Table
        Table of All Plan's benefit and price.
    """
    table = [
        [True, True, True, "Bisa Stream"],
        [True, True, True, "Bisa Download"],
        [True, True, True, "Kualitas SD"],
        [False, True, True, "Kualitas HD"],
        [False, False, True, "Kualitas UHD"],
        [1, 2, 4, "Number of Devices"],
        ["3rd party Movie only", "Basic Plan Content + Sports",
         "Basic Plan + Standard Plan + PacFlix Original Series",
         "Jenis Konten"],
        ["Rp 120.000,00", "Rp 160.000,00", "Rp 200.000,00", "Harga per Bulan"]
    ]
    
    headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Services"]

    benefit_table = tabulate(table, headers)
    return benefit_table

def input_integer(message:str)->int:
    """This function will ask user to input an integer. If the user input
       any other else, the program will keep looping.

    Parameters
    ----------
    message : str
        Message you want to show as input message

    Returns
    -------
    res : int
        Integer inputted by the user
    """
    while True:
        try:
            while True:
                res = int(input('Input the duration of the plan (month): '))
                if res != 0: return res

        except ValueError:
            print('Please input an integer!')

def ask_ref_code():
    while True:
        have_refferal_code = input('Do you have any refferal code (y/n) :') 
        
        # if yes, ask for the refferal code
        if have_refferal_code.lower().strip() == 'y':
            refferal_code = input('Input your refferal code : ')
            return refferal_code
        
        # if no, continue the program to the next step
        elif have_refferal_code.lower().strip() == 'n':
            refferal_code = None
            return refferal_code
        
        # if the answer is not y/n, ask again
        else:
            print('Your answer is invalid, please answer only with y or n')
        