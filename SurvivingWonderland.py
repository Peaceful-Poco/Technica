global age
global name
global size
global death
global year
death = False
size = ""
name = ""
year = 0
age = 0
def old(year):
    age = 2024- year
    if age>18:
        print("Wow, You are OLD! but you can never be too old for a tea party")
    elif age< 10:
        print("Wow, You are Young! but you can never be too young for  a tea party")
    elif age> 81: 
        print("It is a honor to meet a fellow tea party lover!")
    else:
        print("You there. This tea party is perfect for you")
        
def caterpillar(size):
    Choice_1 = input("The White Rabbit, frightened, leaves his fan and two gloves. \nEnter TAKE to take items or LEAVE to leave them ").lower()
    if(Choice_1 == "take"):
        print("You run away and bump into the card soldiers, who charge you with theft (OFF WITH YOUR HEAD)")
        return True
    elif(Choice_1 == "leave"):
        print("You meet the caterpillar, who is smoking on a mushroom")
        print("He notices you and says "'Wow, you are '""+size+". Here eat a mushroom to return to regular size")
        Choice_2 = input("Choose a side to bite: LEFT or RIGHT: ").lower()
        if(Choice_2 == "left"):
            print("You grow more and alert the guards and get your head crushed")
            return True
        else:
            print("You revert to your original size and continue your journey through wonderland.\n A frog that resembles a henchman hops into your path.")
            Choice_3 = input("Do you CHASE after the henchman or CALL after the henchman: ").lower()
            if(Choice_3 == "chase"):
               print("You chase after it and lose sight of it. You walk straight and hope for the best.")
            else: 
               print("The frog henchman hops and squashes you")
               return True
               
 
    else: 
        print("The caterpillar gets angry and blows smoke in your face knocking you unconscious ")
        return True


    
def garden(): 
    print("You meet card gardeners Two, Five, and Seven, who are bickering as they paint the white roses on rose trees red.\nThey admit that they painted the trees white by mistake and need to paint them red before the Queen of Hearts finds out.")
    Choice_1 = input("Will you help them or report them?\nEnter YES to help and NO to report: ").lower()
    if(Choice_1== "yes"):
        print("You help the soldiers paint the roses -but you do not finish in time.\nAs the Queen is giving the order for beheading, she sees that you are human.")
        Choice_2 = input("\nArgue for your innocence (Y) or Argue for the soldiers innocence (N): ").lower()
        if(Choice_2 == "y"):
            print("\nYou successfully avoid a beheading, and use the Queens trust to request for the freedom of the card gardeners. ")
                
            Choice_3  = input("\nThe Queen gives you a task to collect all the bread butterflies in the garden in exchange for the gardeners life. \nChoose to AGREE or DISAGREE: ").lower()
            if(Choice_3 == "agree"):
                print("\nYou capture all the red butterflies except for 1 and the Queen agrees to set the gardeners free. \nHowever, the Queen is outraged that you did not collect all of the bread butterflies.\nShe orders for you to be taken to court.")
            else:
                print("\nThe Queen is outraged at your audacity (she was going to eat the butterflies) and orders for your death")
                return True
                    
                    
        else:
            print("The Queen is furious that you decided to help rule breakers and orders for you to be beheaded with them")
            return True
        
        
    else:
        print("The Queen notices that the roses are not red and orders the beheading of Two, Five, and Seven.")
        print("Feeling guilty over your actions, you run into a forest and cannot find a way out.")
        return True
def final():
    print("You keep walking and eventually stumble onto the croquet court of the Queen of Hearts. The rabbit comes back")
    EndChoice_1 = input("Type YES to follow the rabit or NO to go on your own: ").lower()
    if(EndChoice_1 == "yes"):
        print("He teaches you how to play. Hedgehogs were used as balls, flamingos were used as mallets, and soldiers acted as hoops")
        print("Then, One of the players is caught cheating and the queen orders his beheading. \nYou think that the punishment is too harsh for the crime.")
        EndChoice_2 = input("Do you DEFEND the player or stay SILENT: ").lower()
        if(EndChoice_2 == "defend"):
           print("The Queen is angry and kills you")
           return True
        else:
           print("\nThe player gets beheaded and you, in a daze, rush out. \nThe Queen is pleased that you did not object to her ruling and lets you run away. \nYou meet the Cheshire Cat and the Duchess and they ask if they want to join them")
        
            
    else:
        print("\nYou find a dark hallway and walk down. \nAt the other end of the hallway, you see the Cheshire Cat and Duchess and they ask if you want to join them.")
    EndChoice_3 = input("\nDo you choose to AGREE or DISAGREE: ")
    if(EndChoice_3 == "agree"):
       print("\nYou find the Mad Hatter and March Hare having a tea party");
    else:
        print("The duchess gets mad and sprays you with lethal hot tea")
        return True
    

print("Welcome to Technica Wonderland! Wonder awaits...");
name = input("What is your name? ");
year = int(input("\nWhat year were you born? "));

enter = input(name+ ", Would you like to go down the rabbit hole? Enter Yes or No: ").lower()
if(enter == "no"):
    print("Someone pushs you in with a Wideeee Grin :)")
else:
    print("You jumped in with no hesitation")
print("\nAs you fall, you meet a white rabbit. You curiously follow the rabbit down the hole and you spot a cottage in the distance.\n You enter the house and see a tiny room with a lit up fireplace, a couch, and a table with unknown items. ")
while(death != True):
    print("White Rabbit: “\n'Do you want any refreshments?'” while pointing to the table.")
    Choice_1= input("\nThere is a Drink me Bottle and an Eat me Cookie\n Enter Bottle, Cookie or None: ").lower()
    if Choice_1 == "bottle":
        print("\nYOU ARE SHRinking...")
        size = " really small"
        caterpillar(size)
        
    elif Choice_1 == "cookie": 
        print("\nYou are GROWING!!!")
        size = "HUGE!"
        death = caterpillar(size)
    else:
        print("\nThe rabbit takes you to the garden...")
        death = garden()   
    if (death != True):
        death = final()
        if(death!= True):
            print("Mad Hatter: Welcome to the MAd HatTers Tea Party!/n Congrats,You have made it to my tea party!")
            old(year);

        death = True
        
print("\nYou hear distant calling and it is your sister saying: Wake up " + name + "! \nYou been asleep for too long, it is time for Technica.")    