# cloudy-a
A simple script for light animations for two LED strips according to the weather forecast. For an example see [Youtube](https://www.youtube.com/watch?v=DNXssI4LuMc)  
Instructions for use: 
Here is a short write-up of some instructions to make your own DIY weather forecast cloud lamp.  
I have done this with a Raspberry Pi 3 since there were no Pi Zero’s to be bought anywhere. But since this is probably a bit overkill for this project and right now they seem to be in stock again I would recommend trying this with a Raspberry Pi Zero. If you do, make sure to let us know if it’s working! This tutorial will reference other tutorials as well, since I do not see the need to write again something others have described in a much better way than me.
Some things should be set-up already:  
+ Python and pigpio installed on the Raspberry Pi  
+ An internet connection (if you’re not using WIFI make sure to have a cable that’s long enough)  
+ A WeatherUnderground API key and your location to append the link for the request. For more information see [here](https://github.com/InitialState/wunderground-sensehat/wiki/Part-1.-How-to-Use-the-Wunderground-API) 
*Dark Sky is now suggested as a free alternative for Weather Underground

So what do you need:  
+ Raspberry Pi (obviously)  
+ Internet connectivity (also obvious)  
+ RGB LED-strip with 3 Pins for RGB and 1 Strip for 12 V (I have used a length of 3m but shorter is also fine depending of how much of the strip you want to use)  
+ A 12 V power supply for the LED strip (if you buy the LED strip in a complete pack it should come with a fitting power supply). I have bought the following [strip](https://www.conrad.de/de/led-streifen-komplettset-mit-stecker-12-v-300-cm-rgb-paul-neuhaus-1199-70-1093382.html)  
+ A breadboard or perfboard (for the second option you’ll of course need a soldering iron too, I recommend this since it’s a bit more permanent and also saves space)
+ Some jumper wires (male to male, male to female)  
+ Six MOSFETs (IRLZ34N)  
+ A power jack that fits the 12 V power supply of the LED strip  
+ Multiple socket strip (with at least two sockets, I used one with three sockets because they are more common). I have chosen a lenght of 5 meters, just keep in mind it has to run up to the ceiling, along the ceiling and then to the power outlet.  
For the lamp itself I recommend the following:  
+ A 5 liter plastic bottle (or a similarly big container of see-through material. Some people are using these IKEA paper lanterns but I do not recommend them since they could theoretically burn)  
+ Cotton batting. For the 5 liter bottle I needed about 100g, i have SO much left over now! I have used [this](https://www.idee-shop.com/shop/de/dieprodukte/Basteln/Bastelmaterial/FuellmaterialFell/Fuellwatteweiss250g.html)  
+ Some fishing line (clear string might work too but keep in mind that it will be a bit heavy in the end)  
+ A glue gun or similar to attach the batting to the bottle  
+ A hook for your ceiling  
This seems to be a lot of stuff at first glance. But I didn’t have any of this just lying around and still managed to stay well under 150 € with this project (including the Raspberry Pi 3). If you’re using a Raspberry Pi Zero or do have a Pi lying around you will not spend more than 100 €).  

Ok, so what do you need to do? This:  
+ Start by cutting the LED strip to lenght. I used one strip of two segments (with 3 LEDs each) and one of three segments. But I recommend to use a bit more. 4 and 5 segments should be fine I think. I think having a longer and a shorter segment helps the effect since it gives it a bit of “imbalance”.  
+ Set up two circuits according to this [Tutorial](http://popoklopsi.github.io/RaspberryPi-LedStrip/#!/)
+ To tweak the above tutorial for two strips you should keep two things in mind: first you will need a common ground for all the MOSFETs. But the 12 V should run directly from the end of the first strip to the beginning of the second. I have used jumper cables soldered to the strips and the perfboard, but any kind of cable should work.  
+ The GPIO-pins should be connected as follows (one half follows the above tutorial; I will call them Strip A and Strip B here):  
+ Red A: GPIO 17, Blue A: GPIO 22, Green A: 24  
+ Red B: GPIO 26, Blue B: GPIO 12, Green B: 13  
+ Now is a good moment to plug in the Raspberry Pi and the 12 V power supply. Use the multiple socket strip because they should run on the same power cord. Keep the cables as short as possible. I just rolled them up and bound them together. Some people say you should not do this, I guess with such low Voltages there is no risk but be aware that I can not be held responsible if anything goes wrong with your electronics)  
+ To test the LEDs you should open a terminal and type the following “sudo pigpiod”, press enter and then “pigs p 26 255 p 13 255 p 12 255 p 17 255 p 22 255 p 24 255”. When you press enter again, both LED strips should be completely white. If it doesn’t work please check if you connected everything correctly. You can try out other colours by changin the value 255 to something else. Experiment a bit, expecially how to get a good yellow. I suspect that the correct values for yellow change from strip to strip.  
+ Now we’ll have a look at the code. In the beginning you will have to insert the API key you got earlier from WeatherUndergound and the location for appending the link of the request. You can also decide at which time the lamp should display the forecast for the next day by changing the number of the variable switch_time (if you always want to display the weather for the moment just set it to 24).  
+ If you fill in all the variables correctly we are already done here. To see if you have the correct data for it, insert it in the according places here and check this [link](http://api.wunderground.com/api/ API-KEY /forecast/q/ LOCATION .json)  
+ I recommend trying this first because if something is not working, the problem lies probably in the weather forecast request.  
+ It’s all working and you can see a text forecast for your location? Good, then we will install the code on the Pi now. For this you just have to copy it into the home/pi (or whatever is your username) folder of your Pi and safe it as cloudy-a.py (do this by the method you prefer, either by ssh or directly with a USB stick for example) and run “sudo chmod +x cloudy-a.py” while being in that folder.  
+ Now is probably a good time to see if we can get some lights, eh? Run the code with “sudo pigpiod” followed by “python cloudy-a.py”. When you have been sufficiently blinded by the LEDs, press CTRL-C to stop.  
+ If you are happy with starting the script every time manually, you can skip the next few steps and start building the actual lamp.But who wants to do that, right? So on we go:  
+ Create a new file in the home/pi (again: or whatever is your username) directory: navigate to the folder in the terminal and type “sudo nano launcher.sh” You will have created a new file where you should write the following:  
    #!/bin/sh  
    launcher.sh  
	    cd /  
	    cd home/pi  
	    sudo python cloudy-a.py  
	    cd /  
+ We now have to set up rules that this file is executed on every startup. For that you type in the terminal “sudo crontab -e”. At the end of the file insert the following two lines:  
	    @reboot /usr/bin/pigpiod  
	    @reboot sleep 15 && /home/pi/launcher.sh   
+ Of course if your username is not pi, change accordingly.The “sleep 15” is a lazy work-around to wait for an internet connection. There are much better ways to do this, but it works fine for me. I am of course open for suggestions!  
+ Close the file with CTRL-X and restart with “sudo reboot”. Now the LED strips should light up according to the weather forecast already. We are finally ready to build the lamp!  
+ As I said before I had to experiment around a bit to get a good yellow. I have settled for a ratio of red to green of 1:5. This might not get you the best results. If you want to change it, navigate to the function sun() and change the settings for pin 24 and 13.  
To make the lamp there are actually quite a lot of good tutorials, I just chose this one because it resembles most closely my own process and uses the same kind of [container](
https://www.youtube.com/watch?v=y5bo0-kV5Jo)  
Just some notes: When you finished the lamp, put the Raspberry Pi, the breadboard or perfboard and the LED-strips all in and have everything attached to the multiple socket strip. This should be the only cable that comes out of the lamp. As I said before, I used a (more or less) rectangular clear 5 liter bottle. I cut three sides of it open just where it reaches the biggest diameter under the opening. On the side opposite to the attached side I also made a hole for the power cord. Then I made another hole in the exact middle of the bottom (a soldering iron can help here!) and put the fishing line through that and the hole at the top of the bottle. Then I put it on a hook, put the power cord in the hook and attached the fishing line to it too. Since the fishing line is a bit shorter the lamp is automatically closed the the tension of the weight.  

Then I bought a cheap timeclock because I don’t want the lamp to be switched on all the time, but obviusly this is up to you. The program is set up so that it will finish the cycle of animation about every hour. It will then check for the forecast again and start the according animation. Because I did’t want to bring multithreadinf into the project I have set the cycles of the animations to the number of iterations. Since a lot of these depend on randomly generated cycles, it will never be an exact hour. If you need to check for the real weather forecast every hour, you will have to change the code yourself.  

Anyway, now everything should be finished and you have a working weather forecast cloud lamp. I want to stress again that I can not be held responsible for any damages of injuries that might occur in the making or running of this project. Of course I can also not guarantee that it will work for you even if you follow all the steps correctly. I am not a programmer and the code is probably quite messy and ineficcient. If you have suggestions I would be happy to hear them. I will try to answer questions but don’t count on it. Now I would be very happy to see your creations!  
