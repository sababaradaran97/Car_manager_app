from tkinter import *
from tkinter.ttk import Combobox
from tools.mudals import *

def view ():
    window = Tk()
    window.title( "Car_program" )
    window.geometry ( "500x400" )

    #Car name
    car_name = StringVar()
    Label( window , text = "Car name" ).place( x = 25 , y = 30 )
    Entry( window , textvariable = car_name ).place( x = 100 , y = 30 )

    #Car model
    car_model = StringVar()
    Label( window , text = "Car model" ).place( x = 25 , y = 70 )
    Entry( window , textvariable = car_model ).place( x = 100 , y = 70 )

    #Car color
    Car_color = StringVar()
    Label( window , text = "Car color" ).place( x = 25 , y = 110 )
    Combobox( window , values = [ "White" , "Black" , "Red" ] , width = 17 , state = "readonly" ).place( x = 100 , y = 110 )

    #car plate
    car_plate = StringVar()
    Label( window , text = "Car plate" ).place( x = 25 , y = 150 )
    Entry( window , textvariable = car_plate ).place( x = 100 , y = 150 )

    #save
    Button( window , text = "save" , width = 15 , command = save_car( car_name , car_model , Car_color , car_plate ) ).place( x = 25 , y = 200 )


    window.mainloop()
