NotelistSharp = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
NotelistFlat = ["A","B♭","B","C","D♭","D","E♭","E","F","G♭","G","A♭"]

class Piano:
    def __init__(self, color, noteid, x, y ,keylong, keywidth, pressed):
        self.color = color
        self.noteid = noteid
        self.x = x
        self.y = y
        self.keylong = keylong
        self.keywidth = keywidth
        self.pressed = pressed

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
    
list = []

xpos = 25
ypos = 550
# for i in range(21,109):
#     if len(Piano.NoteDecider(i,i)) == 3:
#         list.append(Piano("black",i,25,550,11,60))
#     else:
#         list.append(Piano("white",i,25,xpos,11,60))
#     xpos += 22

for i in range(52):    
    if(i % 7 == 1):
        list.append(Piano("black",i,xpos-4,ypos,11,60,False))
        # print(str(j) + " " + str(i))
        # pygame.draw.rect(screen,colorr,(posisix-4,posisiy,lebartuts,panjangtuts))
    elif(i % 7 == 3 and i != 52):
        list.append(Piano("black",i,xpos-6,ypos,11,60,False))
        # pygame.draw.rect(screen,colorr,(posisix-6,posisiy,lebartuts,panjangtuts))
    elif(i % 7 == 4):
        list.append(Piano("black",i,xpos-4,ypos,11,60,False))
        # pygame.draw.rect(screen,colorr,(posisix-4,posisiy,lebartuts,panjangtuts))
    elif(i % 7 == 6):
        list.append(Piano("black",i,xpos-6,ypos,11,60,False))
        # pygame.draw.rect(screen,colorr,(posisix-6,posisiy,lebartuts,panjangtuts))
    elif(i % 7 == 0 and i != 0 ):
        list.append(Piano("black",i,xpos-5,ypos,11,60,False))
    list.append(Piano("white",i,xpos,ypos,22,100,False))
    xpos += 22

j = 0
for i in range(21,109):
    list[j].noteid = i
    j += 1

# for PianoObj in list:
#     print(str(PianoObj.noteid) + " " + PianoObj.color)
# for PianoObj in list:
#     print(str(PianoObj.noteid) + " " + PianoObj.color + " " +" " + PianoObj.NoteDecider(PianoObj.noteid))
# testobject = Piano("white",108,25,550,11,60)

# print(testobject.NoteDecider(testobject.noteid))