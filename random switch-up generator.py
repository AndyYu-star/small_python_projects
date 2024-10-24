from random import randint
for a in range(10):
    switchnumber1 = randint(0,6)
    switchnumber2 = randint(0,6)
    switchnumber3 = randint(0,6)
    switchnumber4 = randint(0,6)
    switchnumber5 = randint(0,6)
    switchnumber6 = randint(0,6)
    switchnumber7 = randint(0,6)
    switchnumber8 = randint(0,6)
    switchnumber9 = randint(0,6)
    switchnumber10 = randint(0,6)
if switchnumber1 == 0:
    switch1 = ''
if switchnumber1 == 1:
    switch1 = 'swap'
if switchnumber1 == 2:
    switch1 = 'shift'
if switchnumber1 == 3:
    switch1 = 'spin'
if switchnumber1 == 4:
    switch1 = 'alter'
if switchnumber1 == 5:
    switch1 = 'change'
if switchnumber1 == 6:
    switch1 = 'twist'
if switchnumber2 == 0:
    switch2 = ''
if switchnumber2 == 1:
    switch2 = 'swap'
if switchnumber2 == 2:
    switch2 = 'shift'
if switchnumber2 == 3:
    switch2 = 'spin'
if switchnumber2 == 4:
    switch2 = 'alter'
if switchnumber2 == 5:
    switch2 = 'change'
if switchnumber2 == 6:
    switch2 = 'twist'
if switchnumber3 == 0:
    switch3 = ''
if switchnumber3 == 1:
    switch3 = 'swap'
if switchnumber3 == 2:
    switch3 = 'shift'
if switchnumber3 == 3:
    switch3 = 'spin'
if switchnumber3 == 4:
    switch3 = 'alter'
if switchnumber3 == 5:
    switch3 = 'change'
if switchnumber3 == 6:
    switch3 = 'twist'
if switchnumber4 == 0:
    switch4 = ''
if switchnumber4 == 1:
    switch4 = 'swap'
if switchnumber4 == 2:
    switch4 = 'shift'
if switchnumber4 == 3:
    switch4 = 'spin'
if switchnumber4 == 4:
    switch4 = 'alter'
if switchnumber4 == 5:
    switch4 = 'change'
if switchnumber4 == 6:
    switch4 = 'twist'
if switchnumber5 == 0:
    switch5 = ''
if switchnumber5 == 1:
    switch5 = 'swap'
if switchnumber5 == 2:
    switch5 = 'shift'
if switchnumber5 == 3:
    switch5 = 'spin'
if switchnumber5 == 4:
    switch5 = 'alter'
if switchnumber5 == 5:
    switch5 = 'change'
if switchnumber5 == 6:
    switch5 = 'twist'
if switchnumber6 == 0:
    switch6 = ''
if switchnumber6 == 1:
    switch6 = 'swap'
if switchnumber6 == 2:
    switch6 = 'shift'
if switchnumber6 == 3:
    switch6 = 'spin'
if switchnumber6 == 4:
    switch6 = 'alter'
if switchnumber6 == 5:
    switch6 = 'change'
if switchnumber6 == 6:
    switch6 = 'twist'
if switchnumber7 == 0:
    switch7 = ''
if switchnumber7 == 1:
    switch7 = 'swap'
if switchnumber7 == 2:
    switch7 = 'shift'
if switchnumber7 == 3:
    switch7 = 'spin'
if switchnumber7 == 4:
    switch7 = 'alter'
if switchnumber7 == 5:
    switch7 = 'change'
if switchnumber7 == 6:
    switch7 = 'twist'
if switchnumber8 == 0:
    switch8 = ''
if switchnumber8 == 1:
    switch8 = 'swap'
if switchnumber8 == 2:
    switch8 = 'shift'
if switchnumber8 == 3:
    switch8 = 'spin'
if switchnumber8 == 4:
    switch8 = 'alter'
if switchnumber8 == 5:
    switch8 = 'change'
if switchnumber8 == 6:
    switch8 = 'twist'
if switchnumber9 == 0:
    switch9 = ''
if switchnumber9 == 1:
    switch9 = 'swap'
if switchnumber9 == 2:
    switch9 = 'shift'
if switchnumber9 == 3:
    switch9 = 'spin'
if switchnumber9 == 4:
    switch9 = 'alter'
if switchnumber9 == 5:
    switch9 = 'change'
if switchnumber9 == 6:
    switch9 = 'twist'
if switchnumber10 == 0:
    switch10 = ''
if switchnumber10 == 1:
    switch10 = 'swap'
if switchnumber10 == 2:
    switch10 = 'shift'
if switchnumber10 == 3:
    switch10 = 'spin'
if switchnumber10 == 4:
    switch10 = 'alter'
if switchnumber10 == 5:
    switch10 = 'change'
if switchnumber10 == 6:
    switch10 = 'twist'
print('This is ' + switch1 + switch2 + switch3 + switch4 + switch5 + switch6 + switch7 + switch8 + switch9 + switch10 + ':')
frisk = 'Frisk'
toriel = 'Toriel'
ruinsDummy = 'Ruins Dummy'
napstablook = 'Napstablook'
sans = 'Sans'
papyrus = 'Papyrus'
monsterKid = 'Monster Kid'
undyne = 'Undyne'
gaster = 'Gaster'
madDummy = 'Mad Dummy'
riverPerson = 'River Person'
alphys = 'Alphys'
mettaton = 'Mettaton'
asgore = 'Asgore'
asriel = 'Asriel'
chara = 'Chara'
if switch1 == 'swap':
    friskx = frisk
    frisk = chara
    chara = friskx
    torielx = toriel
    toriel = asgore
    asgore = torielx
    ruinsDummyx = ruinsDummy
    ruinsDummy = madDummy
    madDummy = ruinsDummyx
    napstablookx = napstablook
    napstablook = mettaton
    mettaton = napstablookx
    sansx = sans
    sans = papyrus
    papyrus = sansx
    monsterKidx = monsterKid
    monsterKid = asriel
    asriel = monsterKidx
    undynex = undyne
    undyne = alphys
    alphys = undynex
    gasterx = gaster
    gaster = riverPerson
    riverPerson = gasterx
if switch1 == 'shift':
    undynex = undyne
    undyne = toriel
    toriel = papyrus
    papyrus = asriel
    asriel = napstablook
    napstablook = alphys
    alphys = asgore
    asgore = sans
    sans = chara
    chara = mettaton
    mettaton = undynex
if switch1 == 'spin':
    undynex = undyne
    undyne = mettaton
    mettaton = chara
    chara = sans
    sans = asgore
    asgore = alphys
    alphys = napstablook
    napstablook = asriel
    asriel = papyrus
    papyrus = toriel
    toriel = undynex
if switch1 == 'alter':
    torielx = toriel
    toriel = sans
    sans = torielx
    papyrusx = papyrus
    papyrus = asgore
    asgore = papyrusx
    gasterx = gaster
    gaster = asriel
    asriel = gasterx
if switch1 == 'change':
    torielx = toriel
    toriel = mettaton
    mettaton = torielx
    napstablookx = napstablook
    napstablook = asgore
    asgore = napstablookx
    sansx = sans
    sans = undyne
    undyne = sansx
    papyrusx = papyrus
    papyrus = alphys
    alphys = papyrusx
    charax = chara
    chara = asriel
    asriel = charax
if switch1 == 'twist':
    torielx = toriel
    toriel = mettaton
    mettaton = sans
    sans = alphys
    alphys = asriel
    asriel = madDummy
    madDummy = asgore
    asgore = napstablook
    napstablook = torielx
    papyrusx = papyrus
    papyrus = undyne
    undyne = chara
    chara = papyrusx
if switch2 == 'swap':
    friskx = frisk
    frisk = chara
    chara = friskx
    torielx = toriel
    toriel = asgore
    asgore = torielx
    ruinsDummyx = ruinsDummy
    ruinsDummy = madDummy
    madDummy = ruinsDummyx
    napstablookx = napstablook
    napstablook = mettaton
    mettaton = napstablookx
    sansx = sans
    sans = papyrus
    papyrus = sansx
    monsterKidx = monsterKid
    monsterKid = asriel
    asriel = monsterKidx
    undynex = undyne
    undyne = alphys
    alphys = undynex
    gasterx = gaster
    gaster = riverPerson
    riverPerson = gasterx
if switch2 == 'shift':
    undynex = undyne
    undyne = toriel
    toriel = papyrus
    papyrus = asriel
    asriel = napstablook
    napstablook = alphys
    alphys = asgore
    asgore = sans
    sans = chara
    chara = mettaton
    mettaton = undynex
if switch2 == 'spin':
    undynex = undyne
    undyne = mettaton
    mettaton = chara
    chara = sans
    sans = asgore
    asgore = alphys
    alphys = napstablook
    napstablook = asriel
    asriel = papyrus
    papyrus = toriel
    toriel = undynex
if switch2 == 'alter':
    torielx = toriel
    toriel = sans
    sans = torielx
    papyrusx = papyrus
    papyrus = asgore
    asgore = papyrusx
    gasterx = gaster
    gaster = asriel
    asriel = gasterx
if switch2 == 'change':
    torielx = toriel
    toriel = mettaton
    mettaton = torielx
    napstablookx = napstablook
    napstablook = asgore
    asgore = napstablookx
    sansx = sans
    sans = undyne
    undyne = sansx
    papyrusx = papyrus
    papyrus = alphys
    alphys = papyrusx
    charax = chara
    chara = asriel
    asriel = charax
if switch2 == 'twist':
    torielx = toriel
    toriel = mettaton
    mettaton = sans
    sans = alphys
    alphys = asriel
    asriel = madDummy
    madDummy = asgore
    asgore = napstablook
    napstablook = torielx
    papyrusx = papyrus
    papyrus = undyne
    undyne = chara
    chara = papyrusx
if switch3 == 'swap':
    friskx = frisk
    frisk = chara
    chara = friskx
    torielx = toriel
    toriel = asgore
    asgore = torielx
    ruinsDummyx = ruinsDummy
    ruinsDummy = madDummy
    madDummy = ruinsDummyx
    napstablookx = napstablook
    napstablook = mettaton
    mettaton = napstablookx
    sansx = sans
    sans = papyrus
    papyrus = sansx
    monsterKidx = monsterKid
    monsterKid = asriel
    asriel = monsterKidx
    undynex = undyne
    undyne = alphys
    alphys = undynex
    gasterx = gaster
    gaster = riverPerson
    riverPerson = gasterx
if switch3 == 'shift':
    undynex = undyne
    undyne = toriel
    toriel = papyrus
    papyrus = asriel
    asriel = napstablook
    napstablook = alphys
    alphys = asgore
    asgore = sans
    sans = chara
    chara = mettaton
    mettaton = undynex
if switch3 == 'spin':
    undynex = undyne
    undyne = mettaton
    mettaton = chara
    chara = sans
    sans = asgore
    asgore = alphys
    alphys = napstablook
    napstablook = asriel
    asriel = papyrus
    papyrus = toriel
    toriel = undynex
if switch3 == 'alter':
    torielx = toriel
    toriel = sans
    sans = torielx
    papyrusx = papyrus
    papyrus = asgore
    asgore = papyrusx
    gasterx = gaster
    gaster = asriel
    asriel = gasterx
if switch3 == 'change':
    torielx = toriel
    toriel = mettaton
    mettaton = torielx
    napstablookx = napstablook
    napstablook = asgore
    asgore = napstablookx
    sansx = sans
    sans = undyne
    undyne = sansx
    papyrusx = papyrus
    papyrus = alphys
    alphys = papyrusx
    charax = chara
    chara = asriel
    asriel = charax
if switch3 == 'twist':
    torielx = toriel
    toriel = mettaton
    mettaton = sans
    sans = alphys
    alphys = asriel
    asriel = madDummy
    madDummy = asgore
    asgore = napstablook
    napstablook = torielx
    papyrusx = papyrus
    papyrus = undyne
    undyne = chara
    chara = papyrusx
if switch4 == 'swap':
    friskx = frisk
    frisk = chara
    chara = friskx
    torielx = toriel
    toriel = asgore
    asgore = torielx
    ruinsDummyx = ruinsDummy
    ruinsDummy = madDummy
    madDummy = ruinsDummyx
    napstablookx = napstablook
    napstablook = mettaton
    mettaton = napstablookx
    sansx = sans
    sans = papyrus
    papyrus = sansx
    monsterKidx = monsterKid
    monsterKid = asriel
    asriel = monsterKidx
    undynex = undyne
    undyne = alphys
    alphys = undynex
    gasterx = gaster
    gaster = riverPerson
    riverPerson = gasterx
if switch4 == 'shift':
    undynex = undyne
    undyne = toriel
    toriel = papyrus
    papyrus = asriel
    asriel = napstablook
    napstablook = alphys
    alphys = asgore
    asgore = sans
    sans = chara
    chara = mettaton
    mettaton = undynex
if switch4 == 'spin':
    undynex = undyne
    undyne = mettaton
    mettaton = chara
    chara = sans
    sans = asgore
    asgore = alphys
    alphys = napstablook
    napstablook = asriel
    asriel = papyrus
    papyrus = toriel
    toriel = undynex
if switch4 == 'alter':
    torielx = toriel
    toriel = sans
    sans = torielx
    papyrusx = papyrus
    papyrus = asgore
    asgore = papyrusx
    gasterx = gaster
    gaster = asriel
    asriel = gasterx
if switch4 == 'change':
    torielx = toriel
    toriel = mettaton
    mettaton = torielx
    napstablookx = napstablook
    napstablook = asgore
    asgore = napstablookx
    sansx = sans
    sans = undyne
    undyne = sansx
    papyrusx = papyrus
    papyrus = alphys
    alphys = papyrusx
    charax = chara
    chara = asriel
    asriel = charax
if switch4 == 'twist':
    torielx = toriel
    toriel = mettaton
    mettaton = sans
    sans = alphys
    alphys = asriel
    asriel = madDummy
    madDummy = asgore
    asgore = napstablook
    napstablook = torielx
    papyrusx = papyrus
    papyrus = undyne
    undyne = chara
    chara = papyrusx
if switch5 == 'swap':
    friskx = frisk
    frisk = chara
    chara = friskx
    torielx = toriel
    toriel = asgore
    asgore = torielx
    ruinsDummyx = ruinsDummy
    ruinsDummy = madDummy
    madDummy = ruinsDummyx
    napstablookx = napstablook
    napstablook = mettaton
    mettaton = napstablookx
    sansx = sans
    sans = papyrus
    papyrus = sansx
    monsterKidx = monsterKid
    monsterKid = asriel
    asriel = monsterKidx
    undynex = undyne
    undyne = alphys
    alphys = undynex
    gasterx = gaster
    gaster = riverPerson
    riverPerson = gasterx
if switch5 == 'shift':
    undynex = undyne
    undyne = toriel
    toriel = papyrus
    papyrus = asriel
    asriel = napstablook
    napstablook = alphys
    alphys = asgore
    asgore = sans
    sans = chara
    chara = mettaton
    mettaton = undynex
if switch5 == 'spin':
    undynex = undyne
    undyne = mettaton
    mettaton = chara
    chara = sans
    sans = asgore
    asgore = alphys
    alphys = napstablook
    napstablook = asriel
    asriel = papyrus
    papyrus = toriel
    toriel = undynex
if switch5 == 'alter':
    torielx = toriel
    toriel = sans
    sans = torielx
    papyrusx = papyrus
    papyrus = asgore
    asgore = papyrusx
    gasterx = gaster
    gaster = asriel
    asriel = gasterx
if switch5 == 'change':
    torielx = toriel
    toriel = mettaton
    mettaton = torielx
    napstablookx = napstablook
    napstablook = asgore
    asgore = napstablookx
    sansx = sans
    sans = undyne
    undyne = sansx
    papyrusx = papyrus
    papyrus = alphys
    alphys = papyrusx
    charax = chara
    chara = asriel
    asriel = charax
if switch5 == 'twist':
    torielx = toriel
    toriel = mettaton
    mettaton = sans
    sans = alphys
    alphys = asriel
    asriel = madDummy
    madDummy = asgore
    asgore = napstablook
    napstablook = torielx
    papyrusx = papyrus
    papyrus = undyne
    undyne = chara
    chara = papyrusx
if switch6 == 'swap':
    friskx = frisk
    frisk = chara
    chara = friskx
    torielx = toriel
    toriel = asgore
    asgore = torielx
    ruinsDummyx = ruinsDummy
    ruinsDummy = madDummy
    madDummy = ruinsDummyx
    napstablookx = napstablook
    napstablook = mettaton
    mettaton = napstablookx
    sansx = sans
    sans = papyrus
    papyrus = sansx
    monsterKidx = monsterKid
    monsterKid = asriel
    asriel = monsterKidx
    undynex = undyne
    undyne = alphys
    alphys = undynex
    gasterx = gaster
    gaster = riverPerson
    riverPerson = gasterx
if switch6 == 'shift':
    undynex = undyne
    undyne = toriel
    toriel = papyrus
    papyrus = asriel
    asriel = napstablook
    napstablook = alphys
    alphys = asgore
    asgore = sans
    sans = chara
    chara = mettaton
    mettaton = undynex
if switch6 == 'spin':
    undynex = undyne
    undyne = mettaton
    mettaton = chara
    chara = sans
    sans = asgore
    asgore = alphys
    alphys = napstablook
    napstablook = asriel
    asriel = papyrus
    papyrus = toriel
    toriel = undynex
if switch6 == 'alter':
    torielx = toriel
    toriel = sans
    sans = torielx
    papyrusx = papyrus
    papyrus = asgore
    asgore = papyrusx
    gasterx = gaster
    gaster = asriel
    asriel = gasterx
if switch6 == 'change':
    torielx = toriel
    toriel = mettaton
    mettaton = torielx
    napstablookx = napstablook
    napstablook = asgore
    asgore = napstablookx
    sansx = sans
    sans = undyne
    undyne = sansx
    papyrusx = papyrus
    papyrus = alphys
    alphys = papyrusx
    charax = chara
    chara = asriel
    asriel = charax
if switch6 == 'twist':
    torielx = toriel
    toriel = mettaton
    mettaton = sans
    sans = alphys
    alphys = asriel
    asriel = madDummy
    madDummy = asgore
    asgore = napstablook
    napstablook = torielx
    papyrusx = papyrus
    papyrus = undyne
    undyne = chara
    chara = papyrusx
if switch7 == 'swap':
    friskx = frisk
    frisk = chara
    chara = friskx
    torielx = toriel
    toriel = asgore
    asgore = torielx
    ruinsDummyx = ruinsDummy
    ruinsDummy = madDummy
    madDummy = ruinsDummyx
    napstablookx = napstablook
    napstablook = mettaton
    mettaton = napstablookx
    sansx = sans
    sans = papyrus
    papyrus = sansx
    monsterKidx = monsterKid
    monsterKid = asriel
    asriel = monsterKidx
    undynex = undyne
    undyne = alphys
    alphys = undynex
    gasterx = gaster
    gaster = riverPerson
    riverPerson = gasterx
if switch7 == 'shift':
    undynex = undyne
    undyne = toriel
    toriel = papyrus
    papyrus = asriel
    asriel = napstablook
    napstablook = alphys
    alphys = asgore
    asgore = sans
    sans = chara
    chara = mettaton
    mettaton = undynex
if switch7 == 'spin':
    undynex = undyne
    undyne = mettaton
    mettaton = chara
    chara = sans
    sans = asgore
    asgore = alphys
    alphys = napstablook
    napstablook = asriel
    asriel = papyrus
    papyrus = toriel
    toriel = undynex
if switch7 == 'alter':
    torielx = toriel
    toriel = sans
    sans = torielx
    papyrusx = papyrus
    papyrus = asgore
    asgore = papyrusx
    gasterx = gaster
    gaster = asriel
    asriel = gasterx
if switch7 == 'change':
    torielx = toriel
    toriel = mettaton
    mettaton = torielx
    napstablookx = napstablook
    napstablook = asgore
    asgore = napstablookx
    sansx = sans
    sans = undyne
    undyne = sansx
    papyrusx = papyrus
    papyrus = alphys
    alphys = papyrusx
    charax = chara
    chara = asriel
    asriel = charax
if switch7 == 'twist':
    torielx = toriel
    toriel = mettaton
    mettaton = sans
    sans = alphys
    alphys = asriel
    asriel = madDummy
    madDummy = asgore
    asgore = napstablook
    napstablook = torielx
    papyrusx = papyrus
    papyrus = undyne
    undyne = chara
    chara = papyrusx
if switch8 == 'swap':
    friskx = frisk
    frisk = chara
    chara = friskx
    torielx = toriel
    toriel = asgore
    asgore = torielx
    ruinsDummyx = ruinsDummy
    ruinsDummy = madDummy
    madDummy = ruinsDummyx
    napstablookx = napstablook
    napstablook = mettaton
    mettaton = napstablookx
    sansx = sans
    sans = papyrus
    papyrus = sansx
    monsterKidx = monsterKid
    monsterKid = asriel
    asriel = monsterKidx
    undynex = undyne
    undyne = alphys
    alphys = undynex
    gasterx = gaster
    gaster = riverPerson
    riverPerson = gasterx
if switch8 == 'shift':
    undynex = undyne
    undyne = toriel
    toriel = papyrus
    papyrus = asriel
    asriel = napstablook
    napstablook = alphys
    alphys = asgore
    asgore = sans
    sans = chara
    chara = mettaton
    mettaton = undynex
if switch8 == 'spin':
    undynex = undyne
    undyne = mettaton
    mettaton = chara
    chara = sans
    sans = asgore
    asgore = alphys
    alphys = napstablook
    napstablook = asriel
    asriel = papyrus
    papyrus = toriel
    toriel = undynex
if switch8 == 'alter':
    torielx = toriel
    toriel = sans
    sans = torielx
    papyrusx = papyrus
    papyrus = asgore
    asgore = papyrusx
    gasterx = gaster
    gaster = asriel
    asriel = gasterx
if switch8 == 'change':
    torielx = toriel
    toriel = mettaton
    mettaton = torielx
    napstablookx = napstablook
    napstablook = asgore
    asgore = napstablookx
    sansx = sans
    sans = undyne
    undyne = sansx
    papyrusx = papyrus
    papyrus = alphys
    alphys = papyrusx
    charax = chara
    chara = asriel
    asriel = charax
if switch8 == 'twist':
    torielx = toriel
    toriel = mettaton
    mettaton = sans
    sans = alphys
    alphys = asriel
    asriel = madDummy
    madDummy = asgore
    asgore = napstablook
    napstablook = torielx
    papyrusx = papyrus
    papyrus = undyne
    undyne = chara
    chara = papyrusx
if switch9 == 'swap':
    friskx = frisk
    frisk = chara
    chara = friskx
    torielx = toriel
    toriel = asgore
    asgore = torielx
    ruinsDummyx = ruinsDummy
    ruinsDummy = madDummy
    madDummy = ruinsDummyx
    napstablookx = napstablook
    napstablook = mettaton
    mettaton = napstablookx
    sansx = sans
    sans = papyrus
    papyrus = sansx
    monsterKidx = monsterKid
    monsterKid = asriel
    asriel = monsterKidx
    undynex = undyne
    undyne = alphys
    alphys = undynex
    gasterx = gaster
    gaster = riverPerson
    riverPerson = gasterx
if switch9 == 'shift':
    undynex = undyne
    undyne = toriel
    toriel = papyrus
    papyrus = asriel
    asriel = napstablook
    napstablook = alphys
    alphys = asgore
    asgore = sans
    sans = chara
    chara = mettaton
    mettaton = undynex
if switch9 == 'spin':
    undynex = undyne
    undyne = mettaton
    mettaton = chara
    chara = sans
    sans = asgore
    asgore = alphys
    alphys = napstablook
    napstablook = asriel
    asriel = papyrus
    papyrus = toriel
    toriel = undynex
if switch9 == 'alter':
    torielx = toriel
    toriel = sans
    sans = torielx
    papyrusx = papyrus
    papyrus = asgore
    asgore = papyrusx
    gasterx = gaster
    gaster = asriel
    asriel = gasterx
if switch9 == 'change':
    torielx = toriel
    toriel = mettaton
    mettaton = torielx
    napstablookx = napstablook
    napstablook = asgore
    asgore = napstablookx
    sansx = sans
    sans = undyne
    undyne = sansx
    papyrusx = papyrus
    papyrus = alphys
    alphys = papyrusx
    charax = chara
    chara = asriel
    asriel = charax
if switch9 == 'twist':
    torielx = toriel
    toriel = mettaton
    mettaton = sans
    sans = alphys
    alphys = asriel
    asriel = madDummy
    madDummy = asgore
    asgore = napstablook
    napstablook = torielx
    papyrusx = papyrus
    papyrus = undyne
    undyne = chara
    chara = papyrusx
if switch10 == 'swap':
    friskx = frisk
    frisk = chara
    chara = friskx
    torielx = toriel
    toriel = asgore
    asgore = torielx
    ruinsDummyx = ruinsDummy
    ruinsDummy = madDummy
    madDummy = ruinsDummyx
    napstablookx = napstablook
    napstablook = mettaton
    mettaton = napstablookx
    sansx = sans
    sans = papyrus
    papyrus = sansx
    monsterKidx = monsterKid
    monsterKid = asriel
    asriel = monsterKidx
    undynex = undyne
    undyne = alphys
    alphys = undynex
    gasterx = gaster
    gaster = riverPerson
    riverPerson = gasterx
if switch10 == 'shift':
    undynex = undyne
    undyne = toriel
    toriel = papyrus
    papyrus = asriel
    asriel = napstablook
    napstablook = alphys
    alphys = asgore
    asgore = sans
    sans = chara
    chara = mettaton
    mettaton = undynex
if switch10 == 'spin':
    undynex = undyne
    undyne = mettaton
    mettaton = chara
    chara = sans
    sans = asgore
    asgore = alphys
    alphys = napstablook
    napstablook = asriel
    asriel = papyrus
    papyrus = toriel
    toriel = undynex
if switch10 == 'alter':
    torielx = toriel
    toriel = sans
    sans = torielx
    papyrusx = papyrus
    papyrus = asgore
    asgore = papyrusx
    gasterx = gaster
    gaster = asriel
    asriel = gasterx
if switch10 == 'change':
    torielx = toriel
    toriel = mettaton
    mettaton = torielx
    napstablookx = napstablook
    napstablook = asgore
    asgore = napstablookx
    sansx = sans
    sans = undyne
    undyne = sansx
    papyrusx = papyrus
    papyrus = alphys
    alphys = papyrusx
    charax = chara
    chara = asriel
    asriel = charax
if switch10 == 'twist':
    torielx = toriel
    toriel = mettaton
    mettaton = sans
    sans = alphys
    alphys = asriel
    asriel = madDummy
    madDummy = asgore
    asgore = napstablook
    napstablook = torielx
    papyrusx = papyrus
    papyrus = undyne
    undyne = chara
    chara = papyrusx
print(frisk + ' is now the player.\n' + toriel + ' is now the caretaker of the ruins.\n' + ruinsDummy + ' is now the dummy in the ruins.\n' + napstablook + ' is now hiding in the ruins.\n' + sans + ' is now gonna give you a bad time.\n' + papyrus + ' now wants to be a royal guard.\n' + monsterKid + ' is now an armless kid.\n' + undyne + ' is now the captain of the royal guard.\n' + gaster + ' is now in the void.\n' + madDummy + ' is now going absolutely insane.\n' + riverPerson + ' now sails through the river.\n' + alphys + ' is now the royal scientist.\n' + mettaton + ' is now the only celebrity in the underground.\n' + asgore + ' is now the monarch of the underground.\n' + asriel + ' was killed and turned into a soulless being.\n' + chara + ' was killed and is now your narrator.')
