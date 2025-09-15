from tkinter import *
from tkinter.ttk import *
from data_base.data_base_manager import *
from tools.validation import *
from view.car_park_veiw import *
from datetime import *

def save_car ( car_name , car_model , Car_color , car_plate ) :

    try:
        present_time = datetime.now()
        name_check( car_name )
        model_check( car_model )
        check_plate(  )

        save( car_name , car_model , Car_color , car_model , present_time )   

        car_name.set( "" )
        car_model.set( "" )
        Car_color.set( "" )
        car_plate.set( "" )

    except Exception as e :
        Message.showerror( "Error" , f"{e}" )
    

