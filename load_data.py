import sqlite3, sys, datetime

def data_loader(source:str, database:str):

    file = open(source, "r")
    data_lines = [tmp.strip().split(",") for tmp in file.readlines()][1::]
    lines = [(int(t[0]), int(t[1]), t[2], t[3], t[4], t[5]) for t in data_lines]
    conn = sqlite3.connect(database+".sqlite3")
    cursor = conn.cursor()
    i=1
    dictionary = {}
    for l in lines:
        try:
            cursor.execute('INSERT INTO Stations (station_id, station_name) VALUES (?, ?)', (i, l[5]))
            conn.commit()
            i+=1
            dictionary[l[5]]=i
        except:
            pass
    lines2 = [(int(t[0]), int(t[1]), t[2], t[3], int(dictionary.get(t[4])), int(dictionary.get(t[5]))) for t in lines]
    cursor.executemany('INSERT INTO Rentals (rental_id, bike_number, start_time, end_time, rental_station, return_station) VALUES (?, ?, ?, ?, ?, ?)', lines2)
    conn.commit()
    conn.close()
















if __name__=="__main__":
	
    

    args = sys.argv[1::]
    if(len(args)>=2): 
        data_loader(args[0], args[1])
        try:
            data_loader(args[0], args[1])
        except:
            print("Exception ocurred!")