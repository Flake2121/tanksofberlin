from random import randint
from time import sleep
from os import system
from platform import system as systemType
from math import ceil

RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[0;36m"
END = "\033[0m"


print("July 12th 1944\nYour push into France worked.\nYou are a tank commander and your task is to spearhead into berlin.\nYou're in a comet tank featuring good mobility, a powerful gun but a lack of armour...")
distanceleft=1200
chancet=0
tfuel=600
tankencounter=randint(1,100)

tankName=""
enemyLowerFront=0
enemyUpperFront=0
enemyTurretFront=0

enemyAccuacy=0
enemyShellPower=0

enemyDead=False
dead=False

enemyAim=0

freindlyLowerFront=30
freindlyUpperFront=30
freindlyTurretFront=30

def battle(tankType):
    if not dead:
        enemyDead=False
        if tankType <=20:
            tankName="Panzer IV"
            enemyLowerFront=90
            enemyUpperFront=95
            enemyTurretFront=90
            enemyShellPower=0.6
            enemyAccuacy=0.5
        elif tankType >=21 and tankType <=30:
            tankName="Stug"
            enemyLowerFront=85
            enemyUpperFront=85
            enemyTurretFront=-1
            enemyShellPower=0.65
            enemyAccuacy=0.5
        elif tankType >=31 and tankType <=40:
            tankName="Tiger 1"
            enemyLowerFront=75
            enemyUpperFront=80
            enemyTurretFront=60
            enemyShellPower=0.7
            enemyAccuacy=0.5
        elif tankType >=41 and tankType <=60:
            tankName="Panther"
            enemyLowerFront=70
            enemyUpperFront=20
            enemyTurretFront=50
            enemyShellPower=0.8
            enemyAccuacy=0.5

        elif tankType >=61 and tankType <=65:
            tankName="Tiger 2"
            enemyLowerFront=20
            enemyUpperFront=1
            enemyTurretFront=25
            enemyShellPower=0.92
            enemyAccuacy=0.5

        elif tankType >=65 and tankType <=70:
            tankName="Jagdpanther"
            enemyLowerFront=60
            enemyUpperFront=25
            enemyTurretFront=25
            enemyShellPower=0.92
            enemyAccuacy=0.5
        else:
            tankName=RED + "Maus (satin embodied)" + END
            enemyLowerFront=1
            enemyUpperFront=1
            enemyTurretFront=1
            enemyShellPower=5
            enemyAccuacy=1



        print("You have encounterd a" + GREEN, tankName + END)


        if randint(1,2)==1:
            print("They spotted you before you could fire")
            engagement(enemyShellPower, enemyAccuacy)



        while not enemyDead and not dead:
        
            aim=input("Where do you want to aim? [1: Upper Front ,2: Lower Front ,3: Frontal Turret]")

            if aim.isnumeric():
                aim=int(aim)
            else:
                print("Thats not a number")
                aim=input("Where do you want to aim? [1: Upper Front ,2: Lower Front ,3: Frontal Turret]")


            
            if randint(1,100)>80:
                aim=randint(1,4)
            
            if aim == 1:
                if randint(1,100)<enemyUpperFront:
                    print("You hit the upper front plate - Target Destroyed")
                    enemyDead=True
                else:
                    print("You hit the upper front plate - Non Pen")
            
            if aim == 2:
                if randint(1,100)<enemyUpperFront:
                    print("You hit the lower front plate - Target Destroyed")
                    enemyDead=True
                else:
                    print("You hit the lower front plate - Non Pen")
            
            if aim == 3:
                if randint(1,100)<enemyUpperFront:
                    print("You hit the frontal turret - Target Destroyed")
                    enemyDead=True
                else:
                    print("You hit the frontal turret - Non Pen")
            
            if aim == 4:
                print("Miss!")

            if not enemyDead:
                engagement(enemyShellPower, enemyAccuacy)



def engagement(enemyPen, enemyAccuacy):
    enemyAim=randint(1,ceil((1/enemyAccuacy*100)*300))
    
    print("The enemy are now scoping in on you")

    sleep(0.4)

    if enemyAim==1:
        if randint(1,100)<freindlyUpperFront*enemyPen:
            print("The enemy hit youre upper front plate - " + RED + "Dead" + END)
            dead = True
            enemyDead = True
            input()
            exit()
        else: 
            print("The enemy fired at you're upper front plate - Non Pen")
    
    if enemyAim==2:
        if randint(1,100)<freindlyLowerFront*enemyPen:
            print("The enemy hit youre lower front plate - " + RED + "Dead" + END)
            dead = True
            enemyDead = True
            input()
            exit()
        else: 
            print("The enemy fired at you're lower front plate - Non Pen")
    
    if enemyAim==3:
        if randint(1,100)<freindlyTurretFront*enemyPen:
            print("The enemy hit youre turret front - " + RED + "Dead" + END)
            dead = True
            enemyDead = True
            input()
            exit()
        else: 
            print("The enemy fired at you're turret front - Non Pen")





while distanceleft>0:
    tankencounter=randint(0,100)
    print("You have",distanceleft,"km to go and you have",tfuel,"lites of fuel left")
    print("You travel 20km")
    
    
    
    tfuel=tfuel-50
    distanceleft=distanceleft-20
    chancee=randint(1,1)
    if chancee==1:
        battle(tankencounter)
    
    
    
    if tfuel<=0:
        print("game over")
        break
    if dead:
        break
    
    """if systemType() == "Windows":
        system("cls")
    else:
        system("clear")"""
    print("nig*a")