#variables
import random
sklpnts = 10
shadocamo = ("off")
xequpei = 100
wizlvl = 1
pwrlvl = 1
rcktlnchammo = 0
arrows = 0
grenades = 0
bombs = 0
plyrhp = pwrlvl + 2
inventory = []
print("Currency names provided by roll for fantasy")
#beginning with questions
name = input("what is your name? ")
print("hello " + name)
chtcde = input("do you want to enter a cheat code? ")
if chtcde == ("majik"):
  print("MAGEMODE:ON")
  mgmd = ("active")
  xequpei == (1000000000000)
  wizlvl == 100
  pwrlvl == 100
  plyrhp == 102
  sklpnts == (1000000000000)
elif chtcde == ("no"):
    print("ok")
else:
  print("that is not a valid cheat code")

char = input("Choose your character: Mitsuki, Jace, Kirov, Andrea, or Virgil ")
print("ok, " + char + " it is!")
wpon = input("Choose your weapon: DURENDAL, KUSANGI, ZULFIQAR, CALADBOLG, or VOLPAR ALMACE ")
if wpon == ("onyx stynger"):
    print("only mages can handle this weapon")
    if mgmd == ("active"):
        print("good you are a mage")
        pwrlvl = pwrlvl + 120

    else:
        print("sorry you can't use this")
else:
    print("cool, the " + wpon + " is a good weapon")
    pwrlvl = pwrlvl + 10

shirt = input("what color shirt do you want? ")
pants = input("what color pants do you want? ")
if shirt == ("blak") and pants == ("blak"):
  print("great! now you have shadow camo!")
  shadocamo = ("on")
#element choice
elmnt = input(" what element of magic do you have? Water, Earth, Fire, Air, Dark,or Light? ")
if elmnt == ("earth"):
  print("you are good at making potions can summon animals and much more, buy an almanac for 10 xequpei at the store to learn more")
elif elmnt == ("water"):
  print("you can make ice,control water, and much more, buy an almanac for 10 xequpei at the store to learn more")
elif elmnt == ("fire"):
  print("you cannot get burned and are always the boldest person in the room buy an almanac for 10 xequpei at the store to learn more")
elif elmnt == ("dark"):
  print("you are dark and gloomy and you can control shadows buy an almanac for 10 xequpei at the store to learn more")
elif elmnt == ("air"):
  print("you usually space out and can float buy an almanac for 10 xequpei at the store to learn more")
elif elmnt == ("light"):
  print("you are the flashiest person in the room and can bend light buy an almanac for 10 xequpei at the store to learn more")
elif elmnt == ("im a mage") and mgmd == ("active"):
    print("wait, magemode is on so you don't need to pick an element, for you can harness them all") 
print("now let's get started")
opt = input("would you like to go to the store, fight, or adventure?")
#initial choice of store
if opt == ("store"):
  print("xequpei is the currency of this world. You have" + str(xequpei) + "xequpei")
  buy = input("what would you like to buy armor, weapons, potions,or equipment")
  if buy == ("weapons"):
      wponbuy1 = input("ok what kind of weapon do you want a primary or secondary")
      if wponbuy1 == ("primary"):
        wponbuy2 = input(" would you like ranged or meelee")
        if wponbuy2 == ("ranged"):
          wponbuy3 = input("explosive or projectile launching")
          if wponbuy3 == ("explosive"):
            wponbuy4 = input("rocket launcher for 100 xequpei or bomb for 15 xequpei per bomb")
            if wponbuy4 == ("bomb"):
              bmbamnt = input("how many?")
              xequpei = (xequpei - bmbamnt*15)
##            else:
##          else:
##        else:
##      else:
#initial choice of fight
elif opt == ("fight"):
  ftopt = input("here is the arena, do you want to practice, battle, or hone your magic skills")
  if ftopt == ("practice"):
    mnstrlvl = int(input("ok what level monster do you want to practice on 1-100"))
    mnstrhp = mnstrlvl
    mnstratk = mnstrlvl
    print("ok, the monster's hp is ")
    print(mnstrhp)
    atk = pwrlvl
    mnstrhp = mnstrhp - atk
    if mnstrhp <= 0:
      rtrn = input("the monster is dead you gained some skill points you can use those in the store to upgrade abilities do you want to go again or return to the menu")
      sklpnts == sklpnts + 10
      if rtrn == ("menu"):
        opt1 = input("would you like to go to the store, fight, or adventure?")
    else:
      print("you attacked it now the monster's health is ")
      print(mnstrhp)
      print("the monster's attack is ")
      print(mnstratk)
      print("he attacks you your health is ")
      plyrhp = plyrhp - mnstratk
      print(plyrhp)
      if plyrhp <= 0:
         print("you lost but since this is practice you keep everything")
      else:
        print("you survived")
        rnostyprt = input("will you run or stay")
        if rnostyprt == ("stay"):
          print("ok, the monster's hp is ")
          print(mnstrhp)
          atk = pwrlvl
          mnstrhp = mnstrhp - atk
          if mnstrhp <= 0:
            rtrn = input("the monster is dead you gained some skill points you can use those in the store to upgrade abilities do you want to go again or return to the menu")
          if rtrn == ("menu"):
            opt1 = input("would you like to go to the store, fight, or adventure?")
          else:
              print("you attacked it now the monster's health is ")
              print(mnstrhp)
              print("the monster's attack is ")
              print(mnstratk)
              print("he attacks you your health is ")
              plyrhp = plyrhp - mnstratk
              print(plyrhp)
              if plyrhp <= 0:
                 print("you lost but since this is practice you keep everything")
              else:
                  print("you survived")
                  rnostyprt = input("will you run or stay")
                  #if rnostyprt == ("stay"):
##elif opt ==("adventure"):
##  strt = input("you are walking along when you see a fork in the road do you go left or right")
##  if strt == ("right"):
##    fight1 = input("you see a monster in front of you, his bright aura almost blinds you. do you stay or do you fight")
##    if fight1 == ("stay"):
##    else:
##  else:
