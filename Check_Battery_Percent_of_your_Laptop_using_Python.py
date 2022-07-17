print('\n'"***Laptop battery check ***"'\n')
import psutil

battery = psutil.sensors_battery()
#Dic with points to check
battery_status = {
    'percent_battery': battery.percent,#=> we can replace the battery.percent value for any number in order to simulate the process.
    'power_plugged':battery.power_plugged
}
battery_porcentage = [range(1,100)]

def check_battery_percent():
    for porcentage in battery_porcentage:
          # Battery = 100%
        if battery_status['percent_battery'] == 100:

            print(f"Fully charged {battery_status['percent_battery']}%.", end = "")  
            # check if the laptop is plugged with 100%  
                  
            if battery_status['power_plugged'] == True:        
                print("**Please unplugged the battery.**"'\n')
            else:
                print("Great!! the battery is unplugged.")   

            #check if battery porcent is in range(1,99)% and if plugged.         
        elif battery_status['percent_battery'] in porcentage and battery_status['percent_battery']:      
            print(f" Battery status: {battery_status['percent_battery']}%.", end = "")
            
            if battery_status['power_plugged'] == True:
                print("remaining (plugged in)."'\n')
  
            else:
                print("laptop is unplugged"'\n')
        
check_battery_percent()    
        
        
            

         
        
    
 
    

        
        
    
        
            

   
    
      
        








