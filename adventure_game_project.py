import random
enemy = ["Jason", "Michael", "Leatherface"]
intro = ["He will cut you.", "You can run, but he can walk faster", "He thinks you have nice skin, he wants to wear it."]
userName=input("Please enter your first name: ")

class Adventurer:
    # This will initialize the pieces for the adventurer
    def __init__(self, name, keys, health_points,damage):
        self.name = name
        self.position = 0
        self.keys =0
        health_points=100
        self.health_points = health_points
        self.damage = 0
        
       

class Enemy:
    # This will initialize the pieces for the adventurer
    def __init__(self, name, position,damage,healthPoints):
        self.name = name
        self.position = position
        self.damage = damage
        healthPoints=100
        self.healthPoints=healthPoints
        
def MichaelEnemy(self,name,position,damage,healthPoints):
    self.name=name
    str(self.position)
    str(self.damage)
    str(self.healthpoints)
def JasonEnemy(self,name,position,damage,healthPoints):
    self.name=name
    str(self.position)
    str(self.damage)
    str(self.healthpoints)
def LeatherfaceEnemy(self,name,position,damage,healthPoints):
    self.name=name
    str(self.position)
    str(self.damage)
    str(self.healthpoints)
  
          
def gameoverblock():#This was created to avoid duplicating the same piece of code, and to create an organized and easy to follow final product 
    print("---------------------------------------------------------------")
    print("                           GAME OVER                           ")
    print("---------------------------------------------------------------")
    
def linebreak():
    print("---------------------------------------------------------------")
        

def game(adventurer, enemies, room):
    for i in range(1, room+1): # Loop over the room
        input("\n---Press RETURN/ENTER to run towards the door.---\n") 
        adventurer.position = i # Move adventurer forward
        print(adventurer.name," you are in room ",str(adventurer.position))
        
        adventurer.health_pointss = 100-(100-adventurer.health_points)
        print("You have ",str( adventurer.health_pointss),"/100 health points left.")
        
        adventurer.keyss = 0+adventurer.keys
        print("You currently have ",(str(adventurer.keyss))," key(s).")#Shows the user how many keys they have collected thus far. 
        
        if random.randint(0,1)==0:#If random integer is 0, the user will have a chance to find a key
            pickup=random.randrange(0,2)
            adventurer.keys+=pickup
            adventurer.keyss = 0+adventurer.keys
            print("You found ",str(pickup)," key(s) in this room!") 
        elif random.randint(0,1)!=0:#If random integer is 1, the user does not find a key
            print("You did not find any keys in this room, keep moving!")
            adventurer.keyss = 0+adventurer.keys
 
        for enemy in enemies:
            if adventurer.position == enemy.position:#If the enemy and the adventurer end up in the same position, they are faced with another choice 
                print("You have encountered ",enemy.name+"!")
                if enemy.name=="Jason":
                    print("He will cut you!")
                elif enemy.name=="Michael":
                    print("You can run, but he can walk faster!")
                elif enemy.name=="Leatherface":
                    print("He thinks you have nice skin, he wants to wear it!")# If there's an enemy at this position,
                   
                fightorflight=input("Do you want to run(r) or fight(f)?\n").lower()#If the user selects f, they will fight. If not, they will move on. 
                
                if fightorflight == "f":
                    print(userName,",you have chose to fight!")
                    if random.randrange(0,2) == 0:#The user has a chance to either escape the enemy, or lose. If 0, they will get attacked. 
                        adventurer.health_points -= enemy.damage # this will cause damage to the adventurer
                        print("You got attacked by ", enemy.name, " and lost ",str(enemy.damage),"health_points")
                    else:
                        print("You defeated ",enemy.name," this round, and got away unharmed.")
                        pickup=random.randrange(1,2)#the user will recieve a key for escaping the enmy. They have a chance to find one, or two. 
                        adventurer.keys+=pickup
                        print("Received ",str(pickup)," keys.")#This tells the user how many keys they picked up. 
                        adventurer.keyss = 0+adventurer.keys
                        
                        if random.randrange(0,1) == 0:                        
                            enemy_healthpoints=100#Starting total for enemy health 

                            if enemy.name=="Jason":
                                enemy_damage=random.randrange(10,20)
                                JasonEnemy.healthPoints=JasonEnemy.healthPoints-enemy_damage
                                JasonEnemy.healthPointss=100-(100-JasonEnemy.healthPoints)
                                enemy_healthpoints-=adventurer.damage
                                print("Jason lost "+(str(enemy_damage))+" health points.")
                                print("Jason has",JasonEnemy.healthPointss," /100 health points left")
                            elif enemy.name=="Michael":
                                enemy_damage=random.randrange(10,20)
                                MichaelEnemy.healthPoints=MichaelEnemy.healthPoints-enemy_damage
                                MichaelEnemy.healthPointss=100-(100-MichaelEnemy.healthPoints)
                                enemy_healthpoints-=adventurer.damage
                                print("Michael lost "+(str(enemy_damage))+" health points.")
                                print("Michael has",MichaelEnemy.healthPointss," /100 health points left")
                            elif enemy.name=="Leatherface":
                                enemy_damage=random.randrange(10,20)
                                LeatherfaceEnemy.healthPoints=LeatherfaceEnemy.healthPoints-enemy_damage
                                LeatherfaceEnemy.healthPointss=100-(100-LeatherfaceEnemy.healthPoints)
                                enemy_healthpoints-=adventurer.damage
                                print("Leatherface lost "+(str(enemy_damage))+" health points.")
                                print("Leatherface has",LeatherfaceEnemy.healthPointss," /100 health points left")
                   
                elif fightorflight =="r":#If the user enters r they have chosen to run
                    print(userName,",you have chose to run!")
                    if random.randrange(0,2) == 0:#If the random range is equal to 0, then the adventurer gets attacked 
                        adventurer.health_points -= enemy.damage # it causes damage to the adventurer
                        print("You didn't run fast enough and got attacked by ",enemy.name," and lost the battle. You lost ",str(enemy.damage)," health points")
                        adventurer.keyss = 0+adventurer.keys
                    else:
                        print("Most people do not run fast enough to get away. You escaped ",enemy.name)#If adventurerer is not"attacked" they are told they were able to escape. 
                break 
              
        if adventurer.health_points <= 0: #If the adventurer health points fall below 0, the game will come to an end
            gameoverblock()
            print("\n\n",adventurer.name," you were unable to escape, you lost. ")
            linebreak()
            print("You made it to the final room ",adventurer.name," now it is time for the final challenge","\n")
            print("Adventurer : " + adventurer.name)
            print("Adventurer Position : " + str(adventurer.position))
            print("Adventurer Total Keys : " + str(adventurer.keys))
            print("Adventurer Total Health Points : " + str(adventurer.health_points) + "/100")
            linebreak()
            break
        
    else:#if the adventurer health points did not fall below 0 or equal 0
        linebreak()
        print("You made it to the final room ",adventurer.name," now it is time for the final challenge","\n")
        print("Adventurer : " + adventurer.name)
        print("Adventurer Position : " + str(adventurer.position))
        print("Adventurer Total Keys : " + str(adventurer.keys))
        print("Adventurer Total Health Points : " + str(adventurer.health_points) + "/100")
        linebreak()   
        print("You have gathered","keys","you must try your key(s) to see if you can escape. The number of guesses you get correspond to the number of keys you gathered. Choose a number between 1 and 10")
        keyTries=adventurer.keys#The amount of attemps are equal to the number of keys in which the adventurer acquired 
        keyRandom=random.randint(1,10)#A random number is generated, in which the user is then needing to guess. 

        for key in range(keyTries):
            key=key+1#This will keep track of the number of iterations completed 
            targetSum=(int(input("Enter the guess:"))) 
            if targetSum == keyRandom:#If the guess is correct the game will end with a message telling them they won
                gameoverblock()
                print("You did it! You not only defeated dangerous enemies, made it to the last room, and made it to the last room, but you also had the right key!")
                print("You're safe. You won!")
                linebreak()
                break
            elif targetSum != keyRandom:#If the guess is incorrect they will be prompted to enter until guesses run out
                print("That was not the right number, try again!")
            if key>= keyTries:#Once the amount of user guesses are equal to or greater than the allotted number of guesses, the game will end. 
                gameoverblock()
                print("As you fumbled with the keys, to guess the right one, you were attacked, and could not escape in time. You did not survive. You lost. The correct number was "+(str(keyRandom))+"!")
                linebreak()
 
 
def welcomeMessage():#This provides the user with an idea of what they can expect during the course of the text game 
    linebreak()
    print("Welcome",userName,", Here you will face dangerous enemies, and it will be your choice if you run or fight. Every choice has an impact on your future, will you make the right one?\n")
    print(userName,",you will come in contact with dangerous individuals, all wanting one thing and that is to keep you from escaping the door that leads outside of the house you're in. There are nine rooms you must get through to get to the door. If you make it to the final room, there will be one final challenge awaiting you\n")
    print("As you advance through the rooms you have a chance of finding a key, battling an enemy, or both. Those keys will come in handy later. The more keys you gather, the more chances you have for the final challenge at the end.\n")
    print("The three enemies you may come in contact with are:")
    print("     Jason, he will cut you. \n     Michael, you can try to run from him but he walks faster. \n     Leatherface, he likes your skin, he wants to wear it.\n")
    print("Ready, set, run...")
    linebreak()
            
def main():
    welcomeMessage()

    room = 9#Nine rooms 
    adventurer = Adventurer(userName, 0, 100,(20,30))
    num_enemies = random.randint(int(0.90*room), int(0.95*room))#90-95% chance of enountering an enemy in a room
    enemies = []
    
    for _ in range(num_enemies):
        enemy_name,enemy_intro = random.choice(enemy),random.choice(intro)
        enemy_position, enemy_damage = random.randint(1, room), random.randint(15, 25)
        enemies.append(Enemy(enemy_name, enemy_position,enemy_damage,enemy_intro))
        
        JasonEnemy.healthPoints=100
        MichaelEnemy.healthPoints=100  
        LeatherfaceEnemy.healthPoints=100
   
    game(adventurer, enemies, room)
    
    print("Enemy Final Health Points:")#Message to output the final health points for enemies 
    print("     ","Jason health points:",JasonEnemy.healthPointss)
    print("     ","Michael health points:", MichaelEnemy.healthPoints)
    print("     ","Leatherface health points:",LeatherfaceEnemy.healthPoints)
   
main()

