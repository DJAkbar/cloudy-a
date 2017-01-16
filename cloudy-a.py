#!/usr/bin/python
# -*- coding: UTF-8 -*-
#insert the WeatherUnderground API-key here:
wunder_api = ""
#insert the location for the forecast here. For example "Germany/Berlin"
location = ""
#this decides when it is time to display the forecast for the next day. If you want to show always the forecast for the day, set it to 24:
switch_time = 12

import urllib2
import json
import sys
import time
import pigpio
import random
pi = pigpio.pi()

myweather = json.load(urllib2.urlopen('http://api.wunderground.com/api/' + wunder_api + '/forecast/q/' + location + '.json'))
myweather_sum = myweather['forecast']['simpleforecast']['forecastday']
conditions = {"cloudy" : "cloudy", "nt_cloudy" : "cloudy", "fog" : "cloudy", "nt_fog" : "cloudy", "hazy" : "cloudy", "nt_hazy" : "cloudy", "mostlycloudy" : "cloudy", "nt_mostlycloudy" : "cloudy", "partlycloudy" : "cloudy", "nt_partlycloudy" : "cloudy", "clear" : "sunny", "nt_clear" : "sunny", "sunny" : "sunny", "nt_sunny" : "sunny", "mostlysunny" : "sunny", "nt_mostlysunny" : "sunny", "partlysunny" : "sunny", "nt_partlysunny" : "sunny", "chanceflurries" : "snowy", "nt_chanceflurries" : "snowy", "flurries" : "snowy", "nt_flurries" : "snowy", "chancesnow" : "snowy", "nt_chancesnow" : "snowy", "snow" : "snowy", "nt_snow" : "snowy", "chancerain" : "rainy", "nt_chancerain" : "rainy", "chancesleet" : "rainy", "nt_chancesleet" : "rainy", "sleet" : "rainy", "nt_sleet" : "rainy", "rain" : "rainy", "nt_rain" : "rainy", "tstorms" : "stormy", "nt_tstorms" : "stormy", "chancetstorms" : "stormy", "nt_chancetstorms" : "stormy"}
# conditions (=programs) can be: cloudy, sunny, snowy, rainy, stormy

#These are the different animations for the LED-strips:
def rain():
	for rain_i in range(180):
		blueishness1=255
		blueishness2=0
		fadetimeblue=random.uniform(0.02,0.06)
		pi.set_PWM_dutycycle(17,0)
		pi.set_PWM_dutycycle(24,0)
		pi.set_PWM_dutycycle(26,0)
		pi.set_PWM_dutycycle(13,0)
	
		while blueishness1 !=0 and blueishness2 !=255:
			blueishness1=blueishness1-1
			blueishness2=blueishness2+1
			time.sleep(fadetimeblue)
			pi.set_PWM_dutycycle(22,blueishness1)
		        pi.set_PWM_dutycycle(12,blueishness2)
		time.sleep(random.uniform(0.1,2))
		while blueishness1 !=255 and blueishness2 !=0:
	                blueishness1=blueishness1+1
	                blueishness2=blueishness2-1
	                time.sleep(fadetimeblue)
	                pi.set_PWM_dutycycle(22,blueishness1)
	                pi.set_PWM_dutycycle(12,blueishness2)
	        time.sleep(random.uniform(0.1,2))

def cloud():
        for cloud_i in range(200):
		whiteness1=255
		whiteness2=0
		fadetimewhite=random.uniform(0.02,0.04)
	
		while whiteness1 != 0 and whiteness2 != 255:
			whiteness1=whiteness1-1
			whiteness2=whiteness2+1
			time.sleep(fadetimewhite)
			pi.set_PWM_dutycycle(13,whiteness1)
			pi.set_PWM_dutycycle(26,whiteness1)
			pi.set_PWM_dutycycle(12,whiteness1)
	                pi.set_PWM_dutycycle(17,whiteness2)
		        pi.set_PWM_dutycycle(24,whiteness2)
			pi.set_PWM_dutycycle(22,whiteness2)
		time.sleep(random.uniform(0.5,1))
		while whiteness1 != 255 and whiteness2 != 0:
	                whiteness1=whiteness1+1
	                whiteness2=whiteness2-1
	                time.sleep(fadetimewhite)
	                pi.set_PWM_dutycycle(13,whiteness1) 
	                pi.set_PWM_dutycycle(26,whiteness1)
	                pi.set_PWM_dutycycle(12,whiteness1)
	                pi.set_PWM_dutycycle(17,whiteness2)
	                pi.set_PWM_dutycycle(24,whiteness2)
	                pi.set_PWM_dutycycle(22,whiteness2)
	        time.sleep(random.uniform(0.5,1))

def sun():
        for sun_i in range(140):
		yellowness1=255
		yellowness2=0
		fadetimeyellow=random.uniform(0.05,0.06)
		pi.set_PWM_dutycycle(22,0)
		pi.set_PWM_dutycycle(12,0)

		while yellowness1 != 0 and yellowness2 != 255:
			yellowness1=yellowness1-1
			yellowness2=yellowness2+1
			time.sleep(fadetimeyellow)
			pi.set_PWM_dutycycle(13,(yellowness1/5))
			pi.set_PWM_dutycycle(26,yellowness1)
	                pi.set_PWM_dutycycle(17,yellowness2)
		        pi.set_PWM_dutycycle(24,(yellowness2/5))
		time.sleep(random.uniform(0.1,0.5))
		while yellowness1 != 255 and yellowness2 != 0:
	                yellowness1=yellowness1+1
	                yellowness2=yellowness2-1
	                time.sleep(fadetimeyellow)
	                pi.set_PWM_dutycycle(13,(yellowness1/5))
	                pi.set_PWM_dutycycle(26,yellowness1)
	                pi.set_PWM_dutycycle(17,yellowness2)
	                pi.set_PWM_dutycycle(24,(yellowness2/5))
	        time.sleep(random.uniform(0.1,0.5))


bright=0
brightnew=0
brightnew2=0
bright2=0
fadetime=0
fadetime2=0
def snow():
        for snow_i in range(700000):
		global bright
		global brightnew
		global brightnew2
		global bright2
		global fadetime
		global fadetime2
		start=random.randint(1,100)
		if start==1 and bright==0:
			brightnew=200
			if bright==0:
			       	fadetime=random.uniform(0.002,0.0025)
			else:
				pass
		elif start==2 and bright2==0:
			brightnew2=200
			if bright2==0:
		       		fadetime2=random.uniform(0.002,0.0025)
			else:
				pass
		else:
			pass
		if brightnew > bright and bright < 244:
			bright=bright+1
		elif brightnew == bright:
			brightnew=0
		elif brightnew < bright and bright !=0:
			bright=bright-1
		else:
			pass
	        if brightnew2 > bright2 and bright2 < 244:
	                bright2=bright2+1
	        elif brightnew2 == bright2:
	                brightnew2=0
	        elif brightnew2 < bright2 and bright2 !=0:
	                bright2=bright2-1
	        else:
	                pass
		pi.set_PWM_dutycycle(17, bright+55)
	        pi.set_PWM_dutycycle(22, bright+55)
	        pi.set_PWM_dutycycle(24, bright+55)
	        time.sleep(fadetime)
		pi.set_PWM_dutycycle(26, bright2+55)
	        pi.set_PWM_dutycycle(12, bright2+55)
	        pi.set_PWM_dutycycle(13, bright2+55)
	        time.sleep(fadetime2)

def flash():
        for flash_i in range(400000):
		global bright
		global brightnew
		global brightnew2
		global bright2
		global fadetime
		global fadetime2
		start=random.randint(1,210)
		if start==1:
			brightnew=random.randint(51,255)
			if bright==0:
		        	fadetime=random.uniform(0.002,0.006)
			else:
				pass
		elif start==2:
			brightnew2=random.randint(51,255)
			if bright2==0:
		       		fadetime2=random.uniform(0.002,0.006)
			else:
				pass
		else:
			pass
		if bright+brightnew<255:
			bright=bright+brightnew
			brightnew=0
		else:
			pass	
		if bright2+brightnew2<255:
			bright2=bright2+brightnew2
			brightnew2=0
		else:
			pass
		pi.set_PWM_dutycycle(17, bright)
	        if bright>50:
	                pi.set_PWM_dutycycle(22, bright)
	        else:
	                pi.set_PWM_dutycycle(22, 50)
	        pi.set_PWM_dutycycle(24, bright)
	        time.sleep(fadetime)
		if bright !=0:
			bright=bright-1
		else:
			pass

		pi.set_PWM_dutycycle(26, bright2)
	        if bright2>50:
	                pi.set_PWM_dutycycle(12, bright2)
	        else:
	                pi.set_PWM_dutycycle(12, 50)
	        pi.set_PWM_dutycycle(13, bright2)
	        time.sleep(fadetime2)
			
		if bright2 !=0:
			bright2=bright2-1
		else:
			pass

if int(time.strftime("%H")) < int(switch_time):
	ampm = 1
else:
	ampm = 2

#this executes the main loop. E.g. it is looking for the conditions and decides for the animation that should be displayed:
def main_loop():
    while 1:
		try:
			for period in myweather_sum:
				if period['period'] == ampm:
					orig_conditions = period['icon']
			prog = conditions[orig_conditions]
		except:
			time.sleep(10)
#      for period in myweather_sum:
#       if period['period'] == ampm:
#          orig_conditions = period['icon']
#      prog = conditions[orig_conditions]

		if  prog=="rainy":
			rain()
		elif prog=="cloudy":
			cloud()
		elif prog=="sunny":
			sun()
		elif prog=="snowy":
			snow()
		elif prog=="stormy":
			flash()
		else:
			while 1:
				pi.set_PWM_dutycycle(26, 200)
				time.sleep(1)
				pi.set_PWM_dutycycle(17, 200)
				time.sleep(1)

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
