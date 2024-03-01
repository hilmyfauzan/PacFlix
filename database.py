"""
file name   : database.py
description : This file contain all the database used in main.py
"""

# New User Database
"""This Database will store the username of every user that havent purchased their first plan"""
new_user_database = []

# Old User Database
"""This Database will store the username of every user that have purchase history""" 
old_user_database = []


# Referral Code Database
"""This Database will store the referral code from every user"""
referral_code_database = []

# Plan Database
"""
This Database contain all the details regarding the plan :
1. plan_name     : Plan Name
2. can_stream    : Wether the plan can stream or not
3. can_download  : Wether the plan have download option or not
4. has_SD        : Wether the plan can acess Standard Defintion Quality
5. has_HD        : Wether the plan can acess High Defintion Quality
6. has_UHD       : Wether the plan can acess Ultra High Defintion Quality
7. num_of_device : How many device can the plan being used at the same time
8. content       : The type of content the plan have
9. plan_price    : Monthly price of the plan in IDR
"""
plan_database = [
    {
        'plan_name':'Basic Plan', 'can_stream':True, 'can_download':True,
        'has_SD':True, 'has_HD':False, 'has_UHD':False, 'num_of_device':1,
        'content':'3rd party movie only', 'plan_price':120_000 
    },
    
    {
        'plan_name':'Standard Plan', 'can_stream':True, 'can_download':True,
        'has_SD':True, 'has_HD':True, 'has_UHD':False, 'num_of_device':2,
        'content':'Basic Plan Content + Sports (F1, Footbal, Basketball)',
        'plan_price':160_000 
    },

    {
        'plan_name':'Premium Plan', 'can_stream':True, 'can_download':True,
        'has_SD':True, 'has_HD':True, 'has_UHD':True, 'num_of_device':4,
        'content':'All the Basic and Standard Plan Content + Pacflix Original Series or Movie',
        'plan_price':200_000 
    }      
]