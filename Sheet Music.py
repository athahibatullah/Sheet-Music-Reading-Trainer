import sys
sys.path.insert(1,'Lib\site-packages') #to get all the package
import pygame
import pygame.midi
from pygame.locals import *
import Pianos
# import random
pygame.init()

pygame.midi.init()

input_id = pygame.midi.get_default_input_id()
i = pygame.midi.Input( input_id )

pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post

pygame.display.set_caption("Sheet Music Read")
screen = pygame.display.set_mode((1200, 700), RESIZABLE, 32)
font = pygame.font.Font('freesansbold.ttf', 32) 

black = (0,0,0)
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 

# text = font.render('Sheet Music Reading Trainer', True, green, blue) 
# textRect = text.get_rect()  

# textRect.center = (800 // 2, 300 // 2) 
#print(i)

NotelistSharp = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
NotelistFlat = ["A","B♭","B","C","D♭","D","E♭","E","F","G♭","G","A♭"]

going = True
posisix = 25
posisiy = 550
panjangtuts = 60
lebartuts = 11
tekan = True

for PianoObj in Pianos.list:
        print(str(PianoObj.noteid) + " " + PianoObj.color)

while going:
    screen.fill(white)
    #pygame.draw.rect(screen,blue,(25, 550, 1145, 100), 3)
    # while(bikin):
    for PianoObj in Pianos.list:
        if PianoObj.color == "white":
            if PianoObj.pressed:
                pygame.draw.rect(screen,green,(PianoObj.x,PianoObj.y,PianoObj.keylong,PianoObj.keywidth))
                pygame.draw.rect(screen,black,(PianoObj.x,PianoObj.y,PianoObj.keylong,PianoObj.keywidth),2)
            else:    
                pygame.draw.rect(screen,black,(PianoObj.x,PianoObj.y,PianoObj.keylong,PianoObj.keywidth),2)
        elif PianoObj.color == "black":
            if PianoObj.pressed:
                pygame.draw.rect(screen,green,(PianoObj.x,PianoObj.y,PianoObj.keylong,PianoObj.keywidth))
            else:    
                pygame.draw.rect(screen,black,(PianoObj.x,PianoObj.y,PianoObj.keylong,PianoObj.keywidth))
        # DrawPiano(colors,posisix,posisiy,lebartuts,panjangtuts)
        # posisix += 22
        # print(str(PianoObj.noteid) + " " +PianoObj.color)

    # posisix = 25

    # if(random.randint(0,9) == 3):
    #         pygame.draw.rect(screen,blue,(posisix+(22*random.randint(0,52)),posisiy,22,100))

    # pygame.draw.rect(screen,black,(50,550,30,100),2)
    #     bikins += 1 
    #     posisix += 20
    #     if(bikins == 52):
    #         bikin = False
    # bikin = True
    # screen.blit(text, textRect)
    events = event_get()
    for e in events:
        if e.type in [QUIT]:
                going = False
        if e.type in [KEYDOWN]:
                going = False
    if i.poll():
        # Note = i.read(10)
        # print(Note)
        NoteRead = i.read(10)
        # while(i.poll() ):
        NoteID = NoteRead[0][0][1]
        if NoteRead[0][0][2] != 0:
            # print ("full midi_events " + str(NoteRead))
            # print ("my midi note is " + str(NoteRead[0][0][1]))
            print(Pianos.NoteDecider(NoteRead[0][0][1]) + " " + str(NoteRead[0][0][1]))
            # print(i.read(10)[0][0][2])
            tekan = True
            Pianos.list[NoteID-21].pressed = True
            # print(Pianos.list[NoteID-21].color)
            # print(NoteID-21)
            # print(str(Pianos.list[NoteID-21].x) + " " + Pianos.list[NoteID-21].color)
            # DrawPiano(green,posisix,posisiy,lebartuts,panjangtuts)
        else:
            tekan = False
            Pianos.list[NoteID-21].pressed = False
            # DrawPiano(black,posisix,posisiy,lebartuts,panjangtuts)

    pygame.display.update()  

print("exit button clicked.")
i.close()
pygame.midi.quit()
pygame.quit()
exit()