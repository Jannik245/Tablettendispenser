
# Import Bibliotheken
import machine
# import st7789
import utime
# import vga1_bold_16x32 as font
from machine import Pin
import time
from time import sleep
import network
import webrepl
import os



#wifi connecion setup
wifi = network.WLAN(network.AP_IF) #access point = AP, station mode = STA
wifi.active(True)
wifi.config(essid='ESP 32',password='12345678',authmode=network.AUTH_WPA_WPA2_PSK) 
webrepl.start(password="12345678")



#txt file setup
files = os.listdir()

for file in files:
    print(file)

filename = "Medikamente.txt"

try:
    with open("Medikamente.txt", "r") as file:
        words = []
        for line in file:
            line_words = line.strip().split()
            words.extend(line_words)
        print(words)
    # with open(filename, "r") as f:
    #     contents = f.read()
    #     print("Inhalt der Datei:")
    #     Daten = contents
    #     print(Daten) #Text Datei
    #     #Medikamente durch "," getrennt in Liste schreiben
    #     list = [] 
    #     for line in Daten:
    #         data = line.strip.split(';') 
    #         list.append(data)    
    # print(list)
except OSError:
    print("Datei konnte nicht geöffnet werden.")




#Stepper Motor Setup
IN1 = Pin(26,Pin.OUT)
IN2 = Pin(25,Pin.OUT)
IN3 = Pin(33,Pin.OUT)
IN4 = Pin(32,Pin.OUT)
pins = [IN1, IN2, IN3, IN4]
sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
def step(pins, seq):
    for i in range(len(pins)):
        pins[i].value(seq[i])

a_motor=0
befüllung_counter=0


#Alarm setup
alarm_counter=0
p23 = machine.Pin(21,machine.Pin.OUT)

B0  = 31
C1  = 33
CS1 = 35
D1  = 37
DS1 = 39
E1  = 41
F1  = 44
FS1 = 46
G1  = 49
GS1 = 52
A1  = 55
AS1 = 58
B1  = 62
C2  = 65
CS2 = 69
D2  = 73
DS2 = 78
E2  = 82
F2  = 87
FS2 = 93
G2  = 98
GS2 = 104
A2  = 110
AS2 = 117
B2  = 123
C3  = 131
CS3 = 139
D3  = 147
DS3 = 156
E3  = 165
F3  = 175
FS3 = 185
G3  = 196
GS3 = 208
A3  = 220
AS3 = 233
B3  = 247
C4  = 262
CS4 = 277
D4  = 294
DS4 = 311
E4  = 330
F4  = 349
FS4 = 370
G4  = 392
GS4 = 415
A4  = 440
AS4 = 466
B4  = 494
C5  = 523
CS5 = 554
D5  = 587
DS5 = 622
E5  = 659
F5  = 698
FS5 = 740
G5  = 784
GS5 = 831
A5  = 880
AS5 = 932
B5  = 988
C6  = 1047
CS6 = 1109
D6  = 1175
DS6 = 1245
E6  = 1319
F6  = 1397
FS6 = 1480
G6  = 1568
GS6 = 1661
A6  = 1760
AS6 = 1865
B6  = 1976
C7  = 2093
CS7 = 2217
D7  = 2349
DS7 = 2489
E7  = 2637
F7  = 2794
FS7 = 2960
G7  = 3136
GS7 = 3322
A7  = 3520
AS7 = 3729
B7  = 3951
C8  = 4186
CS8 = 4435
D8  = 4699
DS8 = 4978


def play(pin, melodies, delays, duty):
    pwm=machine.PWM(pin)
    for note in melodies:
        pwm.freq(note)
        pwm.duty(duty)
        time.sleep(delays)
        if button_right_Wochenbetrieb.state == True: 
            break
        
    pwm.duty(0)
    pwm.deinit() #deinitalise


mario = [
     E7, E7,  1, E7,  1, C7, E7,  1,
     G7,  1,  1,  1, G6,  1,  1,  1,
     C7,  1,  1, G6,  1,  1, E6,  1,
      1, A6,  1, B6,  1,AS6, A6,  1,
     G6, E7,  1, G7, A7,  1, F7, G7,
      1, E7,  1, C7, D7, B6,  1,  1,
     C7,  1,  1, G6,  1,  1, E6,  1,
      1, A6,  1, B6,  1,AS6, A6,  1,
     G6, E7,  1, G7, A7,  1, F7, G7,
      1, E7,  1, C7, D7, B6,  1,  1,
]


def play_mario():
    play(p23, mario, 0.15, 50)


    
#Display Setup
# def setup_display() -> st7789.ST7789:
#     """
#     Set the display up.
#     The driver library can be found here: https://github.com/russhughes/st7789_mpy
#     The board specs can be found here: http://www.lilygo.cn/prod_view.aspx?TypeId=50062&Id=1400&FId=t3:50062:3

#     :return: Display instance.
#     """
#     spi = machine.SPI(1, baudrate=30000000, polarity=1,
#                       sck=machine.Pin(18), mosi=machine.Pin(19))
#     device = st7789.ST7789(spi, 135, 240,
#                            reset=machine.Pin(23, machine.Pin.OUT), cs=machine.Pin(5, machine.Pin.OUT),
#                            dc=machine.Pin(16, machine.Pin.OUT), backlight=machine.Pin(4, machine.Pin.OUT),
#                            rotations=[(0x00, 240, 320, 0, 0), (0x60, 320, 240, 0, 0), (0xc0, 240, 320, 0, 0), (0xa0, 320, 240, 0, 0)],
#                            rotation=1, options=1)
                           
#     device.init()
#     device.inversion_mode(True)
#     device.sleep_mode(False)

#     return device



#Buttons Class Setup
class Button:
    def __init__(self, pin_number: int, inverted: bool) -> None:
        """
        This class creates an instance of a button.
        :param pin_number: Hardware pin number.
        :param inverted: Changes the logic from active low to active high.
        """
        self._pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_UP)
        self._inverted = inverted

    @property
    def state(self) -> bool:
        return not bool(self._pin.value()) if self._inverted else bool(self._pin.value())



#Main Code
#Display setup einlesen und dessen Button deklarieren
# display = setup_display()
button_left_Befüllung = Button(18, True)
button_right_Wochenbetrieb = Button(19,True)

#display layout einstellungen setzen
# display.on()
# display.rect(0, 0, 135, 240, st7789.BLACK)
# print(f"Display: h={display.height()}px, w={display.width()}px")
# y_index = 11


#Display ausgabe Wochentage
days_of_week = ["TAG:Montag       ", "TAG:Dienstag     ","TAG:Mittwoch  ", "TAG:Donnerstag   ","TAG:Freitag      ","TAG:Samstag      ","TAG:Sonntag      "]
current_day = 6


#Tageswechsel 
while True:
    #Befüllung
    if button_left_Befüllung.state == True:
        # current_day = (current_day + 1) %7

        # display.text(font, words[current_day], 40, 110)
        # #display.text(font, data_str, 100, 110)
        #utime.sleep(1)
        for x in range (74):
            for step in sequence: 
                for i in range(len(pins)):
                    pins[i].value(step[i])
                    a_motor=a_motor+1
                    sleep(0.001)
                    if a_motor==1165:
                        a_motor=0


            x=x+1
            if x==72:
                befüllung_counter=befüllung_counter+1
                if befüllung_counter==7:
                    time.sleep (5) #24h eigentlich (=86400 Sekunden)
                    for i in range (4):
                        play_mario()
                        if button_right_Wochenbetrieb.state == True:
                            break



    #Wochenbetrieb
    elif button_right_Wochenbetrieb.state == True: 
        # current_day = (current_day + 1) %7

        # display.text(font, days_of_week[current_day], 100, 110)
        # #display.text(font, data_str, 100, 110)
        # #utime.sleep(1)


        for x in range (74):
            for step in sequence: 
                for i in range(len(pins)):
                    pins[i].value(step[i])
                    a_motor=a_motor+1
                    sleep(0.001)
                    if a_motor==1165:
                        a_motor=0

            x=x+1
            if x==72:
                time.sleep (5) #24h eigentlich (=86400 Sekunden)
                for i in range (4):
                    play_mario()
                    if button_right_Wochenbetrieb.state == True:
                        break
                    
