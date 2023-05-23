import sqlite3, sys


def new_db_creation(db_name:str):
	conn = sqlite3.connect(db_name+".sqlite3")
	c = conn.cursor()
	c.execute(
        '''CREATE TABLE `Stations` (
	`station_id` INT PRIMARY KEY NOT NULL,
	`station_name` TEXT NOT NULL UNIQUE ON CONFLICT IGNORE
	);'''
	)
	conn.commit()
	c.execute(
		'''CREATE TABLE `Rentals` (
	`rental_id` INT PRIMARY KEY NOT NULL,
	`bike_number` INT NOT NULL,
	`start_time` DATETIME NOT NULL,
	`end_time` DATETIME NOT NULL,
  	`rental_station` INT NOT NULL,
  	`return_station` INT NOT NULL,
	FOREIGN KEY(rental_station) REFERENCES Stations(station_id),
  	FOREIGN KEY(return_station) REFERENCES Stations(station_id)
);'''
	)
	conn.commit()
	conn.close()


if __name__=="__main__":
	args = sys.argv[1::]
	#print(args)
	if(len(args)):
		new_db_creation(args[0])
	else:
		print("no db name provided!")