from re import *

def name_check ( name ) :
    if match ( r"^[a-zA-Z\s](3-30)$" , name ):
        return name

def model_check ( model ) :
    if match ( r"^[a-zA-Z\s1-9](3-30)$" , model ):
        return model
    
def check_plate ( plate ):
    if match( r"[1-9][a-zA-Z][1-9](6)" , plate ):
        return plate