import sqlite3

def save () :
    Connection = sqlite3.connect( "data_base.db" )
    Cursor = Connection.cursor()
    Cursor.execute(
        """ INSERT INTO car_info
                ( id, name, model, color, plate, record_time )
                values ( {car_name} , {car_model} , {Car_color} , {car_plate} )
        """ 
        )
    Connection.commit()
    Connection.close()
