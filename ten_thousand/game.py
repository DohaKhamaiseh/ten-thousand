from ten_thousand.game_logic import GameLogic
# ten_thousand.
score = 0
total = 0
# rounds=15

<<<<<<< HEAD


rounds=15

def play(roller=GameLogic.roll_dice):
    global total
    total = 0
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    user_input = input("> ")
    if user_input.lower() != "y":
=======
def play(roller=GameLogic.roll_dice, num_round=15):
    '''
    Play is a Method responsible for Running the game 
    This method receives two parameters :
     roller param: to generate random numbers for dices
     num_round param: number rounds to roll the dice and the max allowed to user is 15 round
     returns: Game version2 as its required.

    '''
  
    score = 0
    global dice_roller
    dice_roller = roller
    total =0

    def start_game(num_round):
        '''
       start_game is a Method responsible for starting the game ,exactly the first round and to represnt as sim file.
       receives num_round param: to initiate the game round by round
        '''
        nonlocal score
        dec_round = 0
        nonlocal total
        def bank(num):
            nonlocal score
            if(num_round==1):
              score = num
              print("You banked " + str(num) + " points in round " + str(dec_round))
              print("Total score is " + str(score) + " points")
            else:
                nonlocal total 
                total+=score
                print("You banked " + str(num) + " points in round " + str(dec_round))
                print("Total score is " + str(total) + " points")

           

        def quit():
            '''
             quit is a Method responsible for quitting the game ,when the user inser "q"
       
            '''
            print("Thanks for playing. You earned " + str(total) + " points")

        while num_round > 0:

            dec_round += 1
            num_dice = 6
            
            print("Starting round " + str(dec_round))
            formatted_roll = format_roller(dice_roller(6))
            print("Rolling 6 dice...")
            print(formatted_roll)
            print("Enter dice to keep, or (q)uit:")

            input2 = input("> ")
            rem_input2 = input2.replace("> ", "").strip()
            if rem_input2 == "q":
                quit()
                return 
            else:
                # bank_count_int=int(rem_input2)
                if len(rem_input2)==1:
                    # bank_count_int=int(rem_input2)
                    score = GameLogic.calculate_score((int(rem_input2),))
                    num_dice -= 1
                else:
                    list_num = [int(d) for d in rem_input2]
                    t= tuple(list_num)
                    score = GameLogic.calculate_score(t)
                    num_dice -= len(rem_input2)
               
                # score = GameLogic.calculate_score(rem_input2)
                banked_count = score
                print("You have " + str(banked_count) + " unbanked points and " + str(num_dice) + " dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")

                input3 = input("> ")
                rem_input3 = input3.replace("> ", "").strip()
                if rem_input3 == "b":
                    bank(banked_count)
                    # num_dice=
                elif rem_input3 == "q":
                    quit()
                else:
                    pass

            num_round -= 1
            num_dice = 0
           
           

    def user_input():
        '''
         user_input is a Method responsible for acquiring inputs from user about what to bank and how many times to roll dices.
        '''
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        input1 = input("> ")
        rem_input1 = input1.replace("> ", "").strip()
        return rem_input1

    user = user_input()
    if user == "y":
        start_game(num_round)
    else:
>>>>>>> main
        print("OK. Maybe another time")
        return
    
    for num_round in range(1, 4):
        print(f"Starting round {num_round}")
        num_dice = 6
        round_score = 0
        while True:
            dice = roller(num_dice)
            # print(dice)
            print("Rolling " + str(num_dice) + " dice...")
            formatted_roll = format_roller(dice)
            print(formatted_roll)
           
            if GameLogic.calculate_score(dice) == 0:
             print("****************************************")
             print("**        Zilch!!! Round over         **")
             print("****************************************")
             print(f"You banked 0 points in round {num_round}")
             print(f"Total score is {total} points")
             num_round +=1
             print(f'Starting round {num_round}')
             point = 0
             num_dice = 6
             continue
            
            input_str = input("Enter dice to keep, or (q)uit:\n> ")
            if input_str == "q":
                print(f"Thanks for playing. You earned {total} points")
                return
            kept_dice = tuple(int(d) for d in input_str.replace(" ","") if d.isdigit())
            
            val = GameLogic.validate_keepers(dice,kept_dice)
            while (val==False):
                print("Cheater!!! Or possibly made a typo...")
                print("*** ", " ".join(str(d) for d in dice), " ***")
                input_str = input("Enter dice to keep, or (q)uit:\n> ")
                if input_str == "q":
                 print(f"Thanks for playing. You earned {total} points")
                 return
                else:
                    kept_dice = tuple(int(d) for d in input_str.replace(" ","") if d.isdigit())
                    val = GameLogic.validate_keepers(dice,kept_dice)
                
                
 
            round_score += GameLogic.calculate_score(kept_dice)
            num_dice -= len(kept_dice)
            unbanked_score = round_score + total
            print(f"You have {round_score} unbanked points and {num_dice} dice remaining")
            input_str = input("(r)oll again, (b)ank your points or (q)uit:\n> ")
            if input_str == "b":
                total += round_score
                print(f"You banked {round_score} points in round {num_round}")
                print(f"Total score is {total} points")
                break
            elif input_str == "q":
                print(f"Thanks for playing. You earned {total} points")
                return
            elif input_str == "r":
                continue
            else:
                print("Invalid input. Try again.")
    print(f"Thanks for playing. You earned {total} points")
           
    # user = user_input()
    # if user == "y":
    #   start_game()
    # else:
    #  print("OK. Maybe another time")
   

def format_roller(dice_roller):
    as_string = [str(value) for value in dice_roller]   
    format_roll = " ".join(as_string)
    return f"*** {format_roll} ***"
    
if __name__ == "__main__":
    play()
 