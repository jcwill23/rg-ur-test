# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:15:08 2018

@author: jcwil
"""

def smartsheet_connect(my_token):
    import smartsheet

    # Create base client object and set the access token.
    smartsheet = smartsheet.Smartsheet(my_token)

    # Get current user.
    user = smartsheet.Users.get_current_user()
    print(user)
#%%    