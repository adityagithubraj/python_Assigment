import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    return 'computer'

def update_score(winner, scores):
    scores[winner] += 1
    return scores

def display_score(scores):
    print(f"User: {scores['user']} | Computer: {scores['computer']} | Draws: {scores['draw']}")

def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == 'yes'

def main():
    scores = {'user': 0, 'computer': 0, 'draw': 0}
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        scores = update_score(winner, scores)
        
        print(f"{winner.capitalize()} wins!")
        display_score(scores)
        
        if not play_again():
            break
    
    print("Thank you for playing Rock, Paper, Scissors!")

if __name__ == "__main__":
    main()
