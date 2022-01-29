# OLD VERSION; I originally wanted to do smth specific, but I couldnt figure it out and I'm running out of time to complete this assignment so this is going to live here in case I come back to it 

"""
Name(s): my shoulder hurts this was a terribly inconvenient time to get booster shot
Name of Project: 
"""
import os
surname = input("Enter your surname to begin: ")

def start(): # COMPLETE
    os.system('clear')
    print("Hello Sergeant", surname + "! Colonel Mustang requires an audience with Major Elric. Howver, Major Elric seems to have disappeared! You have been given orders to find Major Elric. Talk to different people to see if anyone might know where he is. \n\nEnter 1 to accept the orders, enter 2 to reject the orders.")
    startchoice = input("\nEnter your choice: ")
    while startchoice != "1" and startchoice != "2":
        startchoice = input("\nInvalid answer. Enter your choice: ")
    if startchoice == "2":
        fail()
    if startchoice == "1":
        location()
def fail(): # COMPLETE
    print("\n__________ \n\nYou're fired! Good luck finding a new job :)")
    failchoice = input("\nEnter 1 to restart: ")
    while failchoice != "1":
        failchoice = input("\nInvalid answer. Enter 1 to restart: ")
    if failchoice == "1":
        start()
def location(): # COMPLETE
    os.system('clear')
    print("LOCATION:")
    print("\nEnter 1 for the main corridor, enter 2 for the reception area, enter 3 for the library, enter 4 for the mess hall.")
    loc = input("\nEnter your choice: ")
    while loc != "1" and loc != "2" and loc != "3" and loc != "4":
        loc = input("\nInvalid answer. Enter your choice: ")
    if loc == "1":
        corridor()
    elif loc == "2":
        reception()
    elif loc == "3":
        library()
    elif loc == "4":
        mess()
def corridor(): # COMPLETE
    os.system('clear')
    print("LOCATION: MAIN CORRIDOR")
    print("\nYou see Sergeant Brosh, Warrant Officer Falman, and Major Armstrong walking through the corridor. \n\nEnter 1 to approach Sergeant Brosh, enter 2 to approach Warrant Officer Falman, enter 3 to approach Major Armstrong, enter 4 to leave the main corridor.")
    corchoice = input("\nEnter your choice: ")
    while corchoice != "1" and corchoice != "2" and corchoice != "3" and corchoice != "4":
        corchoice = input("\nInvalid answer. Enter your choice: ")
    if corchoice == "4":
        location()
    elif corchoice == "1":
        brosh(surname)
    elif corchoice == "2":
        falman(surname)
    elif corchoice == "3":
        armstrong(surname)
def brosh(surname): # COMPLETE
    os.system('clear')
    print("LOCATION: MAIN CORRIDOR\n")
    print('BROSH: "Sergeant', surname+', good morning!"\n\nDIALOGUE/ACTION OPTIONS: \n1: "Do you know where Major Elric might be?" \n2: "Bye."')
    broshchoice = input("\nEnter your choice: ")
    while broshchoice != "1" and broshchoice != "2":
      broshchoice = input("\nInvalid answer. Enter your choice: ")
    if broshchoice == "2":
      os.system('clear')
      print("LOCATION: MAIN CORRIDOR\n")
      print('BROSH: "Sergeant', surname+', good morning!"\n\n__________ \n\nYOU: "Bye." \n\nBROSH: "See you later!"')
      broshchoice = input("\nEnter 1 to go back to the main corridor: ")
      while broshchoice != "1":
        broshchoice = input("\nInvalid answer. Enter your choice: ")
      if broshchoice == "1":
        corridor()
    elif broshchoice == "1":
      os.system('clear')
      print("LOCATION: MAIN CORRIDOR\n")
      print('BROSH: "Sergeant', surname+', good morning!"\n\n__________ \n\nYOU: "Do you know where Major Elric might be?" \n\nBROSH: "Ah, sorry, but no. I remember seeing him pass through the reception area though! Maybe you could try asking the receptionist? Oh! And I was also talking to Second Lieutenant Ross earlier, I think she mentioned that she spoke to him for a little while."')
      broshchoice = input("\nEnter 1 to go back to the main corridor: ")
      while broshchoice != "1" and broshchoice != "2":
        broshchoice = input("\nInvalid answer. Enter your choice: ")
      if broshchoice == "1":
        corridor()
def falman(surname): # COMPLETE
    os.system('clear')
    print("LOCATION: MAIN CORRIDOR")
    print('\nFALMAN: "Hello, sergeant', surname + '." \n\nDIALOGUE/ACTION OPTIONS: \n1: "Do you know where I could find Major Elric?" \n2: "Bye."')
    falmanchoice = input("\nEnter your choice: ")
    while falmanchoice != "1" and falmanchoice != "2":
      falmanchoice = input("\nInvalid answer. Enter your choice: ")
    if falmanchoice == "2":
      os.system('clear')
      print("LOCATION: MAIN CORRIDOR\n")
      print('\nFALMAN: "Hello, sergeant', surname + '." \n\n__________ \n\nYOU: "Bye." \n\nFALMAN: "Goodbye, sergeant."')
      falmanchoice = input("\nEnter 1 to go back to the main corridor: ")
      while falmanchoice != "1":
        falmanchoice = input("\nInvalid answer. Enter your choice: ")
      if falmanchoice == "1":
        corridor()
    elif falmanchoice == "1":
      os.system('clear')
      print("LOCATION: MAIN CORRIDOR\n")
      print('\nFALMAN: "Hello, sergeant', surname + '." \n\n__________ \n\nYOU: "Do you know where I could find Major Elric?" \n\nFALMAN: "No, sorry. But, I remember Second Lieutenant Breda mentioning something about him earlier. Try asking the second lieutenant if you see him around."')
      falmanchoice = input("\nEnter 1 to go back to the main corridor: ")
      while falmanchoice != "1" and falmanchoice != "2":
        falmanchoice = input("\nInvalid answer. Enter your choice: ")
      if falmanchoice == "1":
        corridor()
def armstrong(surname): # COMPLETE
    os.system('clear')
    print("LOCATION: MAIN CORRIDOR")
    print('\nARMSTRONG: "GOOD MORNING, SERGEANT', surname.upper() +'!!! HOW MAY I ASSIST YOU TODAY?"')
    print('\nDIALOGUE/ACTION OPTIONS: \n1: "I need to find Major Elric, do you know where he might be?" \n2: "Bye."')
    armstrongchoice = input("\nEnter your choice: ")
    while armstrongchoice != "1" and armstrongchoice != "2":
      armstrongchoice = input("\nInvalid answer. Enter your choice: ")
    if armstrongchoice == "2":
      os.system('clear')
      print("LOCATION: MAIN CORRIDOR")
      print('\nARMSTRONG: "GOOD MORNING, SERGEANT', surname.upper() +'!!! HOW MAY I ASSIST YOU TODAY?" \n\n__________ \n\nYOU: "Bye." \n\nARMSTRONG: "FAREWELL THEN, SERGEANT! MAY WE MEET AGAIN SOON!!"')
      armstrongchoice = input("\nEnter 1 to go back to the main corridor: ")
      while armstrongchoice != "1":
        armstrongchoice = input("\nInvalid answer. Enter your choice: ")
      if armstrongchoice == "1":
        corridor()
    elif armstrongchoice == "1":
      os.system('clear')
      print("LOCATION: MAIN CORRIDOR")
      print('\nARMSTRONG: "GOOD MORNING, SERGEANT', surname.upper() +'!!! HOW MAY I ASSIST YOU TODAY?" \n\n__________ \n\nYOU: "I need to find Major Elric, do you know where he might be?" \n\nARMSTRONG: "AH, SERGEANT, YOU HAVE MY DEEPEST APOLOGIES, AS I VERY UNFORTUNATELY DO NOT KNOW THE WHEREABOUTS OF EDWARD ELRIC. HOWEVER, I DO BELIEVE THAT SECOND LIEUTENANT ROSS MENTIONED SEEING HIM EARLIER THIS MORNING." \n\nYOU: "Thank you, Major Armstrong. Goodbye." \n\nARMSTRONG: "GOODBYE, SERGEANT! I WISH YOU LUCK ON YOUR MISSION!"')
      armstrongchoice = input("\nEnter 1 to go back to the main corridor: ")
      while armstrongchoice != "1":
        armstrongchoice = input("\nInvalid answer. Enter your choice: ")
      if armstrongchoice == "1":
        corridor()

def reception(): # COMPLETE
    os.system('clear')
    print("LOCATION: RECEPTION AREA\n")
    print("You see Private Seymour dozing off at the reception desk, Major General Halcrow entering the building, and Second Lieutenant Catalina walking into the room. \n\nEnter 1 to approach Private Seymour, enter 2 to approach Major General Halcrow, enter 3 to approach Second Lieutenant Catalina, enter 4 to leave the reception area.")
    recchoice = input("\nEnter your choice: ")
    while recchoice != "1" and recchoice != "2" and recchoice != "3" and recchoice != "4":
        recchoice = input("\nInvalid answer. Enter your choice: ")
    if recchoice == "4":
        location()
    elif recchoice == "1":
        seymour(surname)
    elif recchoice == "2":
        halcrow(surname)
    elif recchoice == "3":
        catalina(surname)

seymouropt = '\nDIALOGUE/ACTION OPTIONS: \n1: "Have you seen Major Elric around?" \n2: "You should know better than to be sleeping on the job. Do better next time." \n3: "Nothing in particular. Goodbye."'
def seymour(surname): # COMPLETE
    os.system('clear')
    print("LOCATION: RECEPTION AREA\n")
    seymour = ['SEYMOUR: "zzzzzzz"', "\nEnter 1 to wake up Private Seymour, enter 2 to go back to the reception area. "]
    for item in seymour:
      print(item)
    seymourchoice = input("\nEnter your choice: ")
    while seymourchoice != "1" and seymourchoice != "2":
      seymourchoice = input("\nInvalid answer. Enter your choice: ")
    if seymourchoice == "2":
      reception()
    elif seymourchoice == "1":
      os.system('clear')
      print("LOCATION: RECEPTION AREA\n")
      seymour.append('\n__________ \n\nYou tap Private Seymour on the head. \n\nSEYMOUR: "Wha...? Just a few more min- AGH!!" \n\nPrivate Seymour jumps up into a salute. \n\nSEYMOUR: "S-sergeant! H-hey there Sergeant, what can I do for you?"')
      seymour.remove("\nEnter 1 to wake up Private Seymour, enter 2 to go back to the reception area. ")
      seymour.append(seymouropt)
      for item in seymour:
        print(item)
      seymourchoice = input("\nEnter your choice: ")
      while seymourchoice != "1" and seymourchoice != "2" and seymourchoice != "3":
        seymourchoice = input("\nInvalid answer. Enter your choice: ")
      if seymourchoice == "3":
        os.system('clear')
        print("LOCATION: RECEPTION AREA\n")
        seymour.remove(seymouropt)
        seymour.append('\n__________ \n\nYOU: "Nothing in particular. Goodbye." \n\nSEYMOUR: "Oh, uh- goodbye then!"')
        for item in seymour:
          print(item)
        seymourchoice = input("\nEnter 1 to go back to the reception area: ")
        while seymourchoice != "1":
          seymourchoice = input("\nInvalid answer. Enter 1 to go back to the reception area: ")
        if seymourchoice == "1":
          reception()
      if seymourchoice == "2":
        os.system('clear')
        print("LOCATION: RECEPTION AREA\n")
        seymour.remove(seymouropt)
        seymour.append('\n__________ \n\nYOU: "You should know better than to be sleeping on the job. Do better next time." \n\nSEYMOUR: "Y-yes sergeant! Of course sergeant! I apologize greatly for my irresponsibility!"')
        for item in seymour:
          print(item)
        seymourchoice = input("\nEnter 1 to go back to the reception area: ")
        while seymourchoice != "1":
          seymourchoice = input("\nInvalid answer. Enter 1 to go back to the reception area: ")
        if seymourchoice == "1":
          reception()
      if seymourchoice == "1":
        os.system('clear')
        print("LOCATION: RECEPTION AREA\n")
        seymour.remove(seymouropt)
        seymour.append('\n__________ \n\nYOU: "Have you seen  Major Elric around?" \n\nSEYMOUR: "Major Elric...? Oh! Yeah, he came in a couple hours ago! He said he was going to the uh... the uhh..." \n\nYou raise a single eyebrow and give Private Seymour a Look. Private Seymour laughs nervously. \n\nSEYMOUR: "Ahaha... I must have been too tired to pay attention... sorry sergeant... " \n\nYOU: "*sigh* Just try to get more sleep tonight." \n\nSEYMOUR: "Y-yes, of course, sergeant! I promise to try my best, sergeant!"')
        for item in seymour:
          print(item)
        seymourchoice = input("\nEnter 1 to go back to the reception area: ")
        while seymourchoice != "1":
          seymourchoice = input("\nInvalid answer. Enter 1 to go back to the reception area: ")
        if seymourchoice == "1":
          reception()

halcrowopt = '\nDIALOGUE/ACTION OPTIONS: \n1: "*Ahem*" \n2: "Pardon me, Major General Halcrow, but may you please spare me a moment?" \n3: Walk away from Major General Halcrow.'
halcrowoptahem = '\nDIALOGUE/ACTION OPTIONS: \n1: "*AHEM*" \n2: "Pardon me, Major General Halcrow, but may you please spare me a moment?" \n3: Walk away from Major General Halcrow.'
halcrowoptpardon = '\nDIALOGUE/ACTION OPTIONS: \n1: "Do you know where Major Elric might be? Colonel Mustang requires an audience with him, I have the orders to find the major." \n2: "Yeah, yeah, busy doing what? Cheating on your wife again?" \n3: Walk away from Major General Halcrow.'
halcrowoptelric = '\nDIALOGUE/ACTION OPTIONS: \n1: "Apologies, sir. I do not know." \n2: "I dunno, and I really doubt it, but I kinda wish they /were/ plotting against you. Personally, and I mean full offense by this, I find you to be more of a major annoyance than a major general."'
def halcrow(surname): # COMPLETE
    os.system('clear')
    print("LOCATION: RECEPTION AREA\n")
    halcrow = []
    halcrow.append("Major General Halcrow gives you an impatient look and ignores you.")
    halcrow.append(halcrowopt)
    for item in halcrow:
      print(item)
    global halcrowchoice
    halcrowchoice = input("\nEnter your choice: ")
    while halcrowchoice != "1" and halcrowchoice != "2" and halcrowchoice != "3":
      halcrowchoice = input("\nInvalid answer. Enter your choice: ")
  
    if halcrowchoice == "3":
      reception()
    elif halcrowchoice == "1": # qhal
      os.system('clear')
      print("LOCATION: RECEPTION AREA\n")
      halcrow.remove(halcrowopt)
      halcrow.append('\n__________ \n\nYOU: "*Ahem*" \n\nMajor General Halcrow looks slightly more impatient and continues to ignore you.')
      halcrow.append(halcrowoptahem)
      for item in halcrow:
        print(item)
      while halcrowchoice != "1" and halcrowchoice != "2" and halcrowchoice != "3":
        halcrowchoice = input("\nInvalid answer. Enter your choice: ")
      halcrowchoice = input("\nEnter your choice: ")
      if halcrowchoice == "3":
       reception()
      elif halcrowchoice == "1": # qnote COMPLETE
        os.system('clear')
        print("LOCATION: RECEPTION AREA\n")
        halcrow.remove(halcrowoptahem)
        halcrow.append('\n__________ \n\nYOU: "*AHEM*" \n\nMajor General Halcrow finally turns to look at you, but his face is full of indignant anger and disgust. \n\nHALCROW: "You dare act towards a superior officer in such a rude manner?! I am absolutely APPALLED at the disrepect! You are FIRED!! NEVER SHOW YOURSELF IN MY SIGHT AGAIN!!!"')
        for item in halcrow:
          print(item)
        fail()
      elif halcrowchoice == "2":
        os.system('clear')
        print("LOCATION: RECEPTION AREA\n")
        halcrow.remove(halcrowoptahem)
        halcrowpardon(surname, halcrowchoice, halcrow)
    elif halcrowchoice == "2":
      os.system('clear')
      print("LOCATION: RECEPTION AREA\n")
      halcrow.remove(halcrowopt)
      halcrowpardon(surname, halcrowchoice, halcrow)
def halcrowpardon(surname, halcrowchoice, halcrow): # COMPLETE
  halcrow.append('\n__________ \n\nYOU: "Pardon me, Major General Halcrow, but may you please spare me a moment?" \n\nMajor General Halcrow lets out an annoyed sigh but turns to face you. \n\nHALCROW: "What do you want Sergeant? And make this quick, I am a very important, very busy man."')
  halcrow.append(halcrowoptpardon)
  for item in halcrow:
    print(item)
  halcrowchoice = input("\nEnter your choice: ")
  while halcrowchoice != "1" and halcrowchoice != "2" and halcrowchoice != "3":
    halcrowchoice = input("\nInvalid answer. Enter your choice: ")
  if halcrowchoice == "2": # qnote COMPLETE
    os.system('clear')
    print("LOCATION: RECEPTION AREA\n")
    halcrow.remove(halcrowoptpardon)
    halcrow.append('\n__________ \n\nYOU: "Yeah, yeah, busy doing what? Cheating on your wife again?"')
    halcrow.append("\nMajor General Halcrow's face goes red, screwing up in anger and what you think looks suspiciously like panic.") 
    halcrow.append('\nHALCROW: "You- you- YOU- THE UTTER AUDACITY YOU HAVE!! I WOULD NEVER DO SUCH A DISHONOURABLE THING!! WHERE DID YOU HEAR OF THIS FROM? WAS IT FROM THAT MUSTANG BASTARD SPREADING RUMORS ABOUT ME?! I WILL NOT TOLERATE SUCH SLANDER!! YOU ARE FIRED!!" \n\nMajor General Halcrow storms off in a rage, muttering something to himself about getting back at Colonel Mustang and needing to "fire everyone who might know."')
    for item in halcrow:
      print(item)
    fail()
  elif halcrowchoice == "3": # qnote COMPLETE
    os.system('clear')
    print("LOCATION: RECEPTION AREA\n")
    halcrow.remove(halcrowoptpardon)
    halcrow.append('\n__________ \n\nYou turn around to walk away from Major General Halcrow, but stop as he barks out: \n\nHALCROW: "Sergeant! Do you take me for a joke? How DARE you waste my time in such a manner?! I am absolutely APPALLED at the disrepect! You are FIRED!! NEVER SHOW YOURSELF IN MY SIGHT AGAIN!!!"')
    for item in halcrow:
      print(item)
    fail()
  elif halcrowchoice == "1":
    os.system('clear')
    print("LOCATION: RECEPTION AREA\n")
    halcrow.remove(halcrowoptpardon)
    halcrow.append('\n__________ \n\nYOU: "Would you by any chance know where Major Elric might be?" \n\nHALCROW: "*scoffs* Major Elric? Why would I concern myself with that obnoxious child?" \n\nMajor General Halcrow gets an ugly look on his face and narrows his eyes in suspicion. \n\nHALCROW: "Why does Mustang need to see him? Is he plotting something? Is he plotting against /me/?"')
    halcrow.append(halcrowoptelric)
    for item in halcrow:
      print(item)
    halcrowchoice = input("\nEnter your choice: ")
    while halcrowchoice != "1" and halcrowchoice != "2":
      halcrowchoice = input("\nInvalid answer. Enter your choice: ")
    if halcrowchoice == "1":
      os.system('clear')
      print("LOCATION: RECEPTION AREA\n")
      halcrow.remove(halcrowoptelric)
      halcrow.append('\n__________ \n\nYOU: "Apologies, sir. I do not know." \n\nHALCROW: "*mutters* Of course not. Useless, utterly useless." \n\nHALCROW: "Well then, sergeant, you are dismissed. Get out of my sight."')
      for item in halcrow:
        print(item)
      halcrowchoice = input("\nEnter 1 to go back to the reception area, enter 2 to continue talking to Major General Halcrow: ")
      while halcrowchoice != "1" and halcrowchoice != "2":
        halcrowchoice = input("\nInvalid answer. Enter 1 to go back to the reception area, enter 2 to continue talking to Major General Halcrow: ")
      if halcrowchoice == "1":
        reception()
      elif halcrowchoice == "2":
        os.system('clear')
        print("LOCATION: RECEPTION AREA\n")
        halcrow.append('\n__________ \n\nYou open your mouth,about to ask Major General Halcrow if the rumors about him cheating on his wife are true, when you are interrupted with— \n\nHALCROW: "Why are you still here? Unable to follow orders? I will NOT tolerate such blantant disrespect towards a superior officer! FIRED!!"')
        for item in halcrow:
          print(item)
        fail()
    if halcrowchoice == "2":
        os.system('clear')
        print("LOCATION: RECEPTION AREA\n")
        halcrow.remove(halcrowoptelric)
        halcrow.append('\n__________ \n\nYOU: "I dunno, and I really doubt it, but I kinda wish they /were/ plotting against you. Personally, and I mean full offense by this, I find you to be more of a major annoyance than a major general." \n\nMajor General Halcrow starts trembling with rage and goes an impressively vivid shade of red. \n\nHALCROW: "I- you- YOU- FIRED! FIRED, FIRED, FIRED!!!"')
        for item in halcrow:
          print(item)
        fail()

def catalina(surname): # COMPLETE
    os.system('clear')
    print("LOCATION: RECEPTION AREA\n")
    print('CATALINA: "Oh, good morning Sergeant', surname + '!"')
    catalina = ['\nDIALOGUE/ACTION OPTIONS: \n1: "Good morning, Second Lieutenant Catalina. Do you have any idea where Major Elric might be?" \n2: "Bye."']
    for item in catalina:
      print(item)
    catalinachoice = input("\nEnter your choice: ")
    while catalinachoice != "1" and catalinachoice != "2":
      catalinachoice = input("\nInvalid answer. Enter your choice: ")
    if catalinachoice == "2":
      os.system('clear')
      print("LOCATION: RECEPTION AREA\n")
      print('CATALINA: "Oh, good morning Sergeant', surname + '!"')
      catalina.remove('\nDIALOGUE/ACTION OPTIONS: \n1: "Good morning, Second Lieutenant Catalina. Do you have any idea where Major Elric might be?" \n2: "Bye."')
      catalina.append('\n__________ \n\nYOU: "Bye." \n\nCATALINA: "Goodbye!"')
      for item in catalina:
        print(item)
      catalinachoice = input("\nEnter 1 to return to the reception area: ")
      while catalinachoice != "1":
        catalinachoice = input("\nInvalid answer. Enter your choice: ")
      if catalinachoice == "1":
        reception()
    if catalinachoice == "1":
      os.system('clear')
      print("LOCATION: RECEPTION AREA\n")
      print('CATALINA: "Oh, good morning Sergeant', surname + '!"')
      print('\n__________ \n\nYOU: "Good morning, Second Lieutenant Catalina. Do you have any idea where Major Elric might be?" \n\nCATALINA: "Oh, I saw him earlier today! ', end = '')
      print("If I remember correctly, I think he said something about needing to do research and 'avoiding Colonel Bastard.' ", end = '')
      print('Maybe you could try looking for him in the library?"')
      catalinachoice = input("\nEnter 1 to return to the reception area: ")
      while catalinachoice != "1":
        catalinachoice = input("\nInvalid answer. Enter your choice: ")
      if catalinachoice == "1":
        reception()

def library(): # COMPLETE
    os.system('clear')
    print("LOCATION: LIBRARY")
    print(
        "\nYou see Master Sergeant Fuery writing in a file. \n\nEnter 1 to approach Master Sergeant Fuery, enter 2 to leave the library.")
    libchoice = input("\nEnter your choice: ")
    while libchoice != "1" and libchoice != "2":
        libchoice = input("\nInvalid answer. Enter your choice: ")
    if libchoice == "2":
        location()
    elif libchoice == "1":
        fuerydoor(surname)

def fuerydoor(surname): # COMPLETE
    os.system('clear')
    print("LOCATION: LIBRARY\n")
    print('As you approach Master Sergeant Fuery, you notice a closed door behind him with a large "RESTRICTED" sign. \n\nEnter 1 to talk to Master Sergeant Fuery, enter 2 to investigate the door, enter 3 to go back to the library.')
    fuerychoice = input("\nEnter your choice: ")
    while fuerychoice != "1" and fuerychoice != "2" and fuerychoice != "3":
      fuerychoice = input("\nInvalid answer. Enter your choice: ")
    if fuerychoice == "3":
      library()
    if fuerychoice == "2":
      os.system('clear')
      print("LOCATION: LIBRARY\n")
      print('As you approach Master Sergeant Fuery, you notice a closed door behind him with a large "RESTRICTED" sign.\n\n__________ \n\nYou try to open the door, but the door is locked.\n\nEnter 1 to keep trying to open the door, enter 2 to return to the main section of the library.')
      fuerychoice = input("\nEnter your choice: ")
      while fuerychoice != "1" and fuerychoice != "2":
        fuerychoice = input("\nInvalid answer. Enter your choice: ")
      if fuerychoice == "2":
        library()
      elif fuerychoice == "1":
        os.system('clear')
        print("LOCATION: LIBRARY\n")
        print('As you approach Master Sergeant Fuery, you notice a closed door behind him with a large "RESTRICTED" sign.\n\n__________ \n\nYou try to open the door, but the door is locked.\n\n__________ \n\nYou bang on the door a few times, rattle the doorknob, and you start reaching for a small lock-picking pin in your pocket when suddenly— \n\nSECURITY: "Hey! You! This area is strictly off-limits!"')
        fail()  
    elif fuerychoice == "1":
      fuery(surname, fuerydoor)

def fuery(surname, fuerydoor): # COMPLETE EXCEPT FOR POSSIBLE EDITS TO FIT HAVOC+BREDA --> SHESKA
  os.system('clear')
  print("LOCATION: LIBRARY\n")
  print('FUERY: "Ah, hey there Sergeant', surname+'."')
  print('\nDIALOGUE/ACTION OPTIONS: \n1: "Do you know where Major Elric is?" \n2: "Pardon me, but may I ask what you are writing?" \n3: "Bye."')
  fuerychoice = input("\nEnter your choice: ")
  while fuerychoice != "1" and fuerychoice != "2" and fuerychoice != "3":
    fuerychoice = input("\nInvalid answer. Enter your choice: ")
  if fuerychoice == "3":
    os.system('clear')
    print("LOCATION: LIBRARY\n")
    print('FUERY: "Ah, hey there Sergeant', surname+'." \n\n__________\n\nYOU: "Bye." \n\nFUERY: "Goodbye! See you around!"')
    fuerychoice = input("\nEnter 1 to return to the library: ")
    while fuerychoice != "1":
     fuerychoice = input("\nInvalid answer. Enter 1 to return to the library: ")
    if fuerychoice == "1":
      library()
  elif fuerychoice == "2":
    os.system('clear')
    print("LOCATION: LIBRARY\n")
    print('FUERY: "Ah, hey there Sergeant', surname+'."') 
    fueryoptpardon = '\nDIALOGUE/ACTION OPTIONS: \n1: "Major Elric?" \n2: "I see, thank you. Goodbye."'
    fuery = ['\n__________\n\nYOU: "Pardon me, but may I ask what you are writing?" \n\nFUERY: "Oh, this? Just a report for a quick little mission I did with Second Lieutenant Havoc and Major Elric yesterday."', fueryoptpardon]
    for item in fuery:
      print(item)
    fuerychoice = input("\nEnter your choice: ")
    while fuerychoice != "1" and fuerychoice != "2":
     fuerychoice = input("\nInvalid answer. Enter your choice: ")
    if fuerychoice == "2":
      os.system('clear')
      print("LOCATION: LIBRARY\n")
      print('FUERY: "Ah, hey there Sergeant', surname+'."')
      fuery.remove(fueryoptpardon)
      fuery.append('\n__________\n\nYOU: "I see, thank you. Goodbye." \n\nFUERY: "Goodbye for now, sergeant!"')
      for item in fuery:
        print(item)
      fuerychoice = input("\nEnter 1 to return to the library: ")
      while fuerychoice != "1":
        fuerychoice = input("\nInvalid answer. Enter 1 to return to the library: ")
      if fuerychoice == "1":
        library()
    if fuerychoice == "1":
      os.system('clear')
      print("LOCATION: LIBRARY\n")
      print('FUERY: "Ah, hey there Sergeant', surname+'."')
      fuery.remove(fueryoptpardon)
      fuery.append('\n__________\n\nYOU: "Major Elric?" \n\nFUERY: "Yup! Most of the details count as classified information, but I can at least tell you that Major Elric has got a lot of new material to research on."')
      fuery.append('\nDIALOGUE/ACTION OPTIONS: \n1: "Do you know where Major Elric is now?" \n2: "I see, thank you. Goodbye."')
      for item in fuery:
        print(item)
      fuerychoice = input("\nEnter your choice: ")
      while fuerychoice != "1" and fuerychoice != "2":
        fuerychoice = input("\nInvalid answer. Enter your choice: ")
      if fuerychoice == "2":
        os.system('clear')
        print("LOCATION: LIBRARY\n")
        print('FUERY: "Ah, hey there Sergeant', surname+'."')
        fuery.remove('\nDIALOGUE/ACTION OPTIONS: \n1: "Do you know where Major Elric is now?" \n2: "I see, thank you. Goodbye."')
        fuery.append('\n__________\n\nYOU: "I see, thank you. Goodbye." \n\nFUERY: "Goodbye for now, sergeant!"')
        for item in fuery:
          print(item)
        fuerychoice = input("\nEnter 1 to return to the library: ")
        while fuerychoice != "1":
          fuerychoice = input("\nInvalid answer. Enter 1 to return to the library: ")
        if fuerychoice == "1":
          library()
      if fuerychoice == "1":
        os.system('clear')
        print("LOCATION: LIBRARY\n")
        print('FUERY: "Ah, hey there Sergeant', surname+'."')
        fuery.remove('\nDIALOGUE/ACTION OPTIONS: \n1: "Do you know where Major Elric is now?" \n2: "I see, thank you. Goodbye."')
        fuery.append('\n__________\n\nYOU: "Do you know where Major Elric is now?" \n\nFUERY: "I have no clue, sorry. However, Second Lieutenant Havoc had to speak to Major Elric about matters relating to the mission this morning. I suggest asking him if you see him around." \n\nYOU: "Thank you, Master Sergeant Fuery. Goodbye."')
        for item in fuery:
          print(item)
        fuerychoice = input("\nEnter 1 to return to the library: ")
        while fuerychoice != "1":
          fuerychoice = input("\nInvalid answer. Enter 1 to return to the library: ")
        if fuerychoice == "1":
          library()
  elif fuerychoice == "1":
    os.system('clear')
    print("LOCATION: LIBRARY\n")
    print('FUERY: "Ah, hey there Sergeant', surname+'."') 
    print('\n__________\n\nYOU: "Do you know where Major Elric is?" \n\nFUERY: "Sorry, but I have no clue. Second Lieutenant Havoc spoke to him earlier today though, you could try asking him."')
    fuerychoice = input("\nEnter 1 to return to the library: ")
    while fuerychoice != "1":
      fuerychoice = input("\nInvalid answer. Enter 1 to return to the library: ")
    if fuerychoice == "1":
      library()

def mess():
    os.system('clear')
    print("LOCATION: MESS HALL")
    print("\nYou see Second Lieutenant Havoc and Second Lieutenant Breda eating together and Second Lieutenant Ross drinking a coffee a few tables away. \n\nEnter 1 to approach Second Lieutenant Havoc and Second Lieutenant Breda, enter 2 to approach Second Lieutenant Ross, enter 3 to leave the mess hall.")
    meschoice = input("\nEnter your choice: ")
    while meschoice != "1" and meschoice != "2" and meschoice != "3":
      meschoice = input("\nInvalid answer. Enter your choice: ")
    if meschoice == "3":
      location()
    elif meschoice == "1":
      havocbreda(surname, fuerydoor)
    elif meschoice == "2":
      ross(surname)

def havocbreda(surname, fuerydoor):
  os.system('clear')
  print("LOCATION: MESS HALL")
  print('\nHAVOC: "Mornin' + "'", 'Sergeant', surname + ', anything we can do for ya?"')
  print('\nDIALOGUE/ACTION OPTIONS: \n1: "Do you know where Major Elric is?" \n2: "Nothing much. How are you two?" \n3: "No, thanks. Goodbye."')
  havbrechoice = input("\nEnter your choice: ")
  while havbrechoice != "1" and havbrechoice != "2" and havbrechoice != "3":
    havbrechoice = input("\nInvalid answer. Enter your choice: ")
  if havbrechoice == "3":
    os.system('clear')
    print("LOCATION: MESS HALL")
    print('\nHAVOC: "Mornin' + "'", 'Sergeant', surname + ', anything we can do for ya?" \n\n__________\n\nYOU: "No, thanks. Goodbye." \n\nBREDA: "Have a good day, sergeant." \n\nHAVOC: "See you around."')
    havbrechoice = input("\nEnter 1 to return to the mess hall: ")
    while havbrechoice != "1":
      havbrechoice = input("\nInvalid answer. Enter 1 to return to the mess hall: ")
    if havbrechoice == "1":
      mess()
  elif havbrechoice == "2":
    os.system('clear')
    print("LOCATION: MESS HALL")
    print('\nHAVOC: "Mornin' + "'", 'Sergeant', surname + ', anything we can do for ya?"') 
    print('\n__________\n\nYOU: "Nothing much. How are you two?" \n\nSecond Lieutenant Havoc lets out a dramatic sigh; Second Lieutenant Breda rolls his eyes at his friend. \n\nHAVOC: "I think Major General Halcrow actually wants me dead." \n\nBREDA: "Ignore him, ', end = '')
    print("Halcrow wasn't even that bad this time. This is nothing compared to last time when he tried accusing the Colonel of ", end = '')
    print('nepotism." \n\nHAVOC: "HA! That was hilarious, as if Colonel Mustang can maintain enough healthy personal relationships for that to happen. ', end = '')
    print("If anything, he should've tried framing him for arson. Not that it would've worked either, but it might've been less ", end = '')
    print('pathetic of an attempt." \n\nDIALOGUE/ACTION OPTIONS: \n1: "Halcrow tries so hard to be a threat to Colonel Mustang. Rather pitiful that all he is is a vaguely entertaining nuisance." \n2: "Thanks for the chat, but I have to be going now. Bye."')
    havbrechoice = input("\nEnter your choice: ")
    while havbrechoice != "1" and havbrechoice != "2":
      havbrechoice = input("\nInvalid answer. Enter your choice: ")
    if havbrechoice == "2":
      os.system('clear')
      print("LOCATION: MESS HALL")
      print('\nHAVOC: "Mornin' + "'", 'Sergeant', surname + ', anything we can do for ya?"') 
      print('\n__________\n\nYOU: "Nothing much. How are you two?" \n\nSecond Lieutenant Havoc lets out a dramatic sigh; Second Lieutenant Breda rolls his eyes at his friend. \n\nHAVOC: "I think Major General Halcrow actually wants me dead." \n\nBREDA: "Ignore him, ', end = '')
      print("Halcrow wasn't even that bad this time. This is nothing compared to last time when he tried accusing the Colonel of ", end = '')
      print('nepotism." \n\nHAVOC: "HA! That was hilarious, as if Colonel Mustang can maintain enough healthy personal relationships for that to happen. ', end = '')
      print("If anything, he should've tried framing him for arson. Not that it would've worked either, but it might've been less ", end = '')
      print('pathetic of an attempt." \n\n__________\n\nYOU: "Thanks for the chat, but I have to be going now. Bye." \n\nBREDA: "Catch you later, sergeant." \n\nHAVOC: "Just', "say the word and we'll tell you all about Halcrow's dirt next", 'time."')
      havbrechoice = input("\nEnter 1 to return to the mess hall: ")
      while havbrechoice != "1":
       havbrechoice = input("\nInvalid answer. Enter 1 to return to the mess hall: ")
      if havbrechoice == "1":
        mess()
    elif havbrechoice == "1":
      os.system('clear')
      print("LOCATION: MESS HALL")
      print('\nHAVOC: "Mornin' + "'", 'Sergeant', surname + ', anything we can do for ya?"') 
      print('\n__________\n\nYOU: "Nothing much. How are you two?" \n\nSecond Lieutenant Havoc lets out a dramatic sigh; Second Lieutenant Breda rolls his eyes at his friend. \n\nHAVOC: "I think Major General Halcrow actually wants me dead." \n\nBREDA: "Ignore him, ', end = '')
      print("Halcrow wasn't even that bad this time. This is nothing compared to last time when he tried accusing the Colonel of ", end = '')
      print('nepotism." \n\nHAVOC: "HA! That was hilarious, as if Colonel Mustang can maintain enough healthy personal relationships for that to happen. ', end = '')
      print("If anything, he should've tried framing him for arson. Not that it would've worked either, but it might've been less ", end = '')
      print('pathetic of an attempt." \n\n__________\n\nYOU: "Halcrow tries so hard to be a threat to Colonel Mustang. Rather pitiful that all he is is a vaguely entertaining nuisance." \n\nSecond Lieutenant Breda bursts into laughter; Second Lieutenant Havoc bursts into louder laughter. \n\nThe three of you continue sharing grievances and increasingly creative insults on Major General Halcrow until Second Lieutenant Breda notices the time and says— \n\nBREDA: "Ah, shoot. We gotta go, need to meet with Colonel Mustang in ten minutes." \n\nAfter exchanging your goodbyes, you walk away from the table to continue your search for Major Elric. However, as you turn the corner, you come face to face with—\n\nHALCROW: "AHA! I KNEW there was something suspicious about you!', "Plotting with Mustang's men to overthrow me now, HM?", 'FIRED!!!"')
      fail()
  elif havbrechoice == "1":
    os.system('clear')
    print("LOCATION: MESS HALL\n")
    print('\nHAVOC: "Mornin' + "'", 'Sergeant', surname + ', anything we can do for ya?"\n\n__________\n\nYOU: "Do you know where Major Elric is?"\n\nHAVOC: "Oh, yeah, we were just', "talkin' about him.", 'He said he was going to the library." \n\nBREDA: "*sigh* That kid works too hard, he was in there all of last night, and then probably skipped sleep to do /more/ research after he got kicked out. Well, in any case, good luck finding him."')
    havbrechoice = input("\nEnter 1 to return to the mess hall: ")
    while havbrechoice != "1":
      havbrechoice = input("\nInvalid answer. Enter 1 to return to the mess hall: ")
    if havbrechoice == "1":
      mess() 

def ross(surname): # COMPLETE
  os.system('clear')
  print("LOCATION: MESS HALL\n")
  print('ROSS: "Hey there, Sergeant', surname+'. Anything I can help you with today?" \n\nDIALOGUE/ACTION OPTIONS: \n1: "Have you seen Major Elric anywhere?" \n2: "No, thanks. Goodbye, second lieutenant."' )
  rosschoice = input("\nEnter your choice: ")
  while rosschoice != '1' and rosschoice != '2':
    rosschoice = input("\nInvalid answer. Enter your choice: ")
  if rosschoice == "2":
    os.system('clear')
    print("LOCATION: MESS HALL\n")
    print('ROSS: "Hey there, Sergeant', surname+'. Anything I can help you with today?" \n\n__________\n\nYOU: "No, thank you. Goodbye, second lieutenant." \n\nROSS: "Bye!"')
    rosschoice = input("\nEnter 1 to return to the mess hall: ")
    while rosschoice != '1':
      rosschoice = input("\nInvalid answer. Enter your choice: ")
    if rosschoice == "1":
      mess()
  if rosschoice == "1":
    os.system('clear')
    print("LOCATION: MESS HALL\n")
    print('ROSS: "Hey there, Sergeant', surname+'. Anything I can help you with today?" \n\n__________\n\nYOU: "Have you seen Major Elric anywhere?" \n\nROSS: "I spoke to him briefly a few hours ago, but', "I'm not sure where he is now. However, I may have overheard Second Lieutenant Havoc and Second Lieutenant Breda mention the major a few minutes ago.", 'I suggest asking them."')
    rosschoice = input("\nEnter 1 to return to the mess hall: ")
    while rosschoice != '1':
      rosschoice = input("\nInvalid answer. Enter your choice: ")
    if rosschoice == "1":
      mess()

start()
