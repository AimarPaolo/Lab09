from database.DB_connect import DBConnect
from model.airport import Airport
from model.flights import Flights


class DAO():
    @staticmethod
    def get_all_airports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select * from airports a"
        cursor.execute(query)
        for row in cursor:
            result.append(Airport(row["ID"], row["IATA_CODE"], row["AIRPORT"], row["CITY"], row["STATE"], row["COUNTRY"], row["LATITUDE"], row["LONGITUDE"], row["TIMEZONE_OFFSET"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_media_tratta():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select f.ID ,f.ORIGIN_AIRPORT_ID ,f.DESTINATION_AIRPORT_ID, AVG(DISTANCE) as distanza_media, COUNT(*) as CONTATORE
                    from flights f 
                    group by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID """
        cursor.execute(query)
        for row in cursor:
            result.append(Flights(row["ID"], row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["distanza_media"], row["CONTATORE"]))
        cursor.close()
        conn.close()
        return result
