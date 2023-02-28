#Visual stimulation for behavioral choice experiment
#Used in the paper: Zaupa M., Nagaraj N., Baier H., Sawamiphak S., Filosa A.; "The Calmodulin-interacting peptide Pcp4a regulates feeding-state-dependent behavioral choice in zebrafish"
#Code written by Alessandro Filosa

import os
from psychopy import visual, event, core

#Create window for visual stimulation
win = visual.Window(size=(1280,1024), units = 'pix', screen = 1, fullscr = True, color = 'white') # Set the window

#Circle radius in pixels

one_deg = 0.5
three_deg = 1.5
five_deg = 2.5
ten_deg = 5
twenty_deg = 10
thirty_deg = 15

#30deg circles
circle1 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle2 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle3 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle4 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle5 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle6 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle7 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle8 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')

circle10 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle20 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle30 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle40 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle50 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle60 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle70 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle80 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')

circle100 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle200 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle300 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle400 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle500 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle600 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle700 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle800 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')

circle1000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle2000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle3000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle4000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle5000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle6000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle7000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle8000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')

circle10000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle20000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle30000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle40000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle50000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle60000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle70000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')
circle80000 = visual.Circle(win, radius = thirty_deg, fillColor= 'black', lineColor= 'black')

#10deg circles
circle1a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle2a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle3a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle4a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle5a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle6a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle7a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle8a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')

circle10a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle20a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle30a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle40a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle50a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle60a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle70a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle80a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')

circle100a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle200a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle300a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle400a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle500a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle600a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle700a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle800a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')

circle1000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle2000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle3000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle4000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle5000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle6000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle7000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle8000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')

circle10000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle20000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle30000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle40000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle50000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle60000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle70000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')
circle80000a = visual.Circle(win, radius = ten_deg, fillColor= 'black', lineColor= 'black')

#5deg circles
circle1b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle2b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle3b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle4b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle5b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle6b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle7b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle8b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')

circle10b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle20b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle30b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle40b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle50b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle60b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle70b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle80b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')

circle100b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle200b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle300b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle400b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle500b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle600b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle700b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle800b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')

circle1000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle2000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle3000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle4000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle5000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle6000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle7000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle8000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')

circle10000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle20000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle30000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle40000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle50000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle60000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle70000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')
circle80000b = visual.Circle(win, radius = five_deg, fillColor= 'black', lineColor= 'black')

#20deg circles
circle1c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle2c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle3c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle4c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle5c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle6c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle7c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle8c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')

circle10c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle20c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle30c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle40c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle50c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle60c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle70c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle80c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')

circle100c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle200c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle300c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle400c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle500c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle600c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle700c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle800c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')

circle1000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle2000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle3000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle4000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle5000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle6000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle7000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle8000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')

circle10000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle20000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle30000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle40000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle50000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle60000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle70000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')
circle80000c = visual.Circle(win, radius = twenty_deg, fillColor= 'black', lineColor= 'black')

#1deg circles
circle1d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle2d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle3d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle4d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle5d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle6d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle7d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle8d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')

circle10d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle20d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle30d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle40d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle50d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle60d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle70d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle80d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')

circle100d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle200d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle300d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle400d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle500d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle600d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle700d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle800d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')

circle1000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle2000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle3000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle4000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle5000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle6000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle7000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle8000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')

circle10000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle20000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle30000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle40000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle50000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle60000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle70000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')
circle80000d = visual.Circle(win, radius = one_deg, fillColor= 'black', lineColor= 'black')

#3deg circles
circle1e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle2e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle3e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle4e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle5e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle6e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle7e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle8e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')

circle10e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle20e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle30e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle40e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle50e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle60e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle70e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle80e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')

circle100e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle200e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle300e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle400e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle500e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle600e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle700e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle800e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')

circle1000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle2000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle3000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle4000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle5000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle6000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle7000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle8000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')

circle10000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle20000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle30000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle40000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle50000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle60000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle70000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')
circle80000e = visual.Circle(win, radius = three_deg, fillColor= 'black', lineColor= 'black')

s = 150 # space between rows of circles

a=0.6 # speed of stimuli

#display 1deg circles

# initial positions of circles
x1 = -1340
x2= -1240
x3= -1140
x4= -1040
x5= -940
x6= -840
x7= -740
x8= -640

y1 = 0
y2 = 30

y1a = y1+s
y2a = y2+s

y1b = y1+2*s
y2b = y2+2*s

y1c = y1-s
y2c = y2-s

y1d = y1-2*s
y2d = y2-2*s

while x1 < 750: # draw moving stimulus
    x1 += a # make circle constantly move rightwards
    x2 += a
    x3 += a
    x4 += a
    x5 += a
    x6 += a
    x7 += a
    x8 += a
    circle1d.pos = [x1, y1] # directly update both x *and* y
    circle2d.pos = [x2, y2]
    circle3d.pos = [x3, y1]
    circle4d.pos = [x4, y2]
    circle5d.pos = [x5, y1]
    circle6d.pos = [x6, y2]
    circle7d.pos = [x7, y1]
    circle8d.pos = [x8, y2]
    circle10d.pos = [x1, y1a] 
    circle20d.pos = [x2, y2a]
    circle30d.pos = [x3, y1a]
    circle40d.pos = [x4, y2a]
    circle50d.pos = [x5, y1a]
    circle60d.pos = [x6, y2a]
    circle70d.pos = [x7, y1a]
    circle80d.pos = [x8, y2a]
    circle100d.pos = [x1, y1b] 
    circle200d.pos = [x2, y2b]
    circle300d.pos = [x3, y1b]
    circle400d.pos = [x4, y2b]
    circle500d.pos = [x5, y1b]
    circle600d.pos = [x6, y2b]
    circle700d.pos = [x7, y1b]
    circle800d.pos = [x8, y2b]
    circle1000d.pos = [x1, y1c] 
    circle2000d.pos = [x2, y2c]
    circle3000d.pos = [x3, y1c]
    circle4000d.pos = [x4, y2c]
    circle5000d.pos = [x5, y1c]
    circle6000d.pos = [x6, y2c]
    circle7000d.pos = [x7, y1c]
    circle8000d.pos = [x8, y2c]
    circle10000d.pos = [x1, y1d] 
    circle20000d.pos = [x2, y2d]
    circle30000d.pos = [x3, y1d]
    circle40000d.pos = [x4, y2d]
    circle50000d.pos = [x5, y1d]
    circle60000d.pos = [x6, y2d]
    circle70000d.pos = [x7, y1d]
    circle80000d.pos = [x8, y2d]
    circle1d.draw()
    circle2d.draw()
    circle3d.draw()
    circle4d.draw()
    circle5d.draw()
    circle6d.draw()
    circle7d.draw()
    circle8d.draw()
    circle10d.draw()
    circle20d.draw()
    circle30d.draw()
    circle40d.draw()
    circle50d.draw()
    circle60d.draw()
    circle70d.draw()
    circle80d.draw()
    circle100d.draw()
    circle200d.draw()
    circle300d.draw()
    circle400d.draw()
    circle500d.draw()
    circle600d.draw()
    circle700d.draw()
    circle800d.draw()
    circle1000d.draw()
    circle2000d.draw()
    circle3000d.draw()
    circle4000d.draw()
    circle5000d.draw()
    circle6000d.draw()
    circle7000d.draw()
    circle8000d.draw()
    circle10000d.draw()
    circle20000d.draw()
    circle30000d.draw()
    circle40000d.draw()
    circle50000d.draw()
    circle60000d.draw()
    circle70000d.draw()
    circle80000d.draw()
    win.flip()
core.wait (5)

#display 3deg circles

# initial positions of circles
x1 = -1340
x2= -1240
x3= -1140
x4= -1040
x5= -940
x6= -840
x7= -740
x8= -640

y1 = 0
y2 = 30

y1a = y1+s
y2a = y2+s

y1b = y1+2*s
y2b = y2+2*s

y1c = y1-s
y2c = y2-s

y1d = y1-2*s
y2d = y2-2*s

while x1 < 750: # draw moving stimulus
    x1 += a # make circle constantly move rightwards
    x2 += a
    x3 += a
    x4 += a
    x5 += a
    x6 += a
    x7 += a
    x8 += a
    circle1e.pos = [x1, y1] # directly update both x *and* y
    circle2e.pos = [x2, y2]
    circle3e.pos = [x3, y1]
    circle4e.pos = [x4, y2]
    circle5e.pos = [x5, y1]
    circle6e.pos = [x6, y2]
    circle7e.pos = [x7, y1]
    circle8e.pos = [x8, y2]
    circle10e.pos = [x1, y1a] 
    circle20e.pos = [x2, y2a]
    circle30e.pos = [x3, y1a]
    circle40e.pos = [x4, y2a]
    circle50e.pos = [x5, y1a]
    circle60e.pos = [x6, y2a]
    circle70e.pos = [x7, y1a]
    circle80e.pos = [x8, y2a]
    circle100e.pos = [x1, y1b] 
    circle200e.pos = [x2, y2b]
    circle300e.pos = [x3, y1b]
    circle400e.pos = [x4, y2b]
    circle500e.pos = [x5, y1b]
    circle600e.pos = [x6, y2b]
    circle700e.pos = [x7, y1b]
    circle800e.pos = [x8, y2b]
    circle1000e.pos = [x1, y1c] 
    circle2000e.pos = [x2, y2c]
    circle3000e.pos = [x3, y1c]
    circle4000e.pos = [x4, y2c]
    circle5000e.pos = [x5, y1c]
    circle6000e.pos = [x6, y2c]
    circle7000e.pos = [x7, y1c]
    circle8000e.pos = [x8, y2c]
    circle10000e.pos = [x1, y1d] 
    circle20000e.pos = [x2, y2d]
    circle30000e.pos = [x3, y1d]
    circle40000e.pos = [x4, y2d]
    circle50000e.pos = [x5, y1d]
    circle60000e.pos = [x6, y2d]
    circle70000e.pos = [x7, y1d]
    circle80000e.pos = [x8, y2d]
    circle1e.draw()
    circle2e.draw()
    circle3e.draw()
    circle4e.draw()
    circle5e.draw()
    circle6e.draw()
    circle7e.draw()
    circle8e.draw()
    circle10e.draw()
    circle20e.draw()
    circle30e.draw()
    circle40e.draw()
    circle50e.draw()
    circle60e.draw()
    circle70e.draw()
    circle80e.draw()
    circle100e.draw()
    circle200e.draw()
    circle300e.draw()
    circle400e.draw()
    circle500e.draw()
    circle600e.draw()
    circle700e.draw()
    circle800e.draw()
    circle1000e.draw()
    circle2000e.draw()
    circle3000e.draw()
    circle4000e.draw()
    circle5000e.draw()
    circle6000e.draw()
    circle7000e.draw()
    circle8000e.draw()
    circle10000e.draw()
    circle20000e.draw()
    circle30000e.draw()
    circle40000e.draw()
    circle50000e.draw()
    circle60000e.draw()
    circle70000e.draw()
    circle80000e.draw()
    win.flip()
core.wait (5)


#display 30deg circles

# initial positions of circles
x1 = -1340
x2= -1240
x3= -1140
x4= -1040
x5= -940
x6= -840
x7= -740
x8= -640

y1 = 0
y2 = 30

y1a = y1+s
y2a = y2+s

y1b = y1+2*s
y2b = y2+2*s

y1c = y1-s
y2c = y2-s

y1d = y1-2*s
y2d = y2-2*s

while x1 < 750: # draw moving stimulus
    x1 += a # make circle constantly move rightwards
    x2 += a
    x3 += a
    x4 += a
    x5 += a
    x6 += a
    x7 += a
    x8 += a
    circle1.pos = [x1, y1] # directly update both x *and* y
    circle2.pos = [x2, y2]
    circle3.pos = [x3, y1]
    circle4.pos = [x4, y2]
    circle5.pos = [x5, y1]
    circle6.pos = [x6, y2]
    circle7.pos = [x7, y1]
    circle8.pos = [x8, y2]
    circle10.pos = [x1, y1a] 
    circle20.pos = [x2, y2a]
    circle30.pos = [x3, y1a]
    circle40.pos = [x4, y2a]
    circle50.pos = [x5, y1a]
    circle60.pos = [x6, y2a]
    circle70.pos = [x7, y1a]
    circle80.pos = [x8, y2a]
    circle100.pos = [x1, y1b] 
    circle200.pos = [x2, y2b]
    circle300.pos = [x3, y1b]
    circle400.pos = [x4, y2b]
    circle500.pos = [x5, y1b]
    circle600.pos = [x6, y2b]
    circle700.pos = [x7, y1b]
    circle800.pos = [x8, y2b]
    circle1000.pos = [x1, y1c] 
    circle2000.pos = [x2, y2c]
    circle3000.pos = [x3, y1c]
    circle4000.pos = [x4, y2c]
    circle5000.pos = [x5, y1c]
    circle6000.pos = [x6, y2c]
    circle7000.pos = [x7, y1c]
    circle8000.pos = [x8, y2c]
    circle10000.pos = [x1, y1d] 
    circle20000.pos = [x2, y2d]
    circle30000.pos = [x3, y1d]
    circle40000.pos = [x4, y2d]
    circle50000.pos = [x5, y1d]
    circle60000.pos = [x6, y2d]
    circle70000.pos = [x7, y1d]
    circle80000.pos = [x8, y2d]
    circle1.draw()
    circle2.draw()
    circle3.draw()
    circle4.draw()
    circle5.draw()
    circle6.draw()
    circle7.draw()
    circle8.draw()
    circle10.draw()
    circle20.draw()
    circle30.draw()
    circle40.draw()
    circle50.draw()
    circle60.draw()
    circle70.draw()
    circle80.draw()
    circle100.draw()
    circle200.draw()
    circle300.draw()
    circle400.draw()
    circle500.draw()
    circle600.draw()
    circle700.draw()
    circle800.draw()
    circle1000.draw()
    circle2000.draw()
    circle3000.draw()
    circle4000.draw()
    circle5000.draw()
    circle6000.draw()
    circle7000.draw()
    circle8000.draw()
    circle10000.draw()
    circle20000.draw()
    circle30000.draw()
    circle40000.draw()
    circle50000.draw()
    circle60000.draw()
    circle70000.draw()
    circle80000.draw()
    win.flip()
core.wait (5)

#display 5deg circles

# initial positions of circles
x1 = -1340
x2= -1240
x3= -1140
x4= -1040
x5= -940
x6= -840
x7= -740
x8= -640

y1 = 0
y2 = 30

y1a = y1+s
y2a = y2+s

y1b = y1+2*s
y2b = y2+2*s

y1c = y1-s
y2c = y2-s

y1d = y1-2*s
y2d = y2-2*s

while x1 < 750: # draw moving stimulus
    x1 += a # make circle constantly move rightwards
    x2 += a
    x3 += a
    x4 += a
    x5 += a
    x6 += a
    x7 += a
    x8 += a
    circle1b.pos = [x1, y1] # directly update both x *and* y
    circle2b.pos = [x2, y2]
    circle3b.pos = [x3, y1]
    circle4b.pos = [x4, y2]
    circle5b.pos = [x5, y1]
    circle6b.pos = [x6, y2]
    circle7b.pos = [x7, y1]
    circle8b.pos = [x8, y2]
    circle10b.pos = [x1, y1a] 
    circle20b.pos = [x2, y2a]
    circle30b.pos = [x3, y1a]
    circle40b.pos = [x4, y2a]
    circle50b.pos = [x5, y1a]
    circle60b.pos = [x6, y2a]
    circle70b.pos = [x7, y1a]
    circle80b.pos = [x8, y2a]
    circle100b.pos = [x1, y1b] 
    circle200b.pos = [x2, y2b]
    circle300b.pos = [x3, y1b]
    circle400b.pos = [x4, y2b]
    circle500b.pos = [x5, y1b]
    circle600b.pos = [x6, y2b]
    circle700b.pos = [x7, y1b]
    circle800b.pos = [x8, y2b]
    circle1000b.pos = [x1, y1c] 
    circle2000b.pos = [x2, y2c]
    circle3000b.pos = [x3, y1c]
    circle4000b.pos = [x4, y2c]
    circle5000b.pos = [x5, y1c]
    circle6000b.pos = [x6, y2c]
    circle7000b.pos = [x7, y1c]
    circle8000b.pos = [x8, y2c]
    circle10000b.pos = [x1, y1d] 
    circle20000b.pos = [x2, y2d]
    circle30000b.pos = [x3, y1d]
    circle40000b.pos = [x4, y2d]
    circle50000b.pos = [x5, y1d]
    circle60000b.pos = [x6, y2d]
    circle70000b.pos = [x7, y1d]
    circle80000b.pos = [x8, y2d]
    circle1b.draw()
    circle2b.draw()
    circle3b.draw()
    circle4b.draw()
    circle5b.draw()
    circle6b.draw()
    circle7b.draw()
    circle8b.draw()
    circle10b.draw()
    circle20b.draw()
    circle30b.draw()
    circle40b.draw()
    circle50b.draw()
    circle60b.draw()
    circle70b.draw()
    circle80b.draw()
    circle100b.draw()
    circle200b.draw()
    circle300b.draw()
    circle400b.draw()
    circle500b.draw()
    circle600b.draw()
    circle700b.draw()
    circle800b.draw()
    circle1000b.draw()
    circle2000b.draw()
    circle3000b.draw()
    circle4000b.draw()
    circle5000b.draw()
    circle6000b.draw()
    circle7000b.draw()
    circle8000b.draw()
    circle10000b.draw()
    circle20000b.draw()
    circle30000b.draw()
    circle40000b.draw()
    circle50000b.draw()
    circle60000b.draw()
    circle70000b.draw()
    circle80000b.draw()
    win.flip()
core.wait (5)

#display 10deg circles

# initial positions of circles
x1 = -1340
x2= -1240
x3= -1140
x4= -1040
x5= -940
x6= -840
x7= -740
x8= -640

y1 = 0
y2 = 30

y1a = y1+s
y2a = y2+s

y1b = y1+2*s
y2b = y2+2*s

y1c = y1-s
y2c = y2-s

y1d = y1-2*s
y2d = y2-2*s

while x1 < 750: # draw moving stimulus
    x1 += a # make circle constantly move rightwards
    x2 += a
    x3 += a
    x4 += a
    x5 += a
    x6 += a
    x7 += a
    x8 += a
    circle1a.pos = [x1, y1] # directly update both x *and* y
    circle2a.pos = [x2, y2]
    circle3a.pos = [x3, y1]
    circle4a.pos = [x4, y2]
    circle5a.pos = [x5, y1]
    circle6a.pos = [x6, y2]
    circle7a.pos = [x7, y1]
    circle8a.pos = [x8, y2]
    circle10a.pos = [x1, y1a] 
    circle20a.pos = [x2, y2a]
    circle30a.pos = [x3, y1a]
    circle40a.pos = [x4, y2a]
    circle50a.pos = [x5, y1a]
    circle60a.pos = [x6, y2a]
    circle70a.pos = [x7, y1a]
    circle80a.pos = [x8, y2a]
    circle100a.pos = [x1, y1b] 
    circle200a.pos = [x2, y2b]
    circle300a.pos = [x3, y1b]
    circle400a.pos = [x4, y2b]
    circle500a.pos = [x5, y1b]
    circle600a.pos = [x6, y2b]
    circle700a.pos = [x7, y1b]
    circle800a.pos = [x8, y2b]
    circle1000a.pos = [x1, y1c] 
    circle2000a.pos = [x2, y2c]
    circle3000a.pos = [x3, y1c]
    circle4000a.pos = [x4, y2c]
    circle5000a.pos = [x5, y1c]
    circle6000a.pos = [x6, y2c]
    circle7000a.pos = [x7, y1c]
    circle8000a.pos = [x8, y2c]
    circle10000a.pos = [x1, y1d] 
    circle20000a.pos = [x2, y2d]
    circle30000a.pos = [x3, y1d]
    circle40000a.pos = [x4, y2d]
    circle50000a.pos = [x5, y1d]
    circle60000a.pos = [x6, y2d]
    circle70000a.pos = [x7, y1d]
    circle80000a.pos = [x8, y2d]
    circle1a.draw()
    circle2a.draw()
    circle3a.draw()
    circle4a.draw()
    circle5a.draw()
    circle6a.draw()
    circle7a.draw()
    circle8a.draw()
    circle10a.draw()
    circle20a.draw()
    circle30a.draw()
    circle40a.draw()
    circle50a.draw()
    circle60a.draw()
    circle70a.draw()
    circle80a.draw()
    circle100a.draw()
    circle200a.draw()
    circle300a.draw()
    circle400a.draw()
    circle500a.draw()
    circle600a.draw()
    circle700a.draw()
    circle800a.draw()
    circle1000a.draw()
    circle2000a.draw()
    circle3000a.draw()
    circle4000a.draw()
    circle5000a.draw()
    circle6000a.draw()
    circle7000a.draw()
    circle8000a.draw()
    circle10000a.draw()
    circle20000a.draw()
    circle30000a.draw()
    circle40000a.draw()
    circle50000a.draw()
    circle60000a.draw()
    circle70000a.draw()
    circle80000a.draw()
    win.flip()
core.wait (5)

#display 5deg circles

# initial positions of circles
x1 = -1340
x2= -1240
x3= -1140
x4= -1040
x5= -940
x6= -840
x7= -740
x8= -640

y1 = 0
y2 = 30

y1a = y1+s
y2a = y2+s

y1b = y1+2*s
y2b = y2+2*s

y1c = y1-s
y2c = y2-s

y1d = y1-2*s
y2d = y2-2*s

while x1 < 750: # draw moving stimulus
    x1 += a # make circle constantly move rightwards
    x2 += a
    x3 += a
    x4 += a
    x5 += a
    x6 += a
    x7 += a
    x8 += a
    circle1b.pos = [x1, y1] # directly update both x *and* y
    circle2b.pos = [x2, y2]
    circle3b.pos = [x3, y1]
    circle4b.pos = [x4, y2]
    circle5b.pos = [x5, y1]
    circle6b.pos = [x6, y2]
    circle7b.pos = [x7, y1]
    circle8b.pos = [x8, y2]
    circle10b.pos = [x1, y1a] 
    circle20b.pos = [x2, y2a]
    circle30b.pos = [x3, y1a]
    circle40b.pos = [x4, y2a]
    circle50b.pos = [x5, y1a]
    circle60b.pos = [x6, y2a]
    circle70b.pos = [x7, y1a]
    circle80b.pos = [x8, y2a]
    circle100b.pos = [x1, y1b] 
    circle200b.pos = [x2, y2b]
    circle300b.pos = [x3, y1b]
    circle400b.pos = [x4, y2b]
    circle500b.pos = [x5, y1b]
    circle600b.pos = [x6, y2b]
    circle700b.pos = [x7, y1b]
    circle800b.pos = [x8, y2b]
    circle1000b.pos = [x1, y1c] 
    circle2000b.pos = [x2, y2c]
    circle3000b.pos = [x3, y1c]
    circle4000b.pos = [x4, y2c]
    circle5000b.pos = [x5, y1c]
    circle6000b.pos = [x6, y2c]
    circle7000b.pos = [x7, y1c]
    circle8000b.pos = [x8, y2c]
    circle10000b.pos = [x1, y1d] 
    circle20000b.pos = [x2, y2d]
    circle30000b.pos = [x3, y1d]
    circle40000b.pos = [x4, y2d]
    circle50000b.pos = [x5, y1d]
    circle60000b.pos = [x6, y2d]
    circle70000b.pos = [x7, y1d]
    circle80000b.pos = [x8, y2d]
    circle1b.draw()
    circle2b.draw()
    circle3b.draw()
    circle4b.draw()
    circle5b.draw()
    circle6b.draw()
    circle7b.draw()
    circle8b.draw()
    circle10b.draw()
    circle20b.draw()
    circle30b.draw()
    circle40b.draw()
    circle50b.draw()
    circle60b.draw()
    circle70b.draw()
    circle80b.draw()
    circle100b.draw()
    circle200b.draw()
    circle300b.draw()
    circle400b.draw()
    circle500b.draw()
    circle600b.draw()
    circle700b.draw()
    circle800b.draw()
    circle1000b.draw()
    circle2000b.draw()
    circle3000b.draw()
    circle4000b.draw()
    circle5000b.draw()
    circle6000b.draw()
    circle7000b.draw()
    circle8000b.draw()
    circle10000b.draw()
    circle20000b.draw()
    circle30000b.draw()
    circle40000b.draw()
    circle50000b.draw()
    circle60000b.draw()
    circle70000b.draw()
    circle80000b.draw()
    win.flip()
core.wait (5)

#display 20deg circles

# initial positions of circles
x1 = -1340
x2= -1240
x3= -1140
x4= -1040
x5= -940
x6= -840
x7= -740
x8= -640

y1 = 0
y2 = 30

y1a = y1+s
y2a = y2+s

y1b = y1+2*s
y2b = y2+2*s

y1c = y1-s
y2c = y2-s

y1d = y1-2*s
y2d = y2-2*s

while x1 < 750: # draw moving stimulus
    x1 += a # make circle constantly move rightwards
    x2 += a
    x3 += a
    x4 += a
    x5 += a
    x6 += a
    x7 += a
    x8 += a
    circle1c.pos = [x1, y1] # directly update both x *and* y
    circle2c.pos = [x2, y2]
    circle3c.pos = [x3, y1]
    circle4c.pos = [x4, y2]
    circle5c.pos = [x5, y1]
    circle6c.pos = [x6, y2]
    circle7c.pos = [x7, y1]
    circle8c.pos = [x8, y2]
    circle10c.pos = [x1, y1a] 
    circle20c.pos = [x2, y2a]
    circle30c.pos = [x3, y1a]
    circle40c.pos = [x4, y2a]
    circle50c.pos = [x5, y1a]
    circle60c.pos = [x6, y2a]
    circle70c.pos = [x7, y1a]
    circle80c.pos = [x8, y2a]
    circle100c.pos = [x1, y1b] 
    circle200c.pos = [x2, y2b]
    circle300c.pos = [x3, y1b]
    circle400c.pos = [x4, y2b]
    circle500c.pos = [x5, y1b]
    circle600c.pos = [x6, y2b]
    circle700c.pos = [x7, y1b]
    circle800c.pos = [x8, y2b]
    circle1000c.pos = [x1, y1c] 
    circle2000c.pos = [x2, y2c]
    circle3000c.pos = [x3, y1c]
    circle4000c.pos = [x4, y2c]
    circle5000c.pos = [x5, y1c]
    circle6000c.pos = [x6, y2c]
    circle7000c.pos = [x7, y1c]
    circle8000c.pos = [x8, y2c]
    circle10000c.pos = [x1, y1d] 
    circle20000c.pos = [x2, y2d]
    circle30000c.pos = [x3, y1d]
    circle40000c.pos = [x4, y2d]
    circle50000c.pos = [x5, y1d]
    circle60000c.pos = [x6, y2d]
    circle70000c.pos = [x7, y1d]
    circle80000c.pos = [x8, y2d]
    circle1c.draw()
    circle2c.draw()
    circle3c.draw()
    circle4c.draw()
    circle5c.draw()
    circle6c.draw()
    circle7c.draw()
    circle8c.draw()
    circle10c.draw()
    circle20c.draw()
    circle30c.draw()
    circle40c.draw()
    circle50c.draw()
    circle60c.draw()
    circle70c.draw()
    circle80c.draw()
    circle100c.draw()
    circle200c.draw()
    circle300c.draw()
    circle400c.draw()
    circle500c.draw()
    circle600c.draw()
    circle700c.draw()
    circle800c.draw()
    circle1000c.draw()
    circle2000c.draw()
    circle3000c.draw()
    circle4000c.draw()
    circle5000c.draw()
    circle6000c.draw()
    circle7000c.draw()
    circle8000c.draw()
    circle10000c.draw()
    circle20000c.draw()
    circle30000c.draw()
    circle40000c.draw()
    circle50000c.draw()
    circle60000c.draw()
    circle70000c.draw()
    circle80000c.draw()
    win.flip()
core.wait (5)

#display 1deg circles

# initial positions of circles
x1 = -1340
x2= -1240
x3= -1140
x4= -1040
x5= -940
x6= -840
x7= -740
x8= -640

y1 = 0
y2 = 30

y1a = y1+s
y2a = y2+s

y1b = y1+2*s
y2b = y2+2*s

y1c = y1-s
y2c = y2-s

y1d = y1-2*s
y2d = y2-2*s

while x1 < 750: # draw moving stimulus
    x1 += a # make circle constantly move rightwards
    x2 += a
    x3 += a
    x4 += a
    x5 += a
    x6 += a
    x7 += a
    x8 += a
    circle1d.pos = [x1, y1] # directly update both x *and* y
    circle2d.pos = [x2, y2]
    circle3d.pos = [x3, y1]
    circle4d.pos = [x4, y2]
    circle5d.pos = [x5, y1]
    circle6d.pos = [x6, y2]
    circle7d.pos = [x7, y1]
    circle8d.pos = [x8, y2]
    circle10d.pos = [x1, y1a] 
    circle20d.pos = [x2, y2a]
    circle30d.pos = [x3, y1a]
    circle40d.pos = [x4, y2a]
    circle50d.pos = [x5, y1a]
    circle60d.pos = [x6, y2a]
    circle70d.pos = [x7, y1a]
    circle80d.pos = [x8, y2a]
    circle100d.pos = [x1, y1b] 
    circle200d.pos = [x2, y2b]
    circle300d.pos = [x3, y1b]
    circle400d.pos = [x4, y2b]
    circle500d.pos = [x5, y1b]
    circle600d.pos = [x6, y2b]
    circle700d.pos = [x7, y1b]
    circle800d.pos = [x8, y2b]
    circle1000d.pos = [x1, y1c] 
    circle2000d.pos = [x2, y2c]
    circle3000d.pos = [x3, y1c]
    circle4000d.pos = [x4, y2c]
    circle5000d.pos = [x5, y1c]
    circle6000d.pos = [x6, y2c]
    circle7000d.pos = [x7, y1c]
    circle8000d.pos = [x8, y2c]
    circle10000d.pos = [x1, y1d] 
    circle20000d.pos = [x2, y2d]
    circle30000d.pos = [x3, y1d]
    circle40000d.pos = [x4, y2d]
    circle50000d.pos = [x5, y1d]
    circle60000d.pos = [x6, y2d]
    circle70000d.pos = [x7, y1d]
    circle80000d.pos = [x8, y2d]
    circle1d.draw()
    circle2d.draw()
    circle3d.draw()
    circle4d.draw()
    circle5d.draw()
    circle6d.draw()
    circle7d.draw()
    circle8d.draw()
    circle10d.draw()
    circle20d.draw()
    circle30d.draw()
    circle40d.draw()
    circle50d.draw()
    circle60d.draw()
    circle70d.draw()
    circle80d.draw()
    circle100d.draw()
    circle200d.draw()
    circle300d.draw()
    circle400d.draw()
    circle500d.draw()
    circle600d.draw()
    circle700d.draw()
    circle800d.draw()
    circle1000d.draw()
    circle2000d.draw()
    circle3000d.draw()
    circle4000d.draw()
    circle5000d.draw()
    circle6000d.draw()
    circle7000d.draw()
    circle8000d.draw()
    circle10000d.draw()
    circle20000d.draw()
    circle30000d.draw()
    circle40000d.draw()
    circle50000d.draw()
    circle60000d.draw()
    circle70000d.draw()
    circle80000d.draw()
    win.flip()
core.wait (5)

#display 3deg circles

# initial positions of circles
x1 = -1340
x2= -1240
x3= -1140
x4= -1040
x5= -940
x6= -840
x7= -740
x8= -640

y1 = 0
y2 = 30

y1a = y1+s
y2a = y2+s

y1b = y1+2*s
y2b = y2+2*s

y1c = y1-s
y2c = y2-s

y1d = y1-2*s
y2d = y2-2*s

while x1 < 750: # draw moving stimulus
    x1 += a # make circle constantly move rightwards
    x2 += a
    x3 += a
    x4 += a
    x5 += a
    x6 += a
    x7 += a
    x8 += a
    circle1e.pos = [x1, y1] # directly update both x *and* y
    circle2e.pos = [x2, y2]
    circle3e.pos = [x3, y1]
    circle4e.pos = [x4, y2]
    circle5e.pos = [x5, y1]
    circle6e.pos = [x6, y2]
    circle7e.pos = [x7, y1]
    circle8e.pos = [x8, y2]
    circle10e.pos = [x1, y1a] 
    circle20e.pos = [x2, y2a]
    circle30e.pos = [x3, y1a]
    circle40e.pos = [x4, y2a]
    circle50e.pos = [x5, y1a]
    circle60e.pos = [x6, y2a]
    circle70e.pos = [x7, y1a]
    circle80e.pos = [x8, y2a]
    circle100e.pos = [x1, y1b] 
    circle200e.pos = [x2, y2b]
    circle300e.pos = [x3, y1b]
    circle400e.pos = [x4, y2b]
    circle500e.pos = [x5, y1b]
    circle600e.pos = [x6, y2b]
    circle700e.pos = [x7, y1b]
    circle800e.pos = [x8, y2b]
    circle1000e.pos = [x1, y1c] 
    circle2000e.pos = [x2, y2c]
    circle3000e.pos = [x3, y1c]
    circle4000e.pos = [x4, y2c]
    circle5000e.pos = [x5, y1c]
    circle6000e.pos = [x6, y2c]
    circle7000e.pos = [x7, y1c]
    circle8000e.pos = [x8, y2c]
    circle10000e.pos = [x1, y1d] 
    circle20000e.pos = [x2, y2d]
    circle30000e.pos = [x3, y1d]
    circle40000e.pos = [x4, y2d]
    circle50000e.pos = [x5, y1d]
    circle60000e.pos = [x6, y2d]
    circle70000e.pos = [x7, y1d]
    circle80000e.pos = [x8, y2d]
    circle1e.draw()
    circle2e.draw()
    circle3e.draw()
    circle4e.draw()
    circle5e.draw()
    circle6e.draw()
    circle7e.draw()
    circle8e.draw()
    circle10e.draw()
    circle20e.draw()
    circle30e.draw()
    circle40e.draw()
    circle50e.draw()
    circle60e.draw()
    circle70e.draw()
    circle80e.draw()
    circle100e.draw()
    circle200e.draw()
    circle300e.draw()
    circle400e.draw()
    circle500e.draw()
    circle600e.draw()
    circle700e.draw()
    circle800e.draw()
    circle1000e.draw()
    circle2000e.draw()
    circle3000e.draw()
    circle4000e.draw()
    circle5000e.draw()
    circle6000e.draw()
    circle7000e.draw()
    circle8000e.draw()
    circle10000e.draw()
    circle20000e.draw()
    circle30000e.draw()
    circle40000e.draw()
    circle50000e.draw()
    circle60000e.draw()
    circle70000e.draw()
    circle80000e.draw()
    win.flip()
core.wait (5)

