import sqlite3

def save ( car_name , car_model , Car_color , car_plate , present_time ) :
    connection = sqlite3.connect( "data_base.db" )
    cursor = connection.cursor()
    cursor.execute(
        f""" INSERT INTO car_info
                ( id, name, model, color, plate, record_time )
                values ( {car_name} , {car_model} , {Car_color} , {car_plate} , {present_time} )
        """ 
        )
    connection.commit()
    connection.close()
