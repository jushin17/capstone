import json

class ReadJson:
    def read(self):
        with open('test.json') as f:
        #for line in f:
            test = json.loads(line)
            if(test['name']=='vehicle_speed'):
                DataScore.dataScore['speed']=test['value']
            elif(test['name']=='transmission_gear_position'):
                DataScore.dataScore['gear']=test['value']
            elif(test['name']=='steering_wheel_angle'):
                DataScore.dataScore['steering']=test['value']
             
