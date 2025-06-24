import cards 

def main():
    while True:
        user_input = input("Enter the number of players(2-10): ").strip().lower()
        if user_input in ("bye", "exit"):
            break


        try:
            num_players = int(user_input)
            if num_players < 2 or num_players > 10:
                raise ValueError("Number of players must be between 2 and 10.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue


        hands = cards.deal(num_players, 5)
        print(f"Dealt hands for {num_players} players:")
        for i, hand in enumerate(hands, 1):
            print(f"Player {i}: {' '.join(str(card) for card in hand)} is a {cards.poker_classification(hand)}")
        print("Press Enter to deal again or type 'bye' or 'exit' to quit.")
        if input().strip().lower() in ("bye", "exit"):
            break


if __name__ == "__main__":
    main()
    print("Goodbye!")
