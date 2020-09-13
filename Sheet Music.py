import sys
sys.path.insert(1,'Lib\site-packages') #to get all the package
import pygame
import pygame.midi
from pygame.locals import *

pygame.init()

pygame.midi.init()

input_id = pygame.midi.get_default_input_id()
i = pygame.midi.Input( input_id )

pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post

pygame.display.set_caption("Sheet Music Read")
screen = pygame.display.set_mode((400, 300), RESIZABLE, 32)

#print(i)

NotelistSharp = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
def NoteDecider(Note):
    decrement = 0
    while Note >= 33:
        Note -= 12
        decrement += 1    
    Note -= 21
    Note = NotelistSharp[Note]
    return Note

going = True
while going:
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
        if NoteRead[0][0][2] != 0:
            # print ("full midi_events " + str(NoteRead))
            # print ("my midi note is " + str(NoteRead[0][0][1]))
            print(NoteDecider(NoteRead[0][0][1]))

print("exit button clicked.")
i.close()
pygame.midi.quit()
pygame.quit()
exit()