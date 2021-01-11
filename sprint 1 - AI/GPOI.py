import time
from gpiozero import LED, Button
from signal import pause

# Importent funcions to use: led(position, onoroff) and RGBledupdate(pos, r, *args) and servo(angle)
# voor de knop pas buttonpressed() en buttonlose() aan

# defining the pins for the schuifregister
Clock = LED(18)
SerialIn = LED(4)
Latch = LED(27)
# defining the pins for the Led strip
clockneo = LED(22)
Serialneo = LED(23)
# defining the pin for the button
button = Button(17)
# defining the pin voor de servo
servopin = LED(21)


# variable for storing info about the leds
ledsave = [0, 0, 0, 0, 0, 0, 0, 0]
neosave = [[0, 0, 0] for x in range(8)]

# name to RGB dictionairy, fell free to add more colors for faster calls.
colours = dict(red=[0, 0, 255], orange=[0, 50, 255], yellow=[0, 100, 255], green=[0, 255, 0], lblue=[255, 255, 0],
               blue=[255, 0, 0], purple=[255, 0, 255], white=[255, 255, 255], black=[0, 0, 0])


# defenitie wat er gebeurd als de knop word ingedrukt
def buttonpressed():
    fullcontrol([0, 1, 0, 1, 0, 1, 0, 1])

# defenitie wat er gebeurd als de knop word los gelaten
def buttonlose():
    fullcontrol([1, 0, 1, 0, 1, 0, 1, 0])


# Defenition to update the schuifregister
def fullcontrol(ledlist):
    Clock.off()  # starting off in the correct pos
    Latch.off()
    for i in ledlist:
        if i:
            SerialIn.on()  # make the led on or off
        Clock.on()  # advance in the clock
        Clock.off()
        SerialIn.off()  # turn the led off (if needed)
    Latch.on()  # update the leds
    Latch.off()


# defenition that stores what leds are on and off and allows individual led control
def led(position, onoroff):
    global ledsave  # get the global storage for the leds
    if onoroff == "on":  # allow for both textual with "on" and "off" and numeral with 1 and 0
        ledsave[position] = 1
    else:
        if onoroff == "off":
            ledsave[position] = 0
        else:
            ledsave[position] = onoroff
    fullcontrol(ledsave)  # update the leds to the correct pos


# definitie om een binaere split te krijgen van nummers als een lijst
def binaerisplitter(num, bits):
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
def neoupdate():
    global neosave  # pak de informatie van de leds, welke kleur ze zouden moetten zijn.
    clockneo.off()  # setup dat alled staat zo als ik denk dat het staat
    Serialneo.off()
    for x in range(32):  # de 32 nullen die als reset verstuurd moetten worden
        clockneo.on()
        clockneo.off()

    for x in neosave:  # begin loop van kleuren aan passen
        information = [1, 1, 1, 0, 0, 0, 1, 0]  # instalatie van de eerste 8 bits (standaat felheid 2 can de 32)
        information += binaerisplitter(x[0], 8)  # RGB nummers tot een binaere lijst omzetten
        information += binaerisplitter(x[1], 8)
        information += binaerisplitter(x[2], 8)
        for i in information:  # loop door de 32 bits voor 1 led
            if i:  # kijk of we een 1 moeten versturen
                Serialneo.on()
            clockneo.on()  # klok de klok een stap verder
            clockneo.off()
            Serialneo.off()  # reset de serial output


def RGBledupdate(pos, r, *args):
    global neosave  # haal de momentele informatie op van de neonleds
    if len(args) == 0:
        neosave[pos] = colours[r]  # pak de RGB waardes uit de dictionary
    else:
        neosave[pos] = [r, args[0], args[1]]  # haal de waardes uit de gegeven RGB waardes
    neoupdate()

def servo(angle):
    servopin.on()
    time.sleep(0.0005+(0.000002*angle))
    servopin.off()

fullcontrol([0, 0, 0, 0, 0, 0, 0, 0])
neoupdate()

button.when_pressed = buttonpressed
button.when_released = buttonlose

servo(30)
# servo(10)
# servo(100)

pause()