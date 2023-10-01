from directkeys import PressKey, ReleaseKey, Z, U, I, O, H, J, K
import fileinput
import time

speed = 0.4

noteToKey = {
    1 : 0x2C,
    2 : 0x16,
    3 : 0x17,
    4 : 0x18,
    5 : 0x23,
    6 : 0x24,
    7 : 0x25,
    "#1" : 0x06,
    "#2" : 0x07,
    "#4" : 0x08,
    "#5" : 0x09,
    "#6" : 0x0A,
}

f = open("soviet march.txt", "r")

print("start")
time.sleep(3)

for line in f.readlines():
    line = line.strip()
    nums = line.split(' ')
    print(nums)
    note = nums[0]
    length = 0

    if len(note) == 0:
        continue

    if len(nums) < 2:
        length = speed * 0.5
    else:
        length = float(nums[1]) * speed
    
    print(length)

    if note[0] == '0':
        time.sleep(length)
        continue

    up = False
    down = False

    if note[0] == '+':
        up = True
        PressKey(0x2A)
        ReleaseKey(0x2A)
        note = note[1:]
        
    elif note[0] == '-':
        down = True
        PressKey(0x1D)
        ReleaseKey(0x1D)
        note = note[1:]
        

    if note[0] == '#':
        key = noteToKey[note[0:2]]
    else:
        note = int(note)
        key = noteToKey[note]

    print(note)
    

    PressKey(key)
    time.sleep(length)
    ReleaseKey(key)
    
    if up:
        PressKey(0x1D)
        ReleaseKey(0x1D)
    if down:
        PressKey(0x2A)
        ReleaseKey(0x2A)
