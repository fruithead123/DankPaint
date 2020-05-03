
#  MLG Dank Paint by Gary Sun 

from pygame import *
from random import * #For spray tool
from tkinter import *
from math import *
root=Tk()
root.withdraw()
init()


#---------Setup----------#
#Colours
RED=   (255,0,0,255)
ORANGE=(255,165,0,255)
YELLOW=(255,255,0,255)
GREEN= (0,255,0,255)
BLUE=  (0,0,255,255)
PURPLE=(128,0,128,255)
WHITE= (255,255,255,255)
BLACK= (0,0,0,255)
RECTBG=(222,222,222,255)

fontSmall=font.SysFont('RuneScape UF',20) #Font for colour numbers
fontLarge=font.SysFont('RuneScape UF',30) #Font for thickness/opacity counters


##Defining Areas

#Main areas
toolBorderRect=Rect(0,0,1080,150)
toolRect=Rect(5,5,1070,140)
stampBorderRect=(30,295,210,460) 
stampRect=Rect(35,300,200,450)
extraRect=Rect(275,625,750,125)
extraBorderRect=Rect(270,620,760,135)
canvasBorderRect=Rect(270,155,760,460)  
canvasRect=Rect(275,160,750,450)        
invisRect=Rect(250,130,810,500)  #used to make sure stamps arn't 'stuck' on the screen when leaving the canvas. Larger than canvasBorderRect to allow slower computers/fast mouse movements to be registered
paintSizeRect=Rect(430,110,270,30) #Area over the thickness/opacity counters. Allows the counters to refresh

#Basic tools
infoRect=Rect(200,10,200,130)
pencilRect=Rect(430,15,40,40)
brushRect=Rect(480,15,40,40)
sprayRect=Rect(530,15,40,40)
fillRect=Rect(580,15,40,40)
eraserRect=Rect(630,15,40,40)
rectRect=Rect(430,65,40,40)
rectFillRect=Rect(480,65,40,40)
ellipseRect=Rect(530,65,40,40)
ellipseFillRect=Rect(580,65,40,40)
lineRect=Rect(630,65,40,40)


#Misc Tools
saveRect=Rect(30,25,40,40)
openRect=Rect(80,25,40,40)
redoRect=Rect(10,75,40,40)
undoRect=Rect(60,75,40,40)
clearRect=Rect(110,75,40,40)

#Colour selection
paletteRect=Rect(800,10,200,130)

col1DisplayRect=Rect(720,25,34,34)
col2DisplayRect=Rect(760,25,34,34)  #Displays the 4 currently saved colours (Borders)
col3DisplayRect=Rect(720,65,34,34)
col4DisplayRect=Rect(760,65,34,34)

col1Rect=Rect(722,27,30,30)
col2Rect=Rect(762,27,30,30)
col3Rect=Rect(722,67,30,30)  ##Displays the 4 currently saved colours (Colours)
col4Rect=Rect(762,67,30,30)

eyedropRect=Rect(680,45,30,30)   #Get clicked colour
redRectBorder=Rect(1010,15,24,24)
redRect=Rect(1012,17,20,20)
orangeRectBorder=Rect(1040,15,24,24)
orangeRect=Rect(1042,17,20,20)
yellowRectBorder=Rect(1010,45,24,24)
yellowRect=Rect(1012,47,20,20)
greenRectBorder=Rect(1040,45,24,24)
greenRect=Rect(1042,47,20,20)            #Predefined colours and borders
blueRectBorder=Rect(1010,75,24,24)
blueRect=Rect(1012,77,20,20)
purpleRectBorder=Rect(1040,75,24,24)
purpleRect=Rect(1042,77,20,20)
blackRectBorder=Rect(1010,105,24,24)
blackRect=Rect(1012,107,20,20)
whiteRectBorder=Rect(1040,105,24,24)
whiteRect=Rect(1042,107,20,20)

#Stamps
doritoRect=Rect(40,310,70,90)
dewRect=Rect(140,310,70,130)
snoopRect=Rect(40,400,70,150)
sanicRect=Rect(140,450,70,80)
frogRect=Rect(40,540,80,100)          #Stamp areas
shrekRect=Rect(140,540,75,75)
glassesRect=Rect(40,660,80,40)
hatRect=Rect(140,660,80,55)

#Extras
filterRect=Rect(285,635,175,105)
filterRect2=Rect(470,635,175,105)
filterRect3=Rect(655,635,175,105)     #Filters at the bottom of the screen
filterRect4=Rect(840,635,175,105)
musicRect=Rect(5,160,260,120)   #Hidden music easter egg when you click the frog on top of the stamp rect


#Define/load Pictures
colPalette=image.load('newcol.png')
background=image.load('background.jpg')
pencil=image.load('Tools/pencil.png')
pencil2=image.load('Tools/pencil2.png')
brush=image.load('Tools/brush.png')
brush2=image.load('Tools/brush2.png')
spray=image.load('Tools/spray.png')
spray2=image.load('Tools/spray2.png')
bucket=image.load('Tools/bucket.png')
bucket2=image.load('Tools/bucket2.png')
rect=image.load('Tools/rect.png')
rect2=image.load('Tools/rect2.png')
rectFill=image.load('Tools/rectFill.png')
rectFill2=image.load('Tools/rectFill2.png')
eraser=image.load('Tools/eraser.png')
eraser2=image.load('Tools/eraser2.png')
ellipse=image.load('Tools/ellipse.png')
ellipse2=image.load('Tools/ellipse2.png')
ellipseFill=image.load('Tools/ellipseFill.png')
ellipseFill2=image.load('Tools/ellipseFill2.png')
line=image.load('Tools/line.png')
line2=image.load('Tools/line2.png')
dropper=image.load('Tools/dropper.png')
dropper2=image.load('Tools/dropper2.png')
save=image.load('Tools/save.png')
save2=image.load('Tools/save2.png')
openI=image.load('Tools/open.png')
openI2=image.load('Tools/open2.png')
undo=image.load('Tools/undo.png')
undo2=image.load('Tools/undo2.png')
redo=image.load('Tools/redo.png')
redo2=image.load('Tools/redo2.png')
clear=image.load('Tools/clear.png')
clear2=image.load('Tools/clear2.png')
logo=image.load('logo.png')

#Hover tool tips
pencilHover=image.load('Hover/pencilHover.png')
brushHover=image.load('Hover/brushHover.png')
sprayHover=image.load('Hover/sprayHover.png')
fillHover=image.load('Hover/fillHover.png')
eraserHover=image.load('Hover/eraserHover.png')
rectHover=image.load('Hover/rectHover.png')
rectFillHover=image.load('Hover/rectFillHover.png')
ellipseHover=image.load('Hover/ellipseHover.png')
ellipseFillHover=image.load('Hover/ellipseFillHover.png')
lineHover=image.load('Hover/lineHover.png')
undoHover=image.load('Hover/undoHover.png')
redoHover=image.load('Hover/redoHover.png')
openHover=image.load('Hover/openHover.png')
saveHover=image.load('Hover/saveHover.png')
clearHover=image.load('Hover/clearHover.png')
dropperHover=image.load('Hover/dropperHover.png')

#Load stamps
stampsSmall=[] #Stamps displayed on canvas
stamps=[]  #Stamps that display on side
for i in range(8):
    stampsSmall.append(image.load('Stamps/stamp'+str(i)+'S.png'))
for i in range(8):
    stamps.append(image.load('Stamps/stamp'+str(i)+'.png'))

#Set screen, surface, caption etc.
size=(1080,768)
screen=display.set_mode(size) 
display.set_caption('Dank Paint V1.0') 
screen.fill(BLACK)
running=True
straight=False
screen.blit(background,(0,0))


 

#Drawing all rectangles and pictures

#Tool and stamp areas
def areas():
    draw.rect(screen,BLACK,toolBorderRect)
    draw.rect(screen,RECTBG,toolRect)
    draw.rect(screen,BLACK,stampBorderRect)
    draw.rect(screen,RECTBG,stampRect)
    draw.rect(screen,BLACK,extraBorderRect)
    draw.rect(screen,RECTBG,extraRect)
    draw.rect(screen,BLACK,canvasBorderRect)
    draw.rect(screen,WHITE,canvasRect)

#tool boxes
def tools():
    draw.rect(screen,BLACK,infoRect)
    draw.rect(screen,BLACK,pencilRect)
    draw.rect(screen,BLACK,brushRect)
    draw.rect(screen,BLACK,sprayRect)
    draw.rect(screen,BLACK,fillRect)
    draw.rect(screen,BLACK,rectRect)
    draw.rect(screen,BLACK,rectFillRect)
    draw.rect(screen,BLACK,ellipseRect)
    draw.rect(screen,BLACK,ellipseFillRect)
    draw.rect(screen,BLACK,eraserRect)
    draw.rect(screen,BLACK,eyedropRect)


#Misc Tools
def misc():
    draw.rect(screen,BLACK,saveRect)
    draw.rect(screen,BLACK,openRect)
    draw.rect(screen,BLACK,undoRect)
    draw.rect(screen,BLACK,redoRect)
    draw.rect(screen,BLACK,clearRect)

#Colours/Palette
def colours():
    draw.rect(screen,BLACK,paletteRect)
    screen.blit(colPalette,(805,15))
    

    draw.rect(screen,BLACK,redRectBorder)
    draw.rect(screen,RED,redRect)
    draw.rect(screen,BLACK,orangeRectBorder)
    draw.rect(screen,ORANGE,orangeRect)
    draw.rect(screen,BLACK,yellowRectBorder)
    draw.rect(screen,YELLOW,yellowRect)
    draw.rect(screen,BLACK,greenRectBorder)
    draw.rect(screen,GREEN,greenRect)
    draw.rect(screen,BLACK,blueRectBorder)
    draw.rect(screen,BLUE,blueRect)
    draw.rect(screen,BLACK,purpleRectBorder)
    draw.rect(screen,PURPLE,purpleRect)
    draw.rect(screen,BLACK,blackRectBorder)
    draw.rect(screen,BLACK,blackRect)
    draw.rect(screen,BLACK,whiteRectBorder)
    draw.rect(screen,WHITE,whiteRect)

    screen.blit(fontSmall.render('1',True,BLACK),(734,10))
    screen.blit(fontSmall.render('2',True,BLACK),(774,10))
    screen.blit(fontSmall.render('3',True,BLACK),(734,100))
    screen.blit(fontSmall.render('4',True,BLACK),(774,100))


def stamp():
    screen.blit(stamps[0],(40,310,80,80))
    screen.blit(stamps[1],(140,310,80,80))
    screen.blit(stamps[2],(40,400,80,80))
    screen.blit(stamps[3],(140,450,80,80))
    screen.blit(stamps[4],(40,540,80,80))
    screen.blit(stamps[5],(140,540,80,80))
    screen.blit(stamps[6],(40,660,80,80))
    screen.blit(stamps[7],(140,660,80,80))


def icons():
    draw.rect(screen,BLACK,pencilRect)
    draw.rect(screen,BLACK,brushRect)
    draw.rect(screen,BLACK,sprayRect)
    draw.rect(screen,BLACK,fillRect)
    draw.rect(screen,BLACK,eraserRect)
    draw.rect(screen,BLACK,rectRect)
    draw.rect(screen,BLACK,rectFillRect)
    draw.rect(screen,BLACK,ellipseRect)
    draw.rect(screen,BLACK,ellipseFillRect)
    draw.rect(screen,BLACK,lineRect)
    draw.rect(screen,BLACK,eyedropRect)

    screen.blit(save,(32,27))
    screen.blit(openI,(82,27))
    screen.blit(redo,(12,77))
    screen.blit(undo,(62,77))
    screen.blit(clear,(112,77))

    
#Default Settings (Pencil and Black colour)
tool='pencil'
col=BLACK   #Default colour
omx,omy=300,300 #Will be used for pencil tool
thickness=1 #thickness can be changed via mouse wheel or up/down keys
copy=screen.subsurface(canvasRect).copy()
undoList=[]  #Undo list always starts with a blank copy of the canvas
redoList=[]  #Redo list is empty
stampTools=['0','1','2','3','4','5','6','7'] #All stamp tool names for easy stamp access
music='unpaused'            #State of music
opacity=40                  #Default opacity
colNum=1                    #Default selected colour
colList=[BLACK,WHITE,WHITE,WHITE] #Default for each saved colour
newUndo=1  #Flag indicating if there is a new item in the undo list (Reduces lag for filters)


screen.blit(background,(0,0))
screen.blit(logo,(0,130))
areas()
tools()
misc()
colours()         #Using functions to draw many objects
stamp()
copy=screen.subsurface(canvasRect).copy() #Copy of the blank canvas for the undo function
undoList.append(copy)


while running:
    mx,my=mouse.get_pos()   #Get mouse pos every frame
    mb=mouse.get_pressed()  #Shortcut
    if not canvasRect.collidepoint(mx,my): #Sets mouse to standard arrow if not in the canvas
        mouse.set_cursor(*cursors.arrow)

    eraserHead=Surface((2*thickness,2*thickness),SRCALPHA)
    draw.circle(eraserHead,(255,255,255,opacity),[thickness,thickness],thickness)  #Transparent eraser surface
    
    brushHead=Surface((2*thickness,2*thickness),SRCALPHA)
    bCol=list(colList[colNum-1])                                    #Waterbrush surface  (Updates every tick to refresh colour)
    bCol[3]=opacity
    draw.circle(brushHead,bCol,[thickness,thickness],thickness)


    for evt in event.get():

        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONUP:
            if evt.button==1 and tool!='eyedrop' and canvasRect.collidepoint(mx,my) or clearRect.collidepoint(mx,my) :
                undoCopy=screen.subsurface(canvasRect).copy()       #If the left click is released and it's in the canvas with any tool that can make changes (Ie. everything except color picker)
                undoList.append(undoCopy)                           #save a picture of the canvas to the undo list (Will always be different to the picture before since every tool except color picker...
                newUndo=1                                            #...Makes changes

            elif evt.button==3 and canvasRect.collidepoint(mx,my) and tool!='eyedrop':
                undoCopy=screen.subsurface(canvasRect).copy()       #If the right click is released and it's in the canvas with any tool that can make changes (Ie. everything except color picker)
                undoList.append(undoCopy)
                newUndo=1  #Indicates there is a new item in the undo list and that the filters must refresh
                
        if evt.type==MOUSEBUTTONDOWN:
          
            copy=screen.subsurface(canvasRect).copy()#used for drawing shapes and stamps
            startx,starty=mouse.get_pos()   #Stores shape starting points
            if evt.button==4 and thickness<15:  #Thickness ranges between 1 and 15 
                thickness+=1                    #Mouse wheel up increases and mouse wheel down decreases
            if evt.button==5 and thickness>1:
                thickness-=1

            if undoRect.collidepoint(mx,my) and evt.button==1 and len(undoList)>1: #If undoRect is left clicked and the undo list is greater than 1 (Ie. blank + at least 1 more pic)           
                cUndo=undoList.pop()             #Pop out the last element
                screen.blit(undoList[-1],(275,160))  #Blit out the now last one (Previously the second last)
                redoList.append(cUndo)                #Append to redo list in case the user wants to redo)
                copy=screen.subsurface(canvasRect).copy()
                newUndo=1
                
            if redoRect.collidepoint(mx,my) and evt.button==1 and len(redoList)>0: #If the redoRect is left clicked and the redo list is greater than 0 (Ie. Has an element)
                screen.blit(redoList[-1],(275,160))   #Blit out the last element
                cRedo=redoList.pop()                  #Pop the blited image out
                undoList.append(cRedo)                #Append to undoList in case the user wants to undo
                copy=screen.subsurface(canvasRect).copy()
                newUndo=1

            if musicRect.collidepoint(mx,my) and evt.button==1:
                if mixer.music.get_busy()==0:
                    mixer.music.load('Songs/song0.mp3')   #plays the music initially (Since busy will always be true after the initial click)
                    mixer.music.play(-1) #loops infinitely
                elif mixer.music.get_busy()==1 and music=='unpaused':    #(Pause)
                    mixer.music.pause()
                    music='paused'
                elif mixer.music.get_busy()==1 and music=='paused':  #(Unpause)
                    mixer.music.unpause()
                    music='unpaused'
                           
        if evt.type==KEYDOWN:
            if evt.key==K_UP and thickness<15:
                thickness+=1                             #Thickness is also changable with arrow keys
            if evt.key==K_DOWN and thickness>1:          #Up/down to change by 1 and left/right to change by 5
                thickness-=1
            if evt.key==K_LEFT and thickness>6:
                thickness-=5
            if evt.key==K_RIGHT and thickness<9:
                thickness+=5
            if evt.key==K_LSHIFT:                   #Holding shift will allow to draw perfect circles, straight lines, etc
                straight=True
            if evt.key==K_EQUALS:
                if straight and opacity<255: #Opacity changes with + and - keys
                    opacity+=1
                elif opacity<245:
                    opacity+=10
            if evt.key==K_MINUS:
                if straight and opacity>1:
                    opacity-=1
                elif opacity>10:
                    opacity-=10
            if tool in stampTools and evt.key==K_ESCAPE:
                screen.blit(undoList[-1],(275,160))
                tool='pencil'
                    
                
                
            if evt.key==K_1:
                colNum=1
            if evt.key==K_2:
                colNum=2                #Current colour can be changed to one of 4 saved colours either by clicking or using the number keys
            if evt.key==K_3:
                colNum=3
            if evt.key==K_4:
                colNum=4

            
                
        if evt.type==KEYUP:
            if evt.key==K_LSHIFT:     #Sets straight flag to false when the user does not want perfect lines, cercles, etc.
                straight=False

        
        #Filters (Placed here because it should only run once per click instead of 60x/second)
        if filterRect.collidepoint(mx,my) and mb[0]==1:  #Sepia
            for x in range(275,1026):                                         #For every pixel in the canvas, apply the filter
                for y in range(160,611):
                    r,g,b,a=screen.get_at((x,y))   
                    r2=min(255,int(r*.393+g*.769+b*.189))
                    g2=min(255,int(r*.349+g*.686+b*.168))
                    b2=min(255,int(r*.272+g*.534+b*.131))
                    screen.set_at((x,y),(r2,g2,b2))
            copy=screen.subsurface(canvasRect).copy()
            undoList.append(copy)                  #Append a copy of the screen so it can be undoed
            newUndo=1

        if filterRect2.collidepoint(mx,my) and mb[0]==1:  #Grayscale
            for x in range(275,1026): 
                for y in range(160,611):
                    r,g,b,a=screen.get_at((x,y))   
                    c2=min(255,0.21*r+0.72*g+0.07*b)
                    screen.set_at((x,y),(c2,c2,c2))
            copy=screen.subsurface(canvasRect).copy()
            undoList.append(copy)
            newUndo=1

        if filterRect3.collidepoint(mx,my) and mb[0]==1:  #Invert colours)
            for x in range(275,1026): 
                for y in range(160,611):
                    r,g,b,a=screen.get_at((x,y))   
                    r2=255-r
                    g2=255-g
                    b2=255-b
                    screen.set_at((x,y),(r2,g2,b2))

            copy=screen.subsurface(canvasRect).copy()
            undoList.append(copy)
            newUndo=1

        if filterRect4.collidepoint(mx,my) and mb[0]==1:    #Pixelate
            smallCanvas=transform.scale(screen.subsurface(canvasRect),(175,105))
            largeCanvas=transform.scale(smallCanvas,(750,450))                      #Shrink the canvas and blow it back up for pixelation
            screen.blit(largeCanvas,(275,160))
            
            copy=screen.subsurface(canvasRect).copy()
            undoList.append(copy)
        
        
                
    if canvasRect.collidepoint(mx,my) and mb[0]==1 and tool!='eyedrop': #If a change is made on the screen, clear the redo list (Same as MS Paint)
        redoList=[]                                                     # Switching between undo and redo can result in different snapshots to be displayed in an odd placement 
                                                                       



    #Event Set up
    icons()
    
    if tool=='pencil':
        draw.rect(screen,RED,pencilRect)
        screen.blit(pencil2,(432,17))
        screen.blit(pencilHover,(210,20))
    if tool=='brush':                                           #If tool is __________
        draw.rect(screen,RED,brushRect)                         #Draw a red border around the tool image to display it is selected
        screen.blit(brush2,(482,17))                            #blit the pressed down picture to indicate it is selected
        screen.blit(brushHover,(210,20))                        #Blit the tool tip picture in the infoRect for information
    if tool=='spray':
        draw.rect(screen,RED,sprayRect)
        screen.blit(spray2,(532,17))
        screen.blit(sprayHover,(210,20))
    if tool=='fill':                                                            #etc.
        draw.rect(screen,RED,fillRect)
        screen.blit(bucket2,(582,17))
        screen.blit(fillHover,(210,20))
    if tool=='eraser':
        draw.rect(screen,RED,eraserRect)
        screen.blit(eraser2,(632,17))
        screen.blit(eraserHover,(210,20))
    if tool=='rect':
        draw.rect(screen,RED,rectRect)
        screen.blit(rect2,(432,67))
        screen.blit(rectHover,(210,20))
    if tool=='rectFill':
        draw.rect(screen,RED,rectFillRect)
        screen.blit(rectFill2,(482,67))
        screen.blit(rectFillHover,(210,20))
    if tool=='ellipse':
        draw.rect(screen,RED,ellipseRect)
        screen.blit(ellipse2,(532,67))
        screen.blit(ellipseHover,(210,20))
    if tool=='ellipseFill':
        draw.rect(screen,RED,ellipseFillRect)
        screen.blit(ellipseFill2,(582,67))
        screen.blit(ellipseFillHover,(210,20))
    if tool=='line':
        draw.rect(screen,RED,lineRect)
        screen.blit(line2,(632,67))
        screen.blit(lineHover,(210,20))
    if tool=='eyedrop':
        draw.rect(screen,RED,eyedropRect)
        screen.blit(dropper2,(682,47))
        screen.blit(dropperHover,(210,20))

    
    ##Selecting Buttons
    #Tools
    if pencilRect.collidepoint(mx,my):          #If the mouse is in the tool rect:
        screen.blit(pencil2,(432,17))           #blit the pressed down picture
        screen.blit(pencilHover,(210,20))       #Blit the tool tips picture
        if mb[0]==1:                            #If the user clicks on the tool: 
            draw.rect(screen,RED,pencilRect)    #Draw a red rect to indicate it has been pressed     (Without this code, a frame delay is somewhat noticible on 144Hz moniters)
            screen.blit(pencil2,(432,17))       #blit the pressed down pic to indicate it has been selected    ^^
            tool='pencil'                       #Change tool to ___________
    if not pencilRect.collidepoint(mx,my):      #If the mouse is not in the tool rect:  
        screen.blit(pencil,(432,17))            #Blit the normal pic for the tool
        
    if brushRect.collidepoint(mx,my):
        screen.blit(brush2,(482,17))
        screen.blit(brushHover,(210,20))
        if mb[0]==1:                                                #etc.
            draw.rect(screen,RED,brushRect)
            screen.blit(brush2,(482,17))
            tool='brush'
    if not brushRect.collidepoint(mx,my):
        screen.blit(brush,(482,17))
        
    if sprayRect.collidepoint(mx,my):
        screen.blit(spray2,(532,17))
        screen.blit(sprayHover,(210,20))
        if mb[0]==1:                                            
            draw.rect(screen,RED,sprayRect)
            screen.blit(spray2,(532,17))
            tool='spray'
    if not sprayRect.collidepoint(mx,my):
        screen.blit(spray,(532,17))
        
    if fillRect.collidepoint(mx,my):
        screen.blit(bucket2,(582,17))
        screen.blit(fillHover,(210,20))
        if mb[0]==1:
            draw.rect(screen,RED,fillRect)
            screen.blit(bucket2,(582,17))
            tool='fill'
    if not fillRect.collidepoint(mx,my):
        screen.blit(bucket,(582,17))
        
    if rectRect.collidepoint(mx,my):
        screen.blit(rect2,(432,67))
        screen.blit(rectHover,(210,20))
        if mb[0]==1:
            draw.rect(screen,RED,rectRect)
            screen.blit(rect2,(432,67))
            tool='rect'
    if not rectRect.collidepoint(mx,my):
        screen.blit(rect,(432,67))
        
    if rectFillRect.collidepoint(mx,my):
        screen.blit(rectFill2,(482,67))
        screen.blit(rectFillHover,(210,20))
        if mb[0]==1:
            draw.rect(screen,RED,rectFillRect)
            screen.blit(rectFill2,(482,67))
            tool='rectFill'
    if not rectFillRect.collidepoint(mx,my):
        screen.blit(rectFill,(482,67))
        
    if eraserRect.collidepoint(mx,my):
        screen.blit(eraser2,(632,17))
        screen.blit(eraserHover,(210,20))
        if mb[0]==1:
            draw.rect(screen,RED,eraserRect)
            screen.blit(eraser2,(632,17))
            tool='eraser'
    if not eraserRect.collidepoint(mx,my):
        screen.blit(eraser,(632,17))
            
    if ellipseRect.collidepoint(mx,my):
        screen.blit(ellipse2,(532,67))
        screen.blit(ellipseHover,(210,20))
        if mb[0]==1:
            draw.rect(screen,RED,ellipseRect)
            screen.blit(ellipse2,(532,67))
            tool='ellipse'
    if not ellipseRect.collidepoint(mx,my):
        screen.blit(ellipse,(532,67))
            
    if ellipseFillRect.collidepoint(mx,my):
        screen.blit(ellipseFill2,(582,67))
        screen.blit(ellipseFillHover,(210,20))
        if mb[0]==1:
            draw.rect(screen,RED,ellipseFillRect)
            screen.blit(ellipseFill2,(582,67))
            tool='ellipseFill'
    if not ellipseFillRect.collidepoint(mx,my):
        screen.blit(ellipseFill,(582,67))
            
    if lineRect.collidepoint(mx,my):
        screen.blit(line2,(632,67))
        screen.blit(lineHover,(210,20))
        if mb[0]==1:
            draw.rect(screen,RED,lineRect)
            screen.blit(line2,(632,67))
            tool='line'
    if not lineRect.collidepoint(mx,my):
        screen.blit(line,(632,67))
            
    if eyedropRect.collidepoint(mx,my):
        screen.blit(dropper2,(682,47))
        screen.blit(dropperHover,(210,20))
        if mb[0]==1:
            draw.rect(screen,RED,eyedropRect)
            screen.blit(dropper2,(682,47))
            tool='eyedrop'
    if not eyedropRect.collidepoint(mx,my):
        screen.blit(dropper,(682,47))
    #Stamps
    if doritoRect.collidepoint(mx,my) and mb[0]==1:
        tool='0'                                            #Tool variable is shared since you cant use stamps and draw at the same time
    if dewRect.collidepoint(mx,my) and mb[0]==1:
        tool='1'
    if snoopRect.collidepoint(mx,my) and mb[0]==1:
        tool='2'
    if sanicRect.collidepoint(mx,my) and mb[0]==1:
        tool='3'                                          #Each stamp's tool is the same as its picture number for easy access
    if frogRect.collidepoint(mx,my) and mb[0]==1:
        tool='4'
    if shrekRect.collidepoint(mx,my) and mb[0]==1:
        tool='5'
    if glassesRect.collidepoint(mx,my) and mb[0]==1:
        tool='6'
    if hatRect.collidepoint(mx,my) and mb[0]==1:
        tool='7'
            
    #Colours
    if col1DisplayRect.collidepoint(mx,my) and mb[0]==1:
        colNum=1
    if col2DisplayRect.collidepoint(mx,my) and mb[0]==1:
        colNum=2                                                 #switch between the saved colours
    if col3DisplayRect.collidepoint(mx,my) and mb[0]==1:
        colNum=3
    if col4DisplayRect.collidepoint(mx,my) and mb[0]==1:
        colNum=4

    if colNum==1:
        draw.rect(screen,RED,col1DisplayRect)
    else:
        draw.rect(screen,BLACK,col1DisplayRect)
    if colNum==2:
        draw.rect(screen,RED,col2DisplayRect)                #If saved colour == ___:
    else:                                                    #Draw the red background to indicate it is selected
        draw.rect(screen,BLACK,col2DisplayRect)              #Other wise draw the black background
    if colNum==3:
        draw.rect(screen,RED,col3DisplayRect)
    else:
        draw.rect(screen,BLACK,col3DisplayRect)
    if colNum==4:
        draw.rect(screen,RED,col4DisplayRect)
    else:
        draw.rect(screen,BLACK,col4DisplayRect)
    
    draw.rect(screen,colList[0],col1Rect)
    draw.rect(screen,colList[1],col2Rect)                 #Shows the user the 4 saved colours
    draw.rect(screen,colList[2],col3Rect)
    draw.rect(screen,colList[3],col4Rect)
    
    
    if paletteRect.collidepoint(mx,my) and mb[0]==1:     #If left clicked in pallette, change the colour
        colList[colNum-1]=screen.get_at((mx,my))

    if redRect.collidepoint(mx,my) and mb[0]==1:               #IF left clicked in a predefined colour box:
        colList[colNum-1]=RED                                                                 #Change colours
    if orangeRect.collidepoint(mx,my) and mb[0]==1:
        colList[colNum-1]=ORANGE
    if yellowRect.collidepoint(mx,my) and mb[0]==1:
        colList[colNum-1]=YELLOW
    if greenRect.collidepoint(mx,my) and mb[0]==1:
        colList[colNum-1]=GREEN
    if blueRect.collidepoint(mx,my) and mb[0]==1:
        colList[colNum-1]=BLUE
    if purpleRect.collidepoint(mx,my) and mb[0]==1:
        colList[colNum-1]=PURPLE
    if blackRect.collidepoint(mx,my) and mb[0]==1:
        colList[colNum-1]=BLACK
    if whiteRect.collidepoint(mx,my) and mb[0]==1:
        colList[colNum-1]=WHITE
            

    #Using tools
    if canvasRect.collidepoint(mx,my): #If mouse is in the canvas, the user can only edit the canvas
        screen.set_clip(canvasRect)
        mouse.set_cursor(*cursors.tri_left)     #Sets cursor to tri_left when in the canvas. 
        
        if tool=='pencil' and mb[0]==1:                               #If tool is selected and left click, preform the action
                draw.line(screen,colList[colNum-1],[omx,omy],[mx,my],min(thickness,5)) #thickness locked between 1 and 5
                
        if tool=='brush':
            dx=mx-omx
            dy=my-omy
            dist=int(sqrt(dx**2+dy**2))
            if mb[0]==1:
                for i in range(1,dist+1):
                    cx=int(omx+i*dx/dist) 
                    cy=int(omy+i*dy/dist)
                    draw.circle(screen,colList[colNum-1],[cx,cy],thickness)
            if mb[2]==1: #Right click allows water brush
                for i in range(1,dist+1):
                    cx=int(omx+i*dx/dist) 
                    cy=int(omy+i*dy/dist)
                    screen.blit(brushHead,(cx-thickness,cy-thickness))
                       
       
        if tool=='spray':
            if mb[0]==1:
                for i in range(int(thickness*10/thickness*10)): #Controls speed
                    x=randint(thickness*-1-50,thickness+50)  #Random within x range (spray has large radius)
                    y=randint(thickness*-1-50,thickness+50)  #Random within y range
                    if (x**2+y**2)**0.5<thickness+7:     #If the distance is less than the thickness, the point is in the circle
                        draw.circle(screen,colList[colNum-1],[mx+x,my+y],0)  #Draw the circle
            if mb[2]==1: #Right mouse allows for blood spray/ drip spray
                for i in range(int(thickness*10/thickness*10)): 
                    x=randint(thickness*-1-50,thickness+50) 
                    y=randint(thickness*-1-50,thickness+50)  
                    if (x**2+y**2)**0.5<thickness+7:    
                        while colList[colNum-1]==screen.get_at((mx+x,my+y)):
                            try:
                                y+=10 #if the randomized pixel is already that colour,shift it down 10
                            except:
                                pass  #Prevents error when reaching the canvas border (similar to fill)
                        draw.circle(screen,colList[colNum-1],[mx+x,my+y],0)
                    
        if tool=='fill' and mb[0]==1:
            try:
                ocol=screen.get_at((mx,my)) #get colour at point of click
                if ocol!=colList[colNum-1]:           #If the colour selected is different than
                    cords=[[mx,my]]     #the colour on screen, create a list that houses cords that need to be checked
                while len(cords)>0:  #While there is something to check, run the loop
                    cx,cy=cords.pop()  #cx,cy becomes point in which we a currently checking

                    if canvasBorderRect.collidepoint(cx,cy) and not canvasRect.collidepoint(cx,cy):
                        continue  #Stops loop from trying to fill the border (Which it cant therefore getting stuck)
                    if screen.get_at((cx,cy))==ocol:  #if cx,cy has same colour as the point clicked:
                        screen.set_at((cx,cy),colList[colNum-1])  #Set cx,cy to be the colour selected
                        cords.append((cx-1,cy))
                        cords.append((cx+1,cy))
                        cords.append((cx,cy-1))   #Append the 4 pixels around cx,cy into the list to be checked
                        cords.append((cx,cy+1))
            except:
                pass
        

            
        if tool=='eraser':

            dx=mx-omx
            dy=my-omy
            dist=int(sqrt(dx**2+dy**2))
            if mb[0]==1:
                for i in range(1,dist+1):
                    cx=int(omx+i*dx/dist) 
                    cy=int(omy+i*dy/dist)
                    draw.circle(screen,WHITE,[cx,cy],thickness+5)     #Eraser always larger than pencil
            if mb[2]==1:  #Right click allows transparent eraser
                for i in range(1,dist+1):
                    cx=int(omx+i*dx/dist) 
                    cy=int(omy+i*dy/dist)
                    screen.blit(eraserHead,(cx-thickness,cy-thickness))
            
        if tool=='eyedrop' and mb[0]==1:
            colList[colNum-1]=screen.get_at((mx,my)) #Get a colour clicked on in the canvas
            

        if tool=='rect' and mb[0]==1:
            screen.blit(copy,(275,160))    #Keeps blitting old copies
            
            if straight:
                hypot=((mx-startx)**2+(my-starty)**2)**0.5 #Distance between starting point and mx,my
                sideLen=int(hypot/(2)**0.5)                #Uses the 1,1,root 2 triangle relationship
                if mx<startx and my<starty:
                    draw.rect(screen,colList[colNum-1],[startx,starty,-sideLen,-sideLen],thickness) #Top left (-,-)
                elif mx>startx and my<starty:
                    draw.rect(screen,colList[colNum-1],[startx,starty,sideLen,-sideLen],thickness)  #Top right (+,-)
                elif mx<startx and my>starty:
                    draw.rect(screen,colList[colNum-1],[startx,starty,-sideLen,sideLen],thickness)  #Bottom left (-,+)
                elif mx>startx and my>starty:
                    draw.rect(screen,colList[colNum-1],[startx,starty,sideLen,sideLen],thickness)   #Bottom right (+,+)
            else:
                if abs(mx-startx)<thickness*2 or abs(my-starty)<thickness*2:
                    draw.rect(screen,colList[colNum-1],[startx,starty,mx-startx,my-starty]) #if the distance is less than twice the thickness, the rect would seemed filled anyways (also wierd things happen)
                else:
                    for i in range(thickness):
                        if mx<startx and my<starty:
                            draw.rect(screen,colList[colNum-1],[startx-i,starty-i,mx-startx+2*i,my-starty+2*i],1) #Top left
                        if mx>startx and my>starty:
                            draw.rect(screen,colList[colNum-1],[startx+i,starty+i,mx-startx-2*i,my-starty-2*i],1) #Bottom Right
                        if mx>startx and my<starty:                                                                             #Rects are drawn diminishing by one pixel to prevent missing corners
                            draw.rect(screen,colList[colNum-1],[startx+i,starty-i,mx-startx-2*i,my-starty+2*i],1) #Top Right
                        if mx<startx and my>starty:
                            draw.rect(screen,colList[colNum-1],[startx-i,starty+i,mx-startx+2*i,my-starty-2*i],1) #Bottom left

        if tool=='rectFill' and mb[0]==1:
            screen.blit(copy,(275,160))
            
            if straight:
                hypot=((mx-startx)**2+(my-starty)**2)**0.5
                sideLen=int(hypot/(2)**0.5)
                if mx<startx and my<starty:
                    draw.rect(screen,colList[colNum-1],[startx,starty,-sideLen,-sideLen])
                elif mx>startx and my<starty:
                    draw.rect(screen,colList[colNum-1],[startx,starty,sideLen,-sideLen])  #Same as unfilled rect except the thickness variable is removed
                elif mx<startx and my>starty:
                    draw.rect(screen,colList[colNum-1],[startx,starty,-sideLen,sideLen])
                elif mx>startx and my>starty:
                    draw.rect(screen,colList[colNum-1],[startx,starty,sideLen,sideLen])
            else:
                draw.rect(screen,colList[colNum-1],[startx,starty,mx-startx,my-starty]) #Unfilled rects dont have missing corners

        if tool=='ellipse' and mb[0]==1:
            screen.blit(copy,(275,160))#Ellipse doesn't support negative side lengths (Width is greater than radius)
            if straight:
                try:
                    cenX=int((startx+mx)/2)  #Find coords for center of the circle (Midpoint between start coords and cursor)
                    cenY=int((starty+my)/2)                                 #Holding shift allows drawing of a circle
                    r=int(((cenX-startx)**2+(cenY-starty)**2)**0.5)  #radius (Distance between center and cursor
                    draw.circle(screen,colList[colNum-1],[cenX,cenY],r,thickness)
                except:
                    pass
            else:
                if abs(mx-startx)<thickness*2 or abs(my-starty)<thickness*2:      
                        draw.ellipse(screen,colList[colNum-1],(min(startx,mx),min(starty,my),abs(mx-startx),abs(my-starty)))    #When the ellipse of less than twice the thickness, it would seemed filled
                        
                else:                   #drawing the ellipse from the min value acts as normalizing the ellipse and the abs (distance from a point) represents conpensation for the shift (See ellipse logic)
                    draw.arc(screen,colList[colNum-1],(min(startx,mx),min(starty,my),abs(mx-startx),abs(my-starty)),0,100,thickness)     #draws a 100 radian arc to prevent 'holes' from only drawing the arc once
                                                                                                       
        if tool=='ellipseFill' and mb[0]==1:
            screen.blit(copy,(275,160))
            if straight:
                cenX=int((startx+mx)/2)
                cenY=int((starty+my)/2)                                 #Holding shift allows drawing of a circle
                r=int(((cenX-startx)**2+(cenY-starty)**2)**0.5)
                draw.circle(screen,colList[colNum-1],[cenX,cenY],r)
            else:
                draw.ellipse(screen,colList[colNum-1],[min(startx,mx),min(starty,my),abs(startx-mx),abs(starty-my)])      

        if tool=='line' and mb[0]==1:
            screen.blit(copy,(275,160))
            if straight:
                if abs(startx-mx)<abs(starty-my):
                    draw.line(screen,colList[colNum-1],[startx,starty],[startx,my],thickness) #y offset is larger creates vertical lines
                if abs(startx-mx)>abs(starty-my):                               #Holding shift allows drawing of striaght lines
                    draw.line(screen,colList[colNum-1],[startx,starty],[mx,starty],thickness) #x offset is larger creates horizontal lines
            else:
                draw.line(screen,colList[colNum-1],[startx,starty],[mx,my],thickness)  #Standard line

        if tool in stampTools:
            px,py=stampsSmall[int(tool)].get_rect().size            #px,py is the dimensions of each stamp (stands for position x, position y)
            screen.blit(copy,(275,160))
            screen.blit(stampsSmall[int(tool)],(mx-px/2,my-py/2))  #Blit at mouse - half of the size of the stamp to center on mouse

    
    if tool in stampTools and not canvasRect.collidepoint(mx,my) and invisRect.collidepoint(mx,my):
        screen.blit(copy,(275,160)) #Prevents stamps from getting 'stuck' when the mouse leaves the canvas without clicking
        
        
    screen.set_clip(None) #Everything can be modified(after draw)

    #Misc tools (Save and open)
    if saveRect.collidepoint(mx,my):
        screen.blit(save2,(32,27))
        screen.blit(saveHover,(210,20))
        if mb[0]==1:
            try:
                fname=filedialog.asksaveasfilename(defaultextension='.png')   
                image.save(screen.subsurface(canvasRect),fname)
            except:
                pass
    if openRect.collidepoint(mx,my):
        screen.blit(openI2,(82,27))
        screen.blit(openHover,(210,20))
        if mb[0]==1:
            screen.set_clip(canvasRect)
            try:
                fname=filedialog.askopenfilename(filetypes=[('Images','*.png;*.jpg;*.jpeg;*.bmp')])
                img=image.load(fname)
                screen.blit(img,(275,160))
                copy=screen.subsurface(canvasRect).copy()
                undoList.append(copy)
                
                
            except:
                pass
                
    if redoRect.collidepoint(mx,my):
        screen.blit(redo2,(12,77))
        screen.blit(redoHover,(210,20))
    if undoRect.collidepoint(mx,my):
        screen.blit(undo2,(62,77))
        screen.blit(undoHover,(210,20))
    if clearRect.collidepoint(mx,my):
        screen.blit(clear2,(112,77))
        screen.blit(clearHover,(210,20))
        if mb[0]==1:
            draw.rect(screen,WHITE,canvasRect) #Fills canvas with white
            copy=screen.subsurface(canvasRect).copy()   
            
    

    if newUndo==1:  #Only activates when there is a new item in the undoList
        sepiaPre=transform.smoothscale(undoList[-1],(175,105))                  #filterPre=transform the last item in the undoList into 175x105 
        screen.blit(sepiaPre,(285,635))                                         #Blit it
        for x in range(285,460):    
                for y in range(635,740):
                    r,g,b,a=screen.get_at((x,y))   
                    r2=min(255,int(r*.393+g*.769+b*.189))                       #Apply the filter to the scaled down surface
                    g2=min(255,int(r*.349+g*.686+b*.168))
                    b2=min(255,int(r*.272+g*.534+b*.131))
                    screen.set_at((x,y),(r2,g2,b2))

        grayscalePre=transform.smoothscale(undoList[-1],(175,105))
        screen.blit(grayscalePre,(470,635))
        for x in range(470,645): 
                for y in range(635,740):
                    r,g,b,a=screen.get_at((x,y))   
                    c2=min(255,0.21*r+0.72*g+0.07*b)
                    screen.set_at((x,y),(c2,c2,c2))

        invertPre=transform.smoothscale(undoList[-1],(175,105))
        screen.blit(invertPre,(655,635))
        for x in range(655,830):
            for y in range(635,740):
                r,g,b,a=screen.get_at((x,y))
                r2=255-r
                g2=255-g
                b2=255-b
                screen.set_at((x,y),(r2,g2,b2))

        pixelPreSmall=transform.scale(undoList[-1],(80,60))         #shrink the canvas lots - smoothscale gives a fuzzy effect instead of a pixelated one
        pixelPre=transform.smoothscale(pixelPreSmall,(175,105))     #Blow it up to the size of the box
        screen.blit(pixelPre,(840,635))                             #Blit it
        

    newUndo=0  #Set flag to 0 so the loop wont repeat itself

                 
    omx,omy=mx,my
    display.update()
    draw.rect(screen,RECTBG,paintSizeRect) #Refreshes the thickness/opacity counters
    screen.blit(fontLarge.render('Thickness: '+str(thickness),True,BLACK),(415,115))  #Blits the thickness/opacity
    screen.blit(fontLarge.render('Opacity: '+str(opacity),True,BLACK),(570,115))
    
quit()

