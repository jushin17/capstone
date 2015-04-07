import gps_getData
import time

if __name__ == '__main__':
    gps_getData.initGPS()

    while True:
        lat, lon = gps_getData.getGPS_lat_lon()
    
        print lat ,' ' , lon

        sleep(5)
