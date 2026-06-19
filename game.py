import random
import black_jack_logo
print("\n********WELCOME TO GAME OF BLACK JACK**************\n")

game = True

while game:

    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    user_cards = []
    computer_cards = []

    start = input(
        "Do you want to play the game of black jack.\nType 'y' for yes and 'n' for no: "
    )

    if start == 'y':
        
        print(black_jack_logo.art)

        # Initial deal
        for i in range(2):
            user_card = random.choice(cards)
            user_cards.append(user_card)
            cards.remove(user_card)

            computer_card = random.choice(cards)
            computer_cards.append(computer_card)
            cards.remove(computer_card)

        user_score = sum(user_cards)
        computer_score = sum(computer_cards)

        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: [{computer_cards[0]}]")

        # User turn
        while user_score < 21:

            pass_chance = input(
                "Type 'y' to get another card, type 'n' to pass: "
            )

            if pass_chance == 'n':
                break

            user_card = random.choice(cards)
            user_cards.append(user_card)
            cards.remove(user_card)

            user_score = sum(user_cards)

            # Ace handling
            if user_score > 21 and 11 in user_cards:
                user_cards[user_cards.index(11)] = 1
                user_score = sum(user_cards)
                

            print(f"Your Cards: {user_cards}, current score: {user_score}")

        # Computer turn
        computer_score = sum(computer_cards)

        if computer_score > 21 and 11 in computer_cards:
            computer_cards[computer_cards.index(11)] = 1
            computer_score = sum(computer_cards)

        while computer_score < 17:

            computer_card = random.choice(cards)
            computer_cards.append(computer_card)
            cards.remove(computer_card)

            computer_score = sum(computer_cards)

            if computer_score > 21 and 11 in computer_cards:
                computer_cards[computer_cards.index(11)] = 1
                computer_score = sum(computer_cards)

        print(f"\nYour final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}\n")

        # Result
        if user_score > 21:
            print("OPPS!! Sorry, you went over 21.\n")

        elif computer_score > 21:
            print("Hurray!!! You win. Computer went over 21.\n")

        elif user_score > computer_score:
            print("Hurray!!! You win.\n")

        elif computer_score > user_score:
            print("OPPS!! Sorry, computer got you.\n")

        else:
            print("It is a draw. Go again!\n")

    elif start == 'n':
        game = False
        print("\nNO Problem!! Come again soon")