class Setting:
	SafetyStand=[]
	SnowStand=[]
	RainStand=[]
	SpeedStand=[]
    
	def __init__(self):
		#set standard of Safety judgement
		SafetyStand[0]=0
		SafetyStand[1]=60
		SafetyStand[2]=80
    
		#set standard of snow
		SnowStand[0]=0
		SnowStand[1]=1
		SnowStand[2]=5
		SnowStand[3]=20
    
		#set standard of rain
		RainStand[0]=0
		RainStand[1]=5
		RainStand[2]=20
		RainStand[3]=80
    
		#set standard of speed
		SpeedStand[0]=0
		SpeedStand[1]=80
		SpeedStand[0]=100
    

	def setSafetyStand(val1,val2,val3):
		SafetyStand['stand0']=val1
		SafetyStand['stand1']=val2
		SafetyStand['stand2']=val3

	def setSnowStand(val1,val2,val3,val4):
		SnowStand['stand0']=val1
		SnowStand['stand1']=val2
		SnowStand['stand2']=val3
		SnowStand['stand2']=val4

	def setRainStand(val1,val2,val3):
		RainStand['stand0']=val1
		RainStand['stand1']=val2
		RainStand['stand2']=val3

