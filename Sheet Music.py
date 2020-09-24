import sys
sys.path.insert(1,'Lib\site-packages') #to get all the package
import pygame
import pygame.midi
from pygame.locals import *
import Piano
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

def NoteDecider(Note):
    if(Note >= 21 and Note <= 23):
        Note -= 21
        Note = NotelistSharp[Note] + "0"
    else:
        decrement = 1
        while Note >= 36:
            Note -= 12
            decrement += 1
        Note -= 33
        Note = NotelistSharp[Note] + str(decrement)
    return Note

# def DrawPiano(colorr,posisix,posisiy,lebartuts,panjangtuts):
#     pygame.draw.rect(screen,colorr,(posisix,posisiy,22,100),2)
#     if(j % 7 == 1):
#         pygame.draw.rect(screen,colorr,(posisix-4,posisiy,lebartuts,panjangtuts))
#     elif(j % 7 == 3):
#         pygame.draw.rect(screen,colorr,(posisix-6,posisiy,lebartuts,panjangtuts))
#     elif(j % 7 == 4):
#         pygame.draw.rect(screen,colorr,(posisix-4,posisiy,lebartuts,panjangtuts))
#     elif(j % 7 == 6):
#         pygame.draw.rect(screen,colorr,(posisix-6,posisiy,lebartuts,panjangtuts))
#     elif(j % 7 == 0 and j != 0):
#         pygame.draw.rect(screen,colorr,(posisix-5,posisiy,lebartuts,panjangtuts))

going = True
posisix = 25
posisiy = 550
panjangtuts = 60
lebartuts = 11
tekan = True
colors = black
while going:
    screen.fill(white)
    #pygame.draw.rect(screen,blue,(25, 550, 1145, 100), 3)
    # while(bikin):
    for PianoObj in Piano.list:
        # print(str(PianoObj.noteid) + " " + str(PianoObj.color) + " " + PianoObj.NoteDecider(PianoObj.noteid))
        if PianoObj.color == "white":
            pygame.draw.rect(screen,black,(PianoObj.x,PianoObj.y,PianoObj.keylong,PianoObj.keywidth),2)
        elif PianoObj.color == "black":
            pygame.draw.rect(screen,black,(PianoObj.x,PianoObj.y,PianoObj.keylong,PianoObj.keywidth))
        # DrawPiano(colors,posisix,posisiy,lebartuts,panjangtuts)
        # posisix += 22

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
        if NoteRead[0][0][2] != 0:
            # print ("full midi_events " + str(NoteRead))
            # print ("my midi note is " + str(NoteRead[0][0][1]))
            print(NoteDecider(NoteRead[0][0][1]) + " " + str(NoteRead[0][0][1]))
            # print(i.read(10)[0][0][2])
            tekan = True
            colors = green
            # DrawPiano(green,posisix,posisiy,lebartuts,panjangtuts)
        else:
            tekan = False
            colors = black
            # DrawPiano(black,posisix,posisiy,lebartuts,panjangtuts)

    pygame.display.update()  

print("exit button clicked.")
i.close()
pygame.midi.quit()
pygame.quit()
exit()