import sqlite3

Connection = sqlite3.connect( "data_base.db" )
Cursor = Connection.cursor()
Cursor.execute( 
    """ 
    CREATE table car_info (
            id           integer primary key autoincrement,
            name         text,
            model        text,
            color        text,
            plate        text,
            record_time  text
     ) """ 
    )

Connection.commit()
Connection.close()


def save () :
    Connection = sqlite3.connect( "data_base.db" )
    Cursor = Connection.cursor()
    Cursor.execute( """ INSERT INTO """ )