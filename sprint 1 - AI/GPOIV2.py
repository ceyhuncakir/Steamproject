import time
from gpiozero import LED, Button
from signal import pause
import threading

# Importent funcions to use: led(position, onoroff) and RGBledupdate(pos, r, *args), servo() en afstandsensor() [geeft cm terug]
# voor de knop pas buttonpressed() en buttonlose() aan

class TiContainer:
    def __init__(self):
        # defining the pins for the schuifregister
        self.Clock = LED(18)
        self.SerialIn = LED(4)
        self.Latch = LED(27)
        # defining the pins for the Led strip
        self.clockneo = LED(22)
        self.Serialneo = LED(23)
        # defining the pin for the button
        self.button = Button(17)
        # defining the pin voor de servo
        self.servopin = LED(21)
        # defining the pins voor de afstand sensor
        self.trigger = LED(25)
        self.echo = Button(24)

        # variable for storing info about the leds
        self.ledsave = [0, 0, 0, 0, 0, 0, 0, 0]
        self.neosave = [[0, 0, 0] for x in range(8)]

        # name to RGB dictionairy, fell free to add more colors for faster calls.
        self.colours = dict(red=[0, 0, 255], orange=[0, 50, 255], yellow=[0, 100, 255], green=[0, 255, 0],
                       lblue=[255, 255, 0],
                       blue=[255, 0, 0], purple=[255, 0, 255], white=[255, 255, 255], black=[0, 0, 0])

        # defenitie wat er gebeurd als de knop word ingedrukt

    def buttonpressed(self):
        self.fullcontrol([0, 1, 0, 1, 0, 1, 0, 1])

    # defenitie wat er gebeurd als de knop word los gelaten
    def buttonlose(self):
        self.fullcontrol([1, 0, 1, 0, 1, 0, 1, 0])

    # ----------------------------------------------------------------------------------------------------------------------
    # alles hier onder is voor het schuifregister, en die acht leds, tot waar aangegeven.
    # ----------------------------------------------------------------------------------------------------------------------
    # Defenition to update the schuifregister
    def fullcontrol(self, ledlist):
        self.Clock.off()  # starting off in the correct pos
        self.Latch.off()
        for i in ledlist:
            if i:
                self.SerialIn.on()  # make the led on or off
            self.Clock.on()  # advance in the clock
            self.Clock.off()
            self.SerialIn.off()  # turn the led off (if needed)
        self.Latch.on()  # update the leds
        self.Latch.off()

    # defenition that stores what leds are on and off and allows individual led control
    def led(self, position, onoroff):
        if onoroff == "on":  # allow for both textual with "on" and "off" and numeral with 1 and 0
            self.ledsave[position] = 1
        else:
            if onoroff == "off":
                self.ledsave[position] = 0
            else:
                self.ledsave[position] = onoroff
        self.fullcontrol(self.ledsave)  # update the leds to the correct pos

    # ----------------------------------------------------------------------------------------------------------------------
    # Alles tot hier is schuifregister gerelateerd
    # Alles hier onder is voor de RGB led strip tot waar aangevenen
    # ----------------------------------------------------------------------------------------------------------------------

    # definitie om een binaere split te krijgen van nummers als een lijst
    def binaerisplitter(self, num, bits):
        returnthis = []  # setup de return
        if num < 0:  # voor zorgen dat het nummer geplits kunnen worden
            num *= -1
        if num > 2 ** bits - 1:  # voor zorgen dat het nummer tot 0 gebracht kan worden
            num = 2 ** bits - 1
        for x in range(bits):  # for loop om naar nul te brengen
            if (2 ** (bits - x)) <= num:
                returnthis.append(1)  # een 1 toevoegen aan binaere lijst
                num -= 2 ** (bits - x)  # nummer verkleinen
            else:
                returnthis.append(0)  # een 0 toevoegen aan de binaere lijst
        return returnthis

    # defenitie om de neon led strip kleuren de veranderen en updaten.
    def neoupdate(self):
        self.clockneo.off()  # setup dat alled staat zo als ik denk dat het staat
        self.Serialneo.off()
        for x in range(32):  # de 32 nullen die als reset verstuurd moetten worden
            self.clockneo.on()
            self.clockneo.off()

        for x in self.neosave:  # begin loop van kleuren aan passen
            information = [1, 1, 1, 0, 0, 0, 1, 0]  # instalatie van de eerste 8 bits (standaat felheid 2 can de 32)
            information += self.binaerisplitter(x[0], 8)  # RGB nummers tot een binaere lijst omzetten
            information += self.binaerisplitter(x[1], 8)
            information += self.binaerisplitter(x[2], 8)
            for i in information:  # loop door de 32 bits voor 1 led
                if i:  # kijk of we een 1 moeten versturen
                    self.Serialneo.on()
                self.clockneo.on()  # klok de klok een stap verder
                self.clockneo.off()
                self.Serialneo.off()  # reset de serial output

    def RGBledupdate(self, pos, r, *args):
        if len(args) == 0:
            self.neosave[pos] = self.colours[r]  # pak de RGB waardes uit de dictionary
        else:
            self.neosave[pos] = [r, args[0], args[1]]  # haal de waardes uit de gegeven RGB waardes
        self.neoupdate()

    # ----------------------------------------------------------------------------------------------------------------------
    # Alles tot hier is RGB led strip gerelateerd
    # Alles hier onder is voor de servo tot waar aangevenen
    # ----------------------------------------------------------------------------------------------------------------------

    # defenition for servo
    def servo(self):  # servo will take less than 0.5 a sec to turn to and from, unfortunately nothing can be prossesed at the same time
        self.servopin.on()
        time.sleep(0.0004)  # angle 0
        self.servopin.off()
        time.sleep(0.4)
        self.servopin.on()
        time.sleep(0.0023)  # angle 180
        self.servopin.off()

    # ----------------------------------------------------------------------------------------------------------------------
    # Alles tot hier is servo gerelateerd
    # Alles hier onder is voor de afstand sensor tot waar aangevenen.
    # ----------------------------------------------------------------------------------------------------------------------

    def afstandsensor(self):
        self.trigger.on()
        time.sleep(0.000001)
        self.trigger.off()

        self.echo.wait_for_inactive(1)
        time1 = time.time()
        self.echo.wait_for_active(0.02)
        time2 = time.time()
        return round(17165 * (time2 - time1), 1)

    # ----------------------------------------------------------------------------------------------------------------------
    # Alles tot hier is afstand sensor gerelateerd
    # Alles hier onder is voor testen en een paar dingen resetten.
    # ----------------------------------------------------------------------------------------------------------------------


ti_class = TiContainer()
ti_class.fullcontrol([0, 0, 0, 0, 0, 0, 0, 0])

#   neoupdate()   ???

ti_class.button.when_pressed = ti_class.buttonpressed()
ti_class.button.when_released = ti_class.buttonlose



#  pause()