from tkinter import *
from data_base.data_base_manager import *
from validation import *

def save_car () :

    try:
        name_check( car_name.get() )
        model_check( car_model.get() )

        save()   

        car_name.set( "" )
        car_model.set( "" )
        Car_color.set( "" )
        car_plate.set( "" )

    except Exception as e :
        msg.showerror( "Error" , f"{e}" )


   
