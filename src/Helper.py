# from Battery import *
# from Led import *
from Servo import *
import time


class Helper:
    def __init__(self):
        # self.adc=ADS7830()
        self.led=Led()
        self.servo=Servo()
        self.battery_voltage=[8.4,8.4,8.4,8.4,8.4]
        self.colorWipeMap = { 
            'red' : (255, 0, 0), 
            'green' : (0, 255, 0),
            'blue' : (0, 0, 255),
            'white' : (255, 255, 255),
            'off' : (0, 0, 0 )
        }

    # def getBattery(self):
    #     try:
    #         while True:
    #             Power=self.adc.readAdc(0)/255.0*5.0*3
    #             print ("The battery voltage is "+str(Power)+"V")
    #             time.sleep(1)
    #             print ('\n')
    #     except KeyboardInterrupt:
    #         print ("\nEnd of program")

    # def measuring_voltage(self,connect):
    #     try:
    #         for i in range(5):
    #             self.battery_voltage[i]=round(self.adc.power(0),2)
    #         return str(max(self.battery_voltage))
    #     except Exception as e:
    #         print(e)

    # def ledColorWipe(self):
    #     #Red wipe
    #     print ("\nRed wipe")
    #     self.led.colorWipe(self.led.strip, Color(255, 0, 0)) 
    #     time.sleep(1)
    #     #Green wipe
    #     print ("\nGreen wipe")
    #     self.led.colorWipe(self.led.strip, Color(0, 255, 0)) 
    #     time.sleep(1)
    #     #Blue wipe
    #     print ("\nBlue wipe")
    #     self.led.colorWipe(self.led.strip, Color(0, 0, 255)) 
    #     time.sleep(1)
    #     #White wipe
    #     print ("\nWhite wipe")
    #     self.led.colorWipe(self.led.strip, Color(255, 255, 255)) 
    #     time.sleep(1)
    #     self.led.colorWipe(self.led.strip, Color(0, 0, 0))   #turn off the light
    #     print ("\nEnd of program")


    def test_Servo(self):
        self.servo.setServoAngle(0,90)
        time.sleep(1)
        self.servo.setServoAngle(0,0)
