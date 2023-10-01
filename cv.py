import fileinput

fin = open("source.txt", "r")
fout = open("out.txt", "w")
fdebug = open("debug.txt", "w")

for line in fin.readlines():
    line = line.strip()
    

    if line == '' or line == '\n':
        continue
    fdebug.write(line)
    fdebug.write("\n")
    dd = False
    gg = False
    dott = False
    xx = 0
    dashh = 0
    hashh = False
    note = ''
    for char in line:
        if char.isdigit():
            note = char
        elif char == 'd':
            dd =True
        elif char == 'g':
            gg =True
        elif char == 'x':
            xx  = xx + 1
        elif char == '.':
            dott = True
        elif char == '-':
            dashh = dashh + 1
        elif char == '#':
            hashh = True

    if dd:
        fout.write('-')
    
    if gg:
        fout.write('+')
    
    if hashh:
        fout.write('#')
    
    fout.write(note)
    fout.write(' ')

    length = 1.0 / (2 ** xx)
    
    if dott:
        length = length * 1.5
    length = length + dashh * 1
    fout.write(str(length))
    fout.write('\n')

