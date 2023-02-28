#Visual stimulation for calcium imaging experiment
#Used in the paper: Zaupa M., Nagaraj N., Baier H., Sawamiphak S., Filosa A.; "The Calmodulin-interacting peptide Pcp4a regulates feeding-state-dependent behavioral choice in zebrafish"
#Code written by Alessandro Filosa
 

import os
from psychopy import visual, event, core
from psychopy.hardware import labjacks
from psychopy.hardware.labjacks import u3

#Setting up U3 parameters
d = u3.U3()

d.configIO(FIOAnalog = 15) #Setting FI0 as analog inputs

AIN0_REGISTER = 0 # Setting AIN0 = 0volts

#Trigger from labjack (not needed when used with other external trigger)
#DAC0_REGISTER = 5000
#DAC1_REGISTER = 5002
#d.writeRegister(DAC1_REGISTER, 5.0)

#Create window for visual stimulation
win = visual.Window(size=(800,600), units = 'pix', screen = 1, fullscr = True, color = 'grey') # Set the window
x = -400 # initial positions
y = 0

# Reading voltage on AIN0
trigsig = d.readRegister(AIN0_REGISTER) 

if trigsig <1:
    while trigsig < 1:
        trigsig=d.readRegister(AIN0_REGISTER)

#Display circles
if trigsig >1:
    core.wait(4)
    #20deg circle
    circle1 = visual.Circle(win, radius = 190, fillColor= 'black', lineColor= 'black')
    while x < 700: # draw moving stimulus
        x += 2 # make circle constantly move rightwards
        circle1.pos = [x, y] # directly update both x *and* y
        circle1.draw()
        win.flip()
    core.wait (4)
    x = -400 # initial positions
    y = 0
    # 5deg circle
    circle2 = visual.Circle(win, radius = 47, fillColor= 'black', lineColor= 'black')
    while x < 700: # draw moving stimulus
        x += 2 # make circle constantly move rightwards
        circle2.pos = [x, y] # directly update both x *and* y
        circle2.draw()
        win.flip() # make the drawn things visible
    core.wait (4)
    x = -400 # initial positions
    y = 0
    # 1deg circle
    circle3 = visual.Circle(win, radius = 10, fillColor= 'black', lineColor= 'black')
    while x < 700: # draw moving stimulus
        x += 2 # make circle constantly move rightwards
        circle3.pos = [x, y] # directly update both x *and* y
        circle3.draw()
        win.flip() # make the drawn things visible
    core.wait (4)
    x = -400 # initial positions
    y = 0
    # 10deg circle
    circle4 = visual.Circle(win, radius = 95, fillColor= 'black', lineColor= 'black')
    while x < 700: # draw moving stimulus
        x += 2 # make circle constantly move rightwards
        circle4.pos = [x, y] # directly update both x *and* y
        circle4.draw()
        win.flip() # make the drawn things visible
    core.wait (4)
    x = -400 # initial positions
    y = 0
    # 3deg circle
    circle5 = visual.Circle(win, radius = 29, fillColor= 'black', lineColor= 'black')
    while x < 700: # draw moving stimulus
        x += 2 # make circle constantly move rightwards
        circle5.pos = [x, y] # directly update both x *and* y
        circle5.draw()
        win.flip() # make the drawn things visible
    core.wait (4)
    x = -400 # initial positions
    y = 0
    # 30deg circle
    circle5 = visual.Circle(win, radius = 280, fillColor= 'black', lineColor= 'black')
    while x < 700: # draw moving stimulus
        x += 2 # make circle constantly move rightwards
        circle5.pos = [x, y] # directly update both x *and* y
        circle5.draw()
        win.flip() # make the drawn things visible
    core.wait (4)
    ##x = -400 # initial positions
    ##y = 0
    ##circle6 = visual.Circle(win, radius = 340, fillColor= 'grey', lineColor= 'grey')
    ##while x < 440: # draw moving stimulus
        ##x += 2 # make circle constantly move rightwards
        ##circle6.pos = [x, y] # directly update both x *and* y
        ##circle6.draw()
        ##win.flip() # make the drawn things visible