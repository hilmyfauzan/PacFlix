from math import floor
from module import *
from database import *
from datetime import datetime, timedelta

class User:
    def __init__(self, username:str) -> None:
        # Initialize default value for current_plan, duration_plan,
        # star_date, and end_date.
        self.current_plan = None
        self.start_date = None
        self.end_date = None
        self.plan_duration_left = None
 
        # check if the username is already used
        self.username = check_username(username, new_user_database,
                                                 old_user_database)

        # Generate referral code in the name of the username
        self.own_referral_code = generate_referral_code(self.username)
        
        # Add the referral code into referral_code_database
        referral_code_database.append(self.own_referral_code)
        print(f'\nYour referral code is {self.own_referral_code}')
        print("\nNote : You can't use your own referral code")
  

    def check_benefit(self) -> str:
        """This function will shows all plan benefit."""
        # Generate all plan benefit in form of table using benefit_table from module
        all_plan_benefit = benefit_table()
        
        # Shows all plan benefit
        print("PacFlix Plan List\n")
        print(all_plan_benefit)


    def pick_plan(self) -> str:
        """This function will allow users to choose the plan they want to
           subscribe. Users could also input a referral code if they have
           one so they'll get a discounted price.

        Parameters
        ----------
        new_plan : str
            The new plan that the user are planning to subscribe to.
        referral_code : str
            Unique code from the previous user that will give a discounted
            price tor the user that's using the code.

        Returns
        -------
        str
            The final price, including the discount if they use valid
            referral code.
        """
        # Ask user to input a new plan using ask_plan function from module
        new_plan, plan_code = ask_plan('Pick a plan that you want to subscire to : ', plan_database)

        # Ask to input new_plan duration
        new_plan_duration = input_integer('Input the duration of the plan (month): ')
        
        # Get the new_plan monthly price from plan_database
        # and multiply it with the new_plan_duration to get the plan_price
        plan_price = int((plan_database[plan_code])['plan_price']) * new_plan_duration
            
        # Ask user did they have a refferal code?
        referral_code = ask_ref_code()
        
        # if the user dont user referral code
        if referral_code == None:
            price = plan_price
        
        # Check if the refferal code is valid
        elif referral_code in referral_code_database\
                         and referral_code != self.own_referral_code\
                         and self.username not in old_user_database:
             
             # if yes, give 4% discount
             price = plan_price * 0.96
             print(f"\nYou've used {referral_code} referral code, you'll get 4% discount")
        
        else:
            # if no, give normal price
            price = plan_price
            print(f"\nYour Referral Code couldn't be used or invalid")

        # Shows the final prince on the screen
        print(f"\nYou've subscribed {new_plan.title()} for {new_plan_duration} months!")
        print(f"The price will be : {convert(price)}\n")

        # Add the new_plan information to current_plan and duration_plan atribute of the user
        self.current_plan = new_plan.title()
        self.current_plan_code = plan_code
        
        # Add start_date, end_date and self.plan_duration information
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(new_plan_duration*30)
        self.plan_duration_left = (self.end_date - datetime.now()).days

        print("Your plan will be active until "
              f'{self.end_date.strftime("%d-%m-%Y at %H:%M")}')
        

        # Move user from new_user_database to old_user_database 
        new_user_database.remove(self.username)
        old_user_database.append(self.username)


    def check_plan(self) -> str:
        """This function will show the user current plan, the duration
           and the benefit according to user current active plan.

        Returns
        -------
        str
            1. User current plan and the duration.
            2. Benefit according to user current active plan.
        """
        # Check if the user have any active plan
        if self.current_plan == None:
            print(f'\nHi {self.username}, you currently do not subscribed to any plan')
            print('')
            print('You can check our plan option using .check_benefit()')
            print('You can subscribe to our plan using .pick_plan()')
        
        else:
            print(f"\nYou're currently subscribed to {self.current_plan}")
            print("You're plan is still active until "
                  f'{self.end_date.strftime("%d-%m-%Y at %H:%M")}')


    def upgrade_plan(self) -> str:
        """This function will alow user to upgrade plan from a current_plan
           to a new_plan. User will be asked what is the new_plan.
           
           The function will calculate the price of the upgrade.
        
        Parameters
        ----------        
        new_plan : str
            The new plan that the user are planning to subscribe to.
        
        Returns
        -------
        str
            The final price, user will get the discount if the current plan
            have more than 12 month duration left.
        """
        # Check if the user already subscribed to the highest plan
        if self.current_plan == 'Premium Plan':
            print("You're already subscribed to the highest plan")
        
        # Ask user to input new plan to upgrade
        else:
            while True:
                new_plan, plan_code = ask_plan('Select the plan you want to upgrade to : ', plan_database)
                
                # if the current plan is higher than the new plan
                if self.current_plan_code > plan_code:
                    print(f"\nYou're currently subscribed to {self.current_plan}, "
                          f"You can't downgrade to {new_plan}")
                    print("Please select another plan you want to upgrade to!")
                
                # if the current plan is the same as the new plan
                elif self.current_plan_code == plan_code:
                    print(f"\nYou're already subscribed to {self.current_plan}")
                    print("Please select another plan you want to upgrade to!")
                
                else: break

        # Calculate the price to pay
        # Check if the current duration plan > 12 months
        duration_in_month = floor(self.plan_duration_left / 30)
        if self.plan_duration_left > 360:
            # if yes, the price will be discounted by 5%
            upgrade_price =  int((plan_database[plan_code])['plan_price']) * duration_in_month * 0.95
        else:    
            # if no, then the price will be normal.
            upgrade_price = int((plan_database[plan_code])['plan_price']) * duration_in_month
        
        # Show the final price on the screen
        print(f'\nSucessfully upgraded from {self.current_plan} to {new_plan}.')
        print(f'The total upgrade price will be {convert(upgrade_price)}')

        # Update self.current_plan information to new_plan
        self.current_plan = new_plan.title()