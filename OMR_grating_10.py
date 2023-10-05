from psychopy import visual, core, event

win0 = visual.Window([800, 600], screen=1, monitor= 'testMonitor', fullscr=True, color=[0,0,0], units='pix')

grat_stim = visual.GratingStim(win=win0, tex='sqr', units= 'pix', pos=(0.0,0.0), size=800, sf=0.02, ori= 0.0, phase=(0.0,0.0))


while(1):
    grat_stim.setPhase(0.02, '+')
    grat_stim.draw()
    win0.flip()
    
    if len(event.getKeys()) > 0:
        break
    event.clearEvents()

win0 = close()

