#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Tue Jan 17 16:16:50 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'NavUtil_RO'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/mettapham/Downloads/HOMES_RankOrder-NavUtil/NavUtil_RO_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "welcome" ---
text = visual.TextStim(win=win, name='text',
    text='Welcome to the Navigational Utility Rank Ordering Task',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "instruction" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='In this task, you are presented with 14 pictures of various objects. Your job is to rank them from 1-14 according to how incline you are to use the object as a landmark to navigate an unknown environment. 1 being most inclined and 14 being least inclined.\n\nPress SPACEBAR to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "trial" ---
exit_TEXT = visual.TextStim(win=win, name='exit_TEXT',
    text='When you are finished ranking the items, press RETURN',
    font='Open Sans',
    pos=(0, .45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
exit_RESP = keyboard.Keyboard()
image1 = visual.ImageStim(
    win=win,
    name='image1', 
    image='images_RO_NU/Landmark1.png', mask=None, anchor='center',
    ori=0.0, pos=(-.5,.3), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
textbox1 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(-.5,.15),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox1',
     autoLog=True,
)
image2 = visual.ImageStim(
    win=win,
    name='image2', 
    image='images_RO_NU/Landmark2.png', mask=None, anchor='center',
    ori=0.0, pos=(-.25,.3), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
textbox2 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(-.25,.15),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox2',
     autoLog=True,
)
image3 = visual.ImageStim(
    win=win,
    name='image3', 
    image='images_RO_NU/Landmark3.png', mask=None, anchor='center',
    ori=0.0, pos=(0,.3), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
textbox3 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0,.15),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox3',
     autoLog=True,
)
image4 = visual.ImageStim(
    win=win,
    name='image4', 
    image='images_RO_NU/Landmark4.png', mask=None, anchor='center',
    ori=0.0, pos=(.25,.3), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
textbox4 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(.25,.15),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox4',
     autoLog=True,
)
image5 = visual.ImageStim(
    win=win,
    name='image5', 
    image='images_RO_NU/Landmark5.png', mask=None, anchor='center',
    ori=0.0, pos=(.5,.3), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
textbox5 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(.5,.15),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox5',
     autoLog=True,
)
image6 = visual.ImageStim(
    win=win,
    name='image6', 
    image='images_RO_NU/Landmark6.png', mask=None, anchor='center',
    ori=0.0, pos=(-.5,0), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
textbox6 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(-.5,-.15),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox6',
     autoLog=True,
)
image7 = visual.ImageStim(
    win=win,
    name='image7', 
    image='images_RO_NU/Landmark7.png', mask=None, anchor='center',
    ori=0.0, pos=(-.25,0), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
textbox7 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(-.25,-.15),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox7',
     autoLog=True,
)
image8 = visual.ImageStim(
    win=win,
    name='image8', 
    image='images_RO_NU/Landmark8.png', mask=None, anchor='center',
    ori=0.0, pos=(0,0), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
textbox8 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0,-.15),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox8',
     autoLog=True,
)
image9 = visual.ImageStim(
    win=win,
    name='image9', 
    image='images_RO_NU/Landmark9.png', mask=None, anchor='center',
    ori=0.0, pos=(.25,0), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
textbox9 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(.25,-.15),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox9',
     autoLog=True,
)
image10 = visual.ImageStim(
    win=win,
    name='image10', 
    image='images_RO_NU/Landmark10.png', mask=None, anchor='center',
    ori=0.0, pos=(.5,0), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
textbox10 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(.5,-.15),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox10',
     autoLog=True,
)
image11 = visual.ImageStim(
    win=win,
    name='image11', 
    image='images_RO_NU/Landmark11.png', mask=None, anchor='center',
    ori=0.0, pos=(-.5,-.3), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-22.0)
textbox11 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(-.5,-.45),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox11',
     autoLog=True,
)
image12 = visual.ImageStim(
    win=win,
    name='image12', 
    image='images_RO_NU/Landmark12.png', mask=None, anchor='center',
    ori=0.0, pos=(-.25,-.3), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-24.0)
textbox12 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(-.25,-.45),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox12',
     autoLog=True,
)
image13 = visual.ImageStim(
    win=win,
    name='image13', 
    image='images_RO_NU/Landmark13.png', mask=None, anchor='center',
    ori=0.0, pos=(0,-.3), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-26.0)
textbox13 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0,-.45),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox13',
     autoLog=True,
)
image14 = visual.ImageStim(
    win=win,
    name='image14', 
    image='images_RO_NU/Landmark14.png', mask=None, anchor='center',
    ori=0.0, pos=(.25,-.3), size=(.2,.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-28.0)
textbox14 = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(.25,-.45),     letterHeight=0.05,
     size=(.15,.08), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=[-1.0000, -1.0000, -1.0000],
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox14',
     autoLog=True,
)

# --- Initialize components for Routine "end" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='Thank you for participating in the Navigational Utility Rank Ordering Task',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
welcomeComponents = [text]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welcome" ---
while continueRoutine and routineTimer.getTime() < 4.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-4.000000)

# --- Prepare to start Routine "instruction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructionComponents = [text_2, key_resp]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction" ---
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trial" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
exit_RESP.keys = []
exit_RESP.rt = []
_exit_RESP_allKeys = []
textbox1.reset()
textbox2.reset()
textbox3.reset()
textbox4.reset()
textbox5.reset()
textbox6.reset()
textbox7.reset()
textbox8.reset()
textbox9.reset()
textbox10.reset()
textbox11.reset()
textbox12.reset()
textbox13.reset()
textbox14.reset()
# keep track of which components have finished
trialComponents = [exit_TEXT, exit_RESP, image1, textbox1, image2, textbox2, image3, textbox3, image4, textbox4, image5, textbox5, image6, textbox6, image7, textbox7, image8, textbox8, image9, textbox9, image10, textbox10, image11, textbox11, image12, textbox12, image13, textbox13, image14, textbox14]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exit_TEXT* updates
    if exit_TEXT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exit_TEXT.frameNStart = frameN  # exact frame index
        exit_TEXT.tStart = t  # local t and not account for scr refresh
        exit_TEXT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exit_TEXT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'exit_TEXT.started')
        exit_TEXT.setAutoDraw(True)
    
    # *exit_RESP* updates
    waitOnFlip = False
    if exit_RESP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exit_RESP.frameNStart = frameN  # exact frame index
        exit_RESP.tStart = t  # local t and not account for scr refresh
        exit_RESP.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exit_RESP, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'exit_RESP.started')
        exit_RESP.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(exit_RESP.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(exit_RESP.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if exit_RESP.status == STARTED and not waitOnFlip:
        theseKeys = exit_RESP.getKeys(keyList=['return'], waitRelease=False)
        _exit_RESP_allKeys.extend(theseKeys)
        if len(_exit_RESP_allKeys):
            exit_RESP.keys = _exit_RESP_allKeys[-1].name  # just the last key pressed
            exit_RESP.rt = _exit_RESP_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image1* updates
    if image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image1.frameNStart = frameN  # exact frame index
        image1.tStart = t  # local t and not account for scr refresh
        image1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image1.started')
        image1.setAutoDraw(True)
    
    # *textbox1* updates
    if textbox1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox1.frameNStart = frameN  # exact frame index
        textbox1.tStart = t  # local t and not account for scr refresh
        textbox1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox1.started')
        textbox1.setAutoDraw(True)
    
    # *image2* updates
    if image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image2.frameNStart = frameN  # exact frame index
        image2.tStart = t  # local t and not account for scr refresh
        image2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image2.started')
        image2.setAutoDraw(True)
    
    # *textbox2* updates
    if textbox2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox2.frameNStart = frameN  # exact frame index
        textbox2.tStart = t  # local t and not account for scr refresh
        textbox2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox2.started')
        textbox2.setAutoDraw(True)
    
    # *image3* updates
    if image3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image3.frameNStart = frameN  # exact frame index
        image3.tStart = t  # local t and not account for scr refresh
        image3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image3.started')
        image3.setAutoDraw(True)
    
    # *textbox3* updates
    if textbox3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox3.frameNStart = frameN  # exact frame index
        textbox3.tStart = t  # local t and not account for scr refresh
        textbox3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox3.started')
        textbox3.setAutoDraw(True)
    
    # *image4* updates
    if image4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image4.frameNStart = frameN  # exact frame index
        image4.tStart = t  # local t and not account for scr refresh
        image4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image4.started')
        image4.setAutoDraw(True)
    
    # *textbox4* updates
    if textbox4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox4.frameNStart = frameN  # exact frame index
        textbox4.tStart = t  # local t and not account for scr refresh
        textbox4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox4.started')
        textbox4.setAutoDraw(True)
    
    # *image5* updates
    if image5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image5.frameNStart = frameN  # exact frame index
        image5.tStart = t  # local t and not account for scr refresh
        image5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image5.started')
        image5.setAutoDraw(True)
    
    # *textbox5* updates
    if textbox5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox5.frameNStart = frameN  # exact frame index
        textbox5.tStart = t  # local t and not account for scr refresh
        textbox5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox5.started')
        textbox5.setAutoDraw(True)
    
    # *image6* updates
    if image6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image6.frameNStart = frameN  # exact frame index
        image6.tStart = t  # local t and not account for scr refresh
        image6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image6.started')
        image6.setAutoDraw(True)
    
    # *textbox6* updates
    if textbox6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox6.frameNStart = frameN  # exact frame index
        textbox6.tStart = t  # local t and not account for scr refresh
        textbox6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox6.started')
        textbox6.setAutoDraw(True)
    
    # *image7* updates
    if image7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image7.frameNStart = frameN  # exact frame index
        image7.tStart = t  # local t and not account for scr refresh
        image7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image7.started')
        image7.setAutoDraw(True)
    
    # *textbox7* updates
    if textbox7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox7.frameNStart = frameN  # exact frame index
        textbox7.tStart = t  # local t and not account for scr refresh
        textbox7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox7.started')
        textbox7.setAutoDraw(True)
    
    # *image8* updates
    if image8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image8.frameNStart = frameN  # exact frame index
        image8.tStart = t  # local t and not account for scr refresh
        image8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image8.started')
        image8.setAutoDraw(True)
    
    # *textbox8* updates
    if textbox8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox8.frameNStart = frameN  # exact frame index
        textbox8.tStart = t  # local t and not account for scr refresh
        textbox8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox8.started')
        textbox8.setAutoDraw(True)
    
    # *image9* updates
    if image9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image9.frameNStart = frameN  # exact frame index
        image9.tStart = t  # local t and not account for scr refresh
        image9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image9.started')
        image9.setAutoDraw(True)
    
    # *textbox9* updates
    if textbox9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox9.frameNStart = frameN  # exact frame index
        textbox9.tStart = t  # local t and not account for scr refresh
        textbox9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox9.started')
        textbox9.setAutoDraw(True)
    
    # *image10* updates
    if image10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image10.frameNStart = frameN  # exact frame index
        image10.tStart = t  # local t and not account for scr refresh
        image10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image10.started')
        image10.setAutoDraw(True)
    
    # *textbox10* updates
    if textbox10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox10.frameNStart = frameN  # exact frame index
        textbox10.tStart = t  # local t and not account for scr refresh
        textbox10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox10.started')
        textbox10.setAutoDraw(True)
    
    # *image11* updates
    if image11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image11.frameNStart = frameN  # exact frame index
        image11.tStart = t  # local t and not account for scr refresh
        image11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image11, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image11.started')
        image11.setAutoDraw(True)
    
    # *textbox11* updates
    if textbox11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox11.frameNStart = frameN  # exact frame index
        textbox11.tStart = t  # local t and not account for scr refresh
        textbox11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox11, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox11.started')
        textbox11.setAutoDraw(True)
    
    # *image12* updates
    if image12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image12.frameNStart = frameN  # exact frame index
        image12.tStart = t  # local t and not account for scr refresh
        image12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image12, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image12.started')
        image12.setAutoDraw(True)
    
    # *textbox12* updates
    if textbox12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox12.frameNStart = frameN  # exact frame index
        textbox12.tStart = t  # local t and not account for scr refresh
        textbox12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox12, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox12.started')
        textbox12.setAutoDraw(True)
    
    # *image13* updates
    if image13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image13.frameNStart = frameN  # exact frame index
        image13.tStart = t  # local t and not account for scr refresh
        image13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image13.started')
        image13.setAutoDraw(True)
    
    # *textbox13* updates
    if textbox13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox13.frameNStart = frameN  # exact frame index
        textbox13.tStart = t  # local t and not account for scr refresh
        textbox13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox13.started')
        textbox13.setAutoDraw(True)
    
    # *image14* updates
    if image14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image14.frameNStart = frameN  # exact frame index
        image14.tStart = t  # local t and not account for scr refresh
        image14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image14, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image14.started')
        image14.setAutoDraw(True)
    
    # *textbox14* updates
    if textbox14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox14.frameNStart = frameN  # exact frame index
        textbox14.tStart = t  # local t and not account for scr refresh
        textbox14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox14, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox14.started')
        textbox14.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial" ---
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if exit_RESP.keys in ['', [], None]:  # No response was made
    exit_RESP.keys = None
thisExp.addData('exit_RESP.keys',exit_RESP.keys)
if exit_RESP.keys != None:  # we had a response
    thisExp.addData('exit_RESP.rt', exit_RESP.rt)
thisExp.nextEntry()
thisExp.addData('textbox1.text',textbox1.text)
thisExp.addData('textbox2.text',textbox2.text)
thisExp.addData('textbox3.text',textbox3.text)
thisExp.addData('textbox4.text',textbox4.text)
thisExp.addData('textbox5.text',textbox5.text)
thisExp.addData('textbox6.text',textbox6.text)
thisExp.addData('textbox7.text',textbox7.text)
thisExp.addData('textbox8.text',textbox8.text)
thisExp.addData('textbox9.text',textbox9.text)
thisExp.addData('textbox10.text',textbox10.text)
thisExp.addData('textbox11.text',textbox11.text)
thisExp.addData('textbox12.text',textbox12.text)
thisExp.addData('textbox13.text',textbox13.text)
thisExp.addData('textbox14.text',textbox14.text)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_3]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end" ---
while continueRoutine and routineTimer.getTime() < 4.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.stopped')
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-4.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
