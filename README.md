# PacFlix
## A Simple CLI Video Streaming Service Project
### **Project Description**
This project is done as a porject for Lecture 12 on Introduction to Python for Software Engineering Class in Pacman Data Academy. This project is used to demonstrate student understanding of Class, Function, Clean Code, Data Structure and Git.

PacFlix is Video Streaming Service Platform. It have 3 subscription plans :
* Basic Plan
* Standard Plan
* Premium Plan

Every plan have its own perks and different monthly price as shown in table 1.

| **Basic Plan**       | **Standard Plan**                                       | **Premium Plan**                                               | **Services**   |
|----------------------|---------------------------------------------------------|----------------------------------------------------------------|----------------|
| ✓                    | ✓                                                       | ✓                                                              | can_stream     |
| ✓                    | ✓                                                       | ✓                                                              | can_download   |
| ✓                    | ✓                                                       | ✓                                                              | has_SD         |
|                      | ✓                                                       | ✓                                                              | has_HD         |
|                      |                                                         | ✓                                                              | has_UHD        |
| 1                    | 2                                                       | 4                                                              | num_of_devices |
| 3rd party movie only | Basic Plan Content + Sports  (F1, Football, Basketball) | Basic Plan + Standard Plan +  PacFlix Original Series or Movie | content        |
| Rp 120.000,-         | Rp 160.000,-                                            | Rp 200.000,-                                                   | price          |

<p align="center"> Table 1. List of All Available Plans in Pacflix </p>

Here are few things or rules on what the user can do :
* User can only choose one of the subscription plan available
* User can only upgrade plan, not downgrade
* User can upgrade from a lower version plan to higher version plan, not he other way around.
  * if User have more than 12 month subscription left, User will get 5% discount on the upgrade

### **Project Objective**
We want to create a program where user could do :
* Check all available subscription plans on PacFlix
* Pick a subscription plan
* Check current active subscription plan
  * if the User have no transaction history (new user), User could input a referral code from another User to get a 4% discount
* Upgrade plan from an existing subscription plan to higher version subscription plan

### **Repositories Explanation**
* **main.py** : This file is where the class User and every function on the user is created.
* **database.py** : This file contain all the database used in main.py
* **module.py** : This file contains all the suporting function used in main.py.
* **case_study.ipynb** : This file is where the program is being tested on case studies.
