# This is a the skeleton funcitons for the upcoming Blackjacques game
import random


royals = ["J", "Q", "K"]
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def pick_a_card(deck):
    while True:
        suit = random.randint(1,4)
        face = random.randint(1,13)
        if int(str(face)+str(suit)) in deck:
            continue
        else:
            deck.append(int(str(face)+str(suit)))
            break
    if face == 1:
        face = "A"
    elif face > 10:
        face = royals[face - 11]
    suit = suits[suit]
    card = str(face) + " " + str(suit)
    return card, deck


if __name__ == '__main__':
    current_deck = []
    game_over = False
    d_hand = []
    d_total = 0
    pl_hand = []
    pl_total = 0
    while not game_over: # While loop for the whole game to run, can replay
        bust = False
        while not bust:                     # Infinite Loop for player turn
            curr_card, current_deck = pick_a_card(current_deck)
            pl_hand.append(curr_card)
            cc_val = curr_card.split()[0]
            try:
                cc_val = int(cc_val)
            except ValueError:
                if cc_val == "A":
                    cc_val = 11
                else:
                    cc_val = 10
            pl_total += int(curr_card.split()[0])
            if pl_total >= 21:
                bust = True
                break
            print("You got a ", curr_card, " and your current total is ", pl_total)
            while True: # Loop to ensure input
                action = input("Do you want to hit or stay? h/s ")
                if action in ["h","s"]:
                    break
                else:
                    continue
            if action == "h":
                continue
            elif action == "s":
                break
        d_end = False
        while not d_end:
            d




            # TODO: Look into make classes for you and the dealer with the pick card method built in
            # TODO: LOGIC FOR ACE OVERFLOW
            # TODO: CHECK THAT AKQJ ARE THE NUMBERS

            # MID TERM TODOs
            # TODO: Create logic surrounding damage from player to dealer
            # TODO: Write a story around jacques and why hes doing this - a compelling story
                    # IDEA: Each suit is one way of damaging, making this a strategic rock paper scissors type
                    # IDEA: YOU HAVE TO BE FAST with your decisions or you take some damage(?) to encourage splitsecond math-gut decisions
                    # You can parry attacks? you gotta be in the right suit for the opposing type
                        # USE INSPIRATION FROM POKEMON - Either the Poison/Fighting/Psychic/Fairy , or Ghost/Dark/Psychic/Fighting squares


            # LONG TERM TODOs
            # TODO: Look into making this multiplayer


