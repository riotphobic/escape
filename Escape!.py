"""
Escape!

Abdallah F Maharmah

A game where the user looks for items to escape a place.

made out of bordom
"""

# import system from os to clear the screen
from os import system, name

# FUNCTIONS
def clear():
  """
  clears the screen (source: https://www.geeksforgeeks.org/clear-screen-python/)
  Args
    None
  Returns
    None
  """
  # for windows
  if name == 'nt':
      _ = system('cls')
  # for mac and linux(here, os.name is 'posix')
  else:
      _ = system('clear')

def menu(options, action = 'do next'):
  """
  Lets the user select an option from a menu
  Args
    options: list
    action: string, default 'do next'
  Returns
    choice: int
  """
  print('\033[0m')
  # only one menu option
  if len(options) == 1:
    input('\033[94mEnter anything to {}\033[94m. \033[0m'.format(options[0]))
    # no need for a failsafe since there's only one option
    clear()

  # multiple options
  else:
    print('\n\033[94mWhat do you {}?'.format(action))
    # print the number for each option and keep track of what numbers are valid
    validOptions = []
    for i in range(len(options)):
      print('\033[94m' + str(i + 1), '\033[0m-', options[i])
      validOptions.append(str(i + 1))

    # only let user enter valid options
    choice = input('\n')
    while choice not in validOptions:
      choice = input('\n\033[31mPlease enter a valid option:\033[0m ')
    clear()
    return int(choice)

def findItem(itemName, currentLocation, context = 'You found a ', punctuation = '!', locationFirstTime = True):
  """
  Add an item to the inventory if the user hasn't already found it.
  Args
    itemName: string
    The name of the item that is being found
    currentLocation: string
    context: string, default 'You found a '
    Tells the user how they got the item. Default: 'You found a '
    punctuation: str, default '!'
    locationFirstTime: bool, default False
    Whether or not to skip printing the current location when the user finds the item
  Returns:
    None
  """
  if itemName not in inventory:
    # print current location and tell the user they have found an item
    if locationFirstTime:
      print(currentLocation, '\n\n\033[3m{}\033[93m{}\033[97m{}\033[0m'.format(context, itemName, punctuation))
    # don't print current location
    else:
      print('\033[3m{}\033[93m{}\033[97m{}\033[0m'.format(context, itemName, punctuation))
    menu(['pick it up'])
    print(currentLocation, '\n\n\033[93;1m{}\033[0m added to inventory'.format(itemName))
    # add the item to inventory
    inventory.append(itemName)
  # if item already in inventory
  else:
    print(currentLocation, "\n\nYou don't find anything else interesting.")

def start(firstTime):
  """
  Location 1: Starting area - connects to sword room (needs goggles and key to enter) & ominous hallway
  Args
    firstTime: int
  Returns
    int
  """
  # if this is not the very start of the game, say what room it is and give a different description of the room depending on if the secret door is visible
  print('\033[96;1mStarting area\033[0m\n')
  if 'goggles' in inventory:
    print('\033[3mA \033[91mglowing doorway\033[97m has appeared in the wall opposite you. \033[36mAlfred\033[97m is still standing in the corner, reading his newspaper.\033[0m')
  elif firstTime != 0:
    print('\033[3mThe walls and floor of the room are inscribed with silver runes. \033[36mAlfred\033[97m is still standing in the corner, reading his newspaper.\033[0m')

  # continue giving the options for this location until user selects a different location
  while True:
    # the options are different at the very start of the game
    if firstTime == 0:
      print('\033[3mYou wake up in a cool, dimly lit room with no memory of who you are or how you got there.\033[0m')
      firstTime += 1 # talk to Alfred next
      option = menu(['look around'])
      print('\033[96;1mStarting area\033[0m\n')
      # describe the room
      print('\033[3mFlickering purple torches line the dark stone walls of the room, their light glimmering off of silver runes inscribed in the walls and floor. A \033[36mtall, bearded man\033[97m stands in the corner, reading what appears to be the newspaper. Maybe he can tell you where you are.\033[0m')

    # once the user has looked around, they have to talk to Alfred to learn the objective of the game
    elif firstTime == 1:
      option = menu(['talk to \033[36mthe man with the newspaper\033[0m'])
      # talk to Alfred
      return 9

    # the sword room is only visible if the user has the goggles
    elif 'goggles' in inventory:
      option = menu(["talk to \033[36mAlfred\033[0m", 'inventory', 'inspect \033[91mglowing door\033[0m', 'go through \033[91;1mglowing door\033[0m', 'go to \033[34;1mVaguely ominous hallway\033[0m', 'go to \033[92;1mStorage\033[0m'])
      # talk to Alfred
      if option == 1:
        print('\033[96;1mStarting area\033[0m\n')
        return 9

      # show inventory
      elif option == 2:
        print('\033[96;1mStarting area\033[0m\n')
        showInventory()

        # inspect the glowing door
      elif option == 3:
        print('\033[96;1mStarting area\033[0m\n')
        print('\033[3mIt seems like the \033[93mgoggles\033[97m from \033[35mDian\033[97m are letting you see a secret door.\033[0m')
      # go to the sword room (location 6), but only the user has found the key
      elif option == 4:
        if 'key' in inventory:
          return 6
        else:
          print('\033[96;1mStarting area\033[0m\n')
          print('The door is locked.')
      # go to the hallway (location 2)
      elif option == 5:
        return 2
      # go to main storage (location 4)
      else:
        return 4

    # if the user hasn't found the goggles yet
    else:
      option = menu(['look around', "talk to \033[36mAlfred\033[0m", 'inventory', 'go to \033[34;1mVaguely ominous hallway\033[0m', 'go to \033[92;1mStorage\033[0m'])
      # look around the room
      if option == 1:
        print('\033[96;1mStarting area\033[0m\n')
        print("\033[3mYou don't find anything particularily interesting\033[0m")
      # talk to Alfred
      if option == 2:
        print('\033[96;1mStarting area\033[0m\n')
        return 9
      # show inventory
      elif option == 3:
        print('\033[96;1mStarting area\033[0m\n')
        showInventory()
      # go to the hallway (location 2)
      elif option == 4:
        return 2
      # go to main storage (location 4)
      else:
        return 4

def hallway():
  """
  Location 2: Vaguely ominous hallway - connects to start, spooky room & danger room
  Args
    None
  Returns
    int
  """
  # give a description of the location
  print('\033[34;1mVaguely ominous hallway\033[0m\n')
  print("\033[3mAt one end of the hallway, a small stone archway leads to the \033[96mStarting area\033[97m, and at the other end is a giant iron door with a handpainted wooden sign that reads, '\033[31mDanger Room\033[97m.' Halfway down the hallway, you see an \033[95munmarked door\033[97m that is slowly leaking pale lavender smoke. The hallway seems unnecessarily long considering that it is only connected to three rooms.\033[0m")
  option = 0
  # continue giving the options for this location until user selects a different location
  while True:
    option = menu(['look around', 'inventory', 'go to \033[96;1mStarting area\033[0m', 'go to \033[95;1mSpooky room\033[0m', 'go to \033[31;1mDanger room\033[0m'])
    # look around
    if option == 1:
      print('\033[34;1mVaguely ominous hallway\033[0m\n')
      print("\033[3mYou don't find anything particularily interesting.\033[0m")
    # show inventory
    elif option == 2:
      print('\033[34;1mVaguely ominous hallway\033[0m\n')
      showInventory()
    # go to the starting area (location 1)
    elif option == 3:
      return 1
    # go to the spooky room (location 3)
    elif option == 4:
      return 3
    # go to the danger room (location 8)
    else:
      return 8

def spookyRoom(dianInteraction):
  """
  Location 3: Spooky room - contains goggles that let the user enter sword room and secret storage, user can get the vial of mysterious liquid once they return Dian's notebook, connects to ominous hallway
  Args
    dianInteraction: int
  Returns
    int
    dianInteraction: int
  """

  # describe the room
  print('\033[95;1mSpooky room\033[0m\n')
  print('\033[3mThe room is full of cool stuff. A person wearing what appears to be some kind of armoured lab coat is mixing bubbling liquids together and laughing maniacally.\033[0m')

  # continue giving the options for this location until user selects a different location
  while True:
    # if the user has never talked to Dian
    if dianInteraction == 1:
      option = menu(['talk to \033[35mthe person in the lab coat\033[0m', 'inventory', 'go back to \033[34mVaguely ominous hallway\033[0m'])
      if option == 1:
        # talk to Dian and get the goggles
        print('\033[95;1mSpooky room\033[0m\n')
        print("\033[35mDian\033[0m: Oh, a new visitor! Welcome! I'm \033[35mDian\033[0m, the mad scientist who's randomly here for some reason. Nice to meet you!")
        menu(['say: \033[0mum...hi!'])
        print('\033[95;1mSpooky room\033[0m\n')
        print("\033[35mDian\033[0m: Wait, you're probably looking for a weapon to defeat the \033[31mMysterious Evil Dude\033[0m, right? Since you're already exploring, could you also see if you can find my \033[93mnotebook\033[97m?")
        menu(['say: \033[0mI guess so'])
        print('\033[95;1mSpooky room\033[0m\n')
        print("\033[35mDian\033[0m: Thank you! Oh, you'll probably need these to find it.\n")
        findItem('goggles', '\033[95;1mSpooky room\033[0m', '\033[35;3mDian\033[97m hands you a pair of ', '', False)
        dianInteraction += 1
      # show inventory
      elif option == 2:
        print('\033[95;1mSpooky room\033[0m\n')
        showInventory()
      # go to hallway (location 2)
      else:
        return 2, dianInteraction

    # if the user has spoken to Dian but hasn't yet returned their notebook
    elif dianInteraction == 2:
      option = menu(['talk to \033[35mDian\033[0m', 'inventory', 'go back to ominous hallway'])
      if option == 1:
        # if the user has the notebook, they return it to Dian and get the vial of strange liquid
        print('\033[95;1mSpooky room\033[0m\n')
        if "Dian's notebook" in inventory:
          print('\033[35mDian\033[0m: Thanks for finding my notebook! Here, this might be useful sometime.\n')
          inventory.remove("Dian's notebook")
          dianInteraction += 1
          findItem('vial of strange liquid', '\033[95;1mSpooky room\033[0m', '\033[35;3mDian\033[97m hands you a ', '', False)

        # if they don't have the notebook, give a hint
        else:
          print('\033[35mDian\033[0m: Have you found my notebook yet?')
          menu(['say: \033[0mno'])
          print('\033[95;1mSpooky room\033[0m\n')
          print('\033[35mDian\033[0m: Maybe try looking in \033[92;1mStorage\033[0m.')

      # show inventory
      elif option == 2:
        print('\033[95;1mSpooky room\033[0m\n')
        showInventory()

      # go to hallway (location 2)
      else:
        return 2, dianInteraction

    # the user has already returned Dian's notebook
    elif dianInteraction == 3:
      option = menu(['talk to \033[35mDian\033[0m', 'inventory', 'go back to ominous hallway'])
      if option == 1:
        # Dian is still there but doesn't do anything anymore
        print('\033[95;1mSpooky room\033[0m\n')
        print("\033[35mDian\033[0m: Good luck on your escape!")
      # show inventory
      elif option == 2:
        print('\033[95;1mSpooky room\033[0m\n')
        showInventory()
      # go to hallway (location 2)
      else:
        return 2, dianInteraction

def storage1():
  """
  location 4: Storage - find pretty crystal, connects to secret storage (needs goggles to enter) & starting area
  Args
    None
  Returns
    int
  """

  print('\033[92;1mStorage\033[0m\n')
  # give a different description of the room if the user has the goggles
  if 'goggles' in inventory:
    print('\033[3mYou enter a room that is full of shelves, cabinets, boxes, and other storage units. There is a \033[92mglowing doorway\033[97m in one of the walls.\033[0m')
  else:
    print('\033[3mYou enter a room that is full of shelves, cabinets, boxes, and other storage units.\033[0m')

  # continue giving the options for this location until user selects a different location
  while True:
    # if the user has the goggles, they can see the secret door
    if 'goggles' in inventory:
      option = menu(['look around', 'inventory', 'inspect \033[92mglowing door\033[0m', 'go through \033[92mglowing door\033[0m', 'go back to \033[96mStarting area\033[0m'])
      # look around and find pretty crystal
      if option == 1:
        findItem('pretty crystal', '\033[92;1mStorage\033[0m')

      # show inventory
      elif option == 2:
        print('\033[92;1mStorage\033[0m\n')
        showInventory()

      # inspect secret door
      elif option == 3:
        print('\033[92;1mStorage\033[0m\n')
        print('\033[3mIt seems like the \033[93mgoggles\033[97m from \033[35mDian\033[97m are letting you see a secret door.\033[0m')

      # go to secret storage (location 5)
      elif option == 4:
        return 5
      # go to starting area (location 1)
      else:
        return 1

    # if user doesn't have the goggles
    else:
      option = menu(['look around', 'inventory', 'go back to \033[96;1mStarting area\033[0m'])
      # look around and find pretty crystal
      if option == 1:
        findItem('pretty crystal', '\033[92;1mStorage\033[0m')

      # show inventoy
      elif option == 2:
        print('\033[92;1mStorage\033[0m\n')
        showInventory()

      # go to starting area (location 1)
      else:
        return 1

def storage2():
  """
  Location 5: Secret storage - requires goggles to enter, find Dian's notebook and key to sword room, connects to main storage
  Args
    None
  Returns
    int
  """

  # describe the location
  print('\033[92;1mSecret storage\033[0m\n')
  print('\033[3mBehind the glowing doorway, you find more cabinets and shelving units, although these ones are significantly dustier.\033[0m')

  # continue giving the options for this location until user selects a different location
  while True:
    option = menu(['look around', 'inventory', 'go back to \033[92mMain storage\033[0m'])
    # look around and find Dian's notebook and the key to the sword room
    if option == 1:
      # user can't find the key and notebook if they already have
      if 'key' not in inventory:
        findItem("Dian's notebook", '\033[92;1mSecret storage\033[0m')
        print('\033[3mA small glimmer of light catches your eye.\033[0m')
        menu(['go look at it'])
        findItem('key', '\033[92;1mSecret storage\033[0m')
      else:
        print("\033[3mYou don't find anything else particularly interesting.")

    # show inventory
    elif option == 2:
      print('\033[92;1mSecret storage\033[0m\n')
      showInventory()

    # go to main storage (location 4)
    else:
      return 4

def swordRoom(cameFromStart):
  """
  Location 6: Sword room - requires goggles and key to enter, find sword, connects to Starting area & anvil
  Args
    cameFromStart: bool
  Returns
    int
  """
  # give a different descriptions of the room if the user came from the starting area or the anvil
  print("\033[91;1mSword room\033[0m\n")
  if cameFromStart:
    print('\033[3mYou unlock the glowing door with the key you found in \033[92mSecret storage\033[97m.\n\nBehind the door appears to be some sort of magic item workshop. The walls are lined with shelves filled with vials of colourful glowing liquids. The centre of the room contains an anvil covered in silver runes like the ones you found in the \033[96mStarting Area.\033[0m')
  else:
    print('\033[3mYou step away from the anvil.\n\nThe room you are in appears to be some sort of magic item workshop. The walls are lined with shelves filled with vials of colourful glowing liquids. The centre of the room contains an anvil covered in silver runes like the ones you found in the \033[96mStarting Area.\033[0m')

  # continue giving the options for this location until user selects a different location
  while True:
    option = menu(['look around', 'inventory', 'go to the \033[91manvil\033[0m', 'go back to \033[96;1mStarting area\033[0m'])
    # look around and find sword
    if option == 1:
      findItem('sword', '\033[91;1mSword room\033[0m')

    # show inventory
    elif option == 2:
      print('\033[91;1mSword room\033[0m\n')
      showInventory()

    # go to anvil (location 7), swordRoomFromStart will be False
    elif option == 3:
      return 7, False

    # go to starting area (location 1), swordRoomFromStart will be True
    else:
      return 1, True

def anvil():
  """
  Location 7: Anvil - user can make the cool magic sword if they have the other sword, the pretty crystal, the glowing orb, and the vial of strange liquid. Connects to sword room.
  Args
    None
  Returns
    int
  """

  print('\033[91;1mAnvil\033[0m\n')
  print('\033[3mYou walk up to the anvil.\033[0m')

  # continue giving the options for this location until user selects a different location
  while True:
    option = menu(['inspect', 'make a \033[93mcool magic sword\033[0m', 'inventory', 'go back to \033[91;1mMain sword room\033[0m'])

    # explain how to make the cool magic sword
    if option == 1:
      print('\033[91;1mAnvil\033[0m\n')
      print("\033[3mYou find a recipe for a \033[93mcool magic sword\033[97m! It looks like if you find a \033[93mcrystal\033[97m, a \033[93mcool glowy orb thing\033[97m, and \033[93msome kind of potion\033[97m, you can simply place them on top of the \033[91manvil\033[97m and it will somehow intantly make your sword more powerful! You're pretty sure that isn't how blacksmithery actually works, but you decide not to think about it too hard.\033[0m\n")

    # make the cool magic sword if the user has all the components and hasnt already made it
    elif option == 2:
      # if the user has already already made it
      if 'cool magic sword' in inventory:
        print('\033[3mYou already made the \033[93mcool magic sword\033[0m.')
      # if the user has all the components and hasn't already made it
      elif 'pretty crystal' in inventory and 'glowing orb' in inventory and 'vial of strange liquid' in inventory and 'sword' in inventory:
        findItem('cool magic sword', '\033[91;1mAnvil\033[0m', '\033[3mA cloud of silver smoke billows out from the anvil.\033[0m\n\nYou made a ')
        inventory.remove('pretty crystal')
        inventory.remove('glowing orb')
        inventory.remove('vial of strange liquid')
        inventory.remove('sword')
      # if the user doesn't have all the components
      else:
        print('\033[91;1mAnvil\033[0m\n')
        print("\033[3mYou don't have all the nescessary components to make a \033[93mcool magic sword\033[0m.")

    # show inventory
    elif option == 3:
      print('\033[91;1mAnvil\033[0m\n')
      showInventory()

    # go to main sword room (location 6)
    else:
      return 6

def dangerRoom():
  """
  Location 8: Danger room - final (only) boss! If the user has no weapon, they die and are teleported back to start; if they have the first sword, they find the glowing orb; and if they have the cool magic sword, they win. Connects to ominous hallway.
  Args
    None
  Returns
    int
  """

  # describe the location
  print('\033[31;1mDanger room\033[0m\n')
  print("\033[3mYou enter what appears to be the \033[31mMysterious Evil Dude\033[97m's throne room. He hefts his cartoonishly large battle axe in preparation to fight.\033[0m")

  # both the options will result in leaving this location
  option = menu(['fight', 'escape'])

  # fight the Mysterious Evil Dude
  if option == 1:
    # if the user has the cool magic sword, they win
    if 'cool magic sword' in inventory:
      return 0

    # if the user has the first sword but not the cool magic sword, they escape the danger room and find the gloiwng orb
    elif 'sword' in inventory:
      print('\033[31;1mDanger room\033[0m\n')
      print('\033[3mThe \033[31mMysterious Evil Dude\033[97m is too strong, and you are forced to run away. However, you manage to steal a \033[93mcool glowy thing\033[97m on your way out.\033[0m')
      menu(['continue'])
      findItem('glowing orb', '\033[31mDanger room\033[0m')
      menu(['continue escaping'])
      return 2

    # if the user has no weapon, they die and are teleported back to the starting area
    else:
      print('\033[3mYou die a horrible, bloody death because you tried to fight the final boss without a weapon. \n\nFortunately, \033[36mAlfred\033[97m is somehow able to ressurect you.\033[0m')
      menu(['continue'])
      return 1

  # escape (go back to location 2)
  else:
    return 2

def alfred(giveTutorial):
  """
  Location 9 (technically an NPC, not a location): (Alfred - Explain the game to the user or give hints, then go back to Starting area
  Args
    giveTutorial: bool
  Returns
    int
    giveTutorial: bool
  """
  # if this is the start of the game, give the user a tutorial
  if giveTutorial:
    print('\033[36mThe tall, bearded man\033[0m: Oh, a new arrival?')
    menu(['What?', 'Where am I', 'Who are you?'], 'say')
    print("""\033[36mThe tall, bearded man\033[0m: Ah, you must be very confused. My name is \033[36mAlfred\033[0m, and I am the official greeter, necromancer, and head pastry chef of this fine establishment.\n\n\033[36mAlfred\033[0m: What even \033[3mis\033[0m this fine establishment?, you may be asking. Well, we have no idea, really. It's almost like whoever created this place was too lazy to come up with a decent backstory.""")

    moreInfo = False # can the user see the third section of information?
    evenMoreInfo = False # can the user see the fourth section of information?
    exitTutorial = False # has the user been given all necessary background information?

    # continue giving the options for this location until the user understands the game
    while True:
      # the user knows everything they need to play and can now safely exit the tutorial
      if moreInfo and evenMoreInfo and exitTutorial:
        option = menu(['Why am I here?', 'How do I get out of here?', 'Who is the \033[31mMysterious Evil Dude\033[0m?', 'How do I defeat the \033[31mMysterious Evil Dude?\033[0m', 'I have no more questions'], 'say')

        if option == 1:
          print('\033[36mAlfred\033[0m: Every so often, a new person arrives in this room, like you just did. As far as we know, your job is to defeat the \033[31mMysterious Evil Dude\033[0m.')

        elif option == 2:
          print("\033[36mAlfred\033[0m: As far as we know, the only way to get out involves besting the \033[31mMysterious Evil Dude\033[0m in combat, since that's where most of the previous visitors went before dissapearring. They could just all be dead, but I probably would have noticed and ressurected them.")

        elif option == 3:
          print("\033[36mAlfred\033[0m: No one really knows who the \033[31mMysterious Evil Dude\033[0m is, just that he is the antagonist and that he must be defeated. That's actually why we call him the \033[31mMysterious Evil Dude\033[0m.")

        elif option == 4:
          print("\033[36mAlfred\033[0m: The \033[31mMysterious Evil Dude\033[0m lives in the \033[31;1mDanger room\033[0m, which is just down that hallway. \n\n\033[3mHe gestures towards a \033[34mvaguely ominous hallway.\033[0m\n\n\033[36mAlfred\033[0m: All you have to do is go into the \033[31;1mDanger room\033[0m and fight him. However, you should probably look around to try to find a weapon first. I have no idea if it still has anything useful in it, but you might want to start in the \033[92mStorage room\033[0m.")
          exitTutorial = True

        # go to starting area (location 1), Alfred will no longer give the tutorial
        else:
          return 1, False

      # the user knows who the Mysterious Evil Dude is but still needs to be told how to win the game
      if moreInfo and evenMoreInfo:
        option = menu(['Why am I here?', 'How do I get out of here?', 'Who is the \033[31mMysterious Evil Dude\033[0m?', 'How do I defeat the \033[31mMysterious Evil Dude\033[0m?'], 'say')

        if option == 1:
          print('\033[36mAlfred\033[0m: Every so often, a new person arrives in this room, like you just did. As far as we know, your job is to defeat the \033[31mMysterious Evil Dude\033[0m.')

        elif option == 2:
          print("\033[36mAlfred\033[0m: As far as we know, the only way to get out involves besting the \033[31mMysterious Evil Dude\033[0m in combat, since that's where most of the previous visitors went before dissapearring. They could just all be dead, but I probably would have noticed and ressurected them.")

        elif option == 3:
          print("\033[36mAlfred\033[0m: No one really knows who the \033[31mMysterious Evil Dude\033[0m is, just that he is the antagonist and that he must be defeated. That's actually why we call him the \033[31mMysterious Evil Dude\033[0m.")

        elif option == 4:
          print("\033[36mAlfred\033[0m: The \033[31mMysterious Evil Dude\033[0m lives in the \033[31;1mDanger room\033[0m, which is just down that hallway. \n\n\033[3mHe gestures towards a vaguely ominous hallway.\033[0m\n\n\033[36mAlfred\033[0m: All you have to do is go into the \033[31;1mDanger room\033[0m and fight him. However, you should probably look around to try to find a weapon first. I have no idea if it still has anything useful in it, but you might want to start in the \033[92mStorage room\033[0m.")
          exitTutorial = True

      # the user has learned about the Mysterious Evil Dude and is probably confused
      elif moreInfo:
        option = menu(['Why am I here?', 'How do I get out of here?', 'Who is the \033[31mMysterious Evil Dude?\033[0m'], 'say')
        if option == 1:
          print('\033[36mAlfred\033[0m: Every so often, a new person arrives in this room, like you just did. As far as we know, your job is to defeat the \033[31mMysterious Evil Dude\033[0m.')

        elif option == 2:
          print("\033[36mAlfred\033[0m: As far as we know, the only way to get out involves besting the \033[31mMysterious Evil Dude\033[0m in combat, since that's where most of the previous visitors went before disappearing. They could just all be dead, but I probably would have noticed and ressurected them.")

        elif option == 3:
          print("\033[36mAlfred\033[0m: No one really knows who the \033[31mMysterious Evil Dude\033[0m is, just that he is the antagonist and that he must be defeated. That's actually why we call him the \033[31mMysterious Evil Dude\033[0m.")
          evenMoreInfo = True

      # the user doesn't know about the Mysterious Evil Dude
      else:
        option = menu(['Why am I here?', 'How do I get out of here?'], 'say')
        if option == 1:
          print('\033[36mAlfred\033[0m: Every so often, a new person arrives in this room, like you just did. As far as we know, your job is to defeat the \033[31mMysterious Evil Dude\033[0m.')
          moreInfo = True

        elif option == 2:
          print("\033[36mAlfred\033[0m: As far as we know, the only way to get out involves besting the \033[31mMysterious Evil Dude\033[0m in combat, since that's where most of the previous visitors went before dissapearring. They could just all be dead, but I probably would have noticed and ressurected them.")
          moreInfo = True

  # not the tutorial - give user a hint
  else:
    # if user has all the components for the cool magic sword
    if 'pretty crystal' in inventory and 'vial of strange liquid' in inventory and 'glowing orb' in inventory:
      print('\033[36mAlfred\033[0m: It looks like you have enough stuff to make a \033[93mcool magic sword\033[0m using the anvil in the \033[91mSword room\033[0m!')
    # if user hasn't talked to Dian or looked around in Main storage
    elif 'cool magic sword' not in inventory and ('goggles' not in inventory or 'pretty crystal' not in inventory):
      print('\033[36mAlfred\033[0m: You should look around a bit.')
    # if user has the goggles and hasn't looked around in secret storage
    elif 'key' not in inventory:
      print('\033[36mAlfred\033[0m: Oh, did Dian ask you to find their notebook? I think it might be in \033[92mStorage\033[0m somewhere.')
    # if user has found Dian's notebook but hasn't returned it
    elif "Dian's notebook" in inventory:
      print('\033[36mAlfred\033[0m: You should bring Dian their notebook.')
    # if user has a weapon and needs to go fight the Mysterious Evil Dude
    elif 'sword' in inventory or 'cool magic sword' in inventory:
      print('\033[36mAlfred\033[0m: You found a sword! You should go and fight the \033[31mMysterious Evil Dude\033[0m in the \033[31mDanger room\033[0m!')
    # user has the key to the sword room but hasn't looked around and found the first sword
    else:
      print("\033[36mAlfred\033[0m: You should look around in that secret room.\n\n\033[3mHe points to the \033[91mGlowing doorway\033[0m.\n\n\033[36mAlfred\033[0m: I assume you can see it, since you're wearing those goggles.")
    # go back to starting area (location 1)
    menu(['continue'])
    return 1, False

def win():
  """
  Congratulate the user for winning the game.
  Args
    None
  Returns
    None
  """

  print('\033[31;1mDanger room\033[0m\n')
  print('\033[3mYou defeat the \033[31mMysterious Evil Dude\033[97m with your \033[93mcool magic sword\033[97;1m.\n\nCongratulations! You won!')

def showInventory():
  """
  Prints the inventory
  Args
    None
  Returns
    None
  """
  # if inventory is empty
  if inventory == []:
    print('Inventory empty')
  # show inventory
  else:
    print('\033[1mInventory\033[0m\n-------------------\033[93m')
    for elem in inventory:
      print(elem)

# MAIN
inventory = [] # list of items that have been collected
dianInteractionNum = 1 # which interaction with Dian
swordRoomFromStart = True # are you entering the sword room (location 6) from the starting area?
alfredTutorial = True # whether Alfred will give the tutorial (True) or hints (False)

clear()
print('\033[1mEscape!')
menu(['start'])

location = start(0) # start at the starting area, give the user the tutorial

# keep going to different locations until the user wins
while location > 0:
  # start
  if location == 1:
    location = start(2)

  # ominous hallway
  elif location == 2:
    location = hallway()

  # spooky room
  elif location == 3:
    location, dianInteractionNum = spookyRoom(dianInteractionNum)

  # main storage
  elif location == 4:
    location = storage1()

  # secret storage
  elif location == 5:
    location = storage2()

  # sword room
  elif location == 6:
    location, swordRoomFromStart = swordRoom(swordRoomFromStart)

  # anvil
  elif location == 7:
    location = anvil()

  # danger room
  elif location == 8:
    location = dangerRoom()

  # talk to Alfred
  elif location == 9:
    location, alfredTutorial = alfred(alfredTutorial)

# you won!
win()
