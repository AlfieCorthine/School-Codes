import time
import random

time.sleep(0.7)

print('''
      - ===== - Menu - ===== - 
      1. BlackJack
      2. Coding Quiz
      3. Number Guess
      4. Calculator
''')    
#menu selection
menu_selection = int(input("Please enter your menu selection > "))
#menu selection 1 - Blackjack
if menu_selection == 1:
    
    H = False
    S = False
    endh = False
    fu = False
    dealerblackjack = False
    playerblackjack = False
    money = 100

    print("==========WELCOME TO BLACKJACK==========")
    time.sleep(1.5)
    print("HERE ARE THE RULES AND GOALS:")
    time.sleep(1.5)
    print("YOUR JOB IS TO GET TO 21")
    time.sleep(1.5)
    print("IF YOU GO ABOVE YOU LOSE")
    time.sleep(1.5)
    print("BECAUSE CODING IS HARD AND I'M LAZY, YOU HAVE NO CHOICE IF ACES ARE 1 OR 11, THEY WILL ALWAYS BE WORTH 11 :)")
    time.sleep(2)

    # Initialize variables
    player1 = random.randint(2, 11)
    player2 = random.randint(2, 11)
    dealer1 = random.randint(2, 11)
    dealer2 = random.randint(2, 11)

    total = player1 + player2
    dealertotal = dealer1 + dealer2

    # Track the number of Aces in the player's hand
    num_aces = 0
    if player1 == 11:
        num_aces += 1
    if player2 == 11:
        num_aces += 1

    # Function to calculate total value considering Aces
    def calculate_total(player_total, num_aces):
        while player_total > 21 and num_aces > 0:
            player_total -= 10  # Change Ace value from 11 to 1
            num_aces -= 1
        return player_total

    print(f"Your cards are: a {player1} and a {player2}")
    time.sleep(1)
    print(f"Your card total is: {total}")
    time.sleep(1)
    print(f"The dealer's visible card is: a {dealer1}")
    time.sleep(1)

    while endh == False:
        # Check for player's Blackjack
        if total == 21:
            print("-------------------------------")
            time.sleep(1)
            print("BLACKJACK!")
            time.sleep(1)
            print("YOU WIN!")
            time.sleep(1)
            print("BEING DEALT A BLACKJACK FIRST ROUND IS A 4.78% CHANCE!")
            time.sleep(1)
            print("MAYBE GO BUY A LOTTERY TICKET?")
            playerblackjack = True
            endh = True
            break

        else:
            print("-------------------------------")
            hitorstand = str(input("Would you like to hit or stand? > "))
            hitorstandf = hitorstand.lower()
            if hitorstandf == 'hit':
                H = True
            elif hitorstandf == 'stand':
                S = True 

        while S != True:
            if H == True:
                player3 = random.randint(2, 11)
                print(f"you're new card is a: {player3}")
                total += player3
                num_aces += 1 if player3 == 11 else 0  # Update number of Aces
                total = calculate_total(total, num_aces)  # Calculate total considering Aces
                print(f"Your new total is: {total}")
                time.sleep(1)
                if total > 21:
                    print("-------------------------------")
                    time.sleep(1)
                    print("You went Bust!")
                    time.sleep(1)
                    print("You lose!")
                    time.sleep(1)
                    print("Better luck next time!")
                    time.sleep(1)
                    endh = True
                    break
                elif total == 21:
                    print("BLACKJACK!")
                    time.sleep(1)
                    print("YOU WIN!")
                    time.sleep(1)
                    print("WELL DONE!")
                    fu = True
                    endh = True
                    break
                else:
                    print("-------------------------------")
                    time.sleep(1)
                    hitorstandfs = str(input("Would you like to hit again or stand? > "))
                    hitorstandff = hitorstandfs.lower()
                    if hitorstandff == 'hit':
                        H = True
                    elif hitorstandff == 'stand':
                        S = True 
                        break

    while fu == False and endh == False:
        print("-------------------------------")
        dealer2 = random.randint(2, 11)
        print(f"The dealer flips the card to reveal: {dealer2}")
        print(f"You're total is: {total} and the dealer's total is: {dealertotal} ")
        time.sleep(2)
        fu = True
        break

    while S == True:
        if dealertotal < total:
            print("-------------------------------")
            dealer3 = random.randint(2, 11)
            print(f"The Dealer reveals another card: {dealer3}")
            dealertotal = dealertotal + dealer3
            print(f"Dealer's total is now: {dealertotal}")
            time.sleep(2)
        else:
            if dealertotal > 21:
                print("-------------------------------")
                print("Dealer is bust!")
                print("You win!, Well Done!")  
                endh = True
                break
            elif dealertotal == total:
                print("-------------------------------")
                print("Dealer has the same as you!")
                print("Dealer wins!")
                endh = True
                break 
            elif dealertotal > 21:
                print("-------------------------------")
                print("Dealer is bust!")
                print("You Win!")
                endh = True
                break
            elif dealertotal == 21:
                print("-------------------------------")
                print("Dealer has BLACKJACK!")
                print("Dealer Wins!")
                dealerblackjack = True
                endh = True
                break

    if dealertotal > total and dealertotal <= 21 and dealerblackjack == False:
        print("-------------------------------")
        print(f"Dealer has {dealertotal}!")
        print(f"You only have {total}!")
        print("You Lose!, Unlucky!") 

    elif dealertotal < total and total <= 21 and playerblackjack == False:
        print("-------------------------------")
        print(f"You have {total}!")
        print(f"Dealer only has {dealertotal}!")
        print("You Win!, Well Done!") 

    time.sleep(2)
    print("**********THANKS FOR PLAYING**********")
    time.sleep(1.5)
    print("*********SUPPORT ME ON GITHUB*********")
    time.sleep(1.5)

#menu selection 2 - Quiz
if menu_selection == 2:
    
    score =0
    
    print('''
          - === - Coding Quiz - === -
          
          Welcome to the Coding Quiz
          
          - This is multiple choice
            so pick the number that 
            corresponds to your 
            answer
    ''')
    
    time.sleep(1)
    
    #Question 1
    print('''Question one: What is this statement coded in?
        
                console.log("Hello, World!");

             1. Java   2. C++   3. C#   4. JavaScript
             
          ''')
    q1_response = int(input("Your answer > "))
 
    #correct/incorrect/invalid
    if q1_response == 4:
        print("Well Done!")
        score = score +1
        print(f"You have 1 point!")
        time.sleep(0.6) 
        
    if q1_response > 4 or q1_response < 1:
        print("Invalid Selection")
        time.sleep(0.7)
        print("Onto the next question!")
        time.sleep(0.6) 
        
    if q1_response != 4:
        print(f'''Sorry number {q1_response} is wrong!
                  The right answer is 4. JavaScript!
                  you have {score} Points!
              ''')        
        time.sleep(0.6) 
    


    #Question 2
    print('''Question two: What language is this coded in?
        
             self.root.geometry("600x400")

             1. HTML   2. Python    3. C#   4. Ruby
             
          ''')
    q2_response = int(input("Your answer > "))
 
    #correct/incorrect/invalid
    if q2_response == 2:
        print("Well Done!")
        score = score +1
        print(f"You have {score} point(s)!")
        
    if q2_response > 4 or q2_response < 1:
        print("Invalid Selection")
        time.sleep(0.7)
        print("Onto the next question!")
        time.sleep(0.6) 
        
    if q2_response != 2:
        print(f'''Sorry number {q2_response} is wrong!
                  The right answer is 2. Python!
                  you have {score} Point(s)!
              ''')    
        
        

    #Question 3
    print('''Question three: What language is this coded in?
        
             #include <iostream>

             int main() {
                 std::cout << "Hello, World!" << std::endl;
                 return 0;
             }

             1. Rust   2. Swift    3. C++   4. HTML
             
          ''')
    q3_response = int(input("Your answer > "))
 
    #correct/incorrect/invalid
    if q3_response == 3:
        print("Well Done!")
        score = score +1
        print(f"You have {score} point(s)!")
        
    if q3_response > 4 or q3_response < 1:
        print("Invalid Selection")
        time.sleep(0.7)
        print("Onto the next question!")
        time.sleep(0.6) 
        
    if q3_response != 2:
        print(f'''Sorry number {q3_response} is wrong!
                  The right answer is 3. C++!
                  you have {score} Point(s)!
              ''')    
    
    
    
    
    #Question 4        
    time.sleep(0.75) 

    print('''Question four: What language is this coded in? 
            
                fn main() {
                    println!("Hello, world!");
                }

        ''')
    print(" 1: Java     2: HTML     3: Rust     4: C++  ")
    print("")
    q4_selection = int(input("Your guess is > "))
    if q4_selection == 3:
        print("Correct!")
        score = score +1
        print(f"You have {score} point(s)!")

    if q4_selection > 4 or q4_selection < 1:
        print("Invalid Selection!")
        time.sleep(1)
        print("Onto the next question!")
        time.sleep(0.7)

    if q4_selection != 3:
        print(f'''Sorry number {q4_selection} is wrong!
                  The right answer is 3. C++!
                  you have {score} Point(s)!
              ''')  
    
    
    #Question 5       
    time.sleep(0.75) 

    print('''Question five: What language is this coded in? 
            
                       puts "Hello, World!"
          
        ''')
    print(" 1: Ruby   2: Sapphire   3: Assembly   4: HolyC  ")
    print("")
    q5_selection = int(input("Your guess is > "))
    if q5_selection == 1:
        print("Correct!")
        score = score +1
        print(f"You have {score} point(s)!")

    if q5_selection > 4 or q5_selection < 1:
        print("Invalid Selection!")
        time.sleep(1)
        print("Onto the next question!")
        time.sleep(0.7)

    if q5_selection != 1:
        print(f'''Sorry number {q5_selection} is wrong!
                  The right answer is 3. Ruby!
                  you have {score} Point(s)!
              ''')
    
    print(f'''
            Thats the end of the Quiz!
            You scored {score}/5!
    ''')
    if score >3:
        print("Well done!")
    else:
        print("Maybe you need to do some more revision!")
    
#menu selection 3
if menu_selection == 3:
    print("3")
    
    
#menu selection 4   
if menu_selection == 4:
    print("4")
