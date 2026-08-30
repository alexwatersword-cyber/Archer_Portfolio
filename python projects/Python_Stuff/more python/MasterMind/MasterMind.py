import random

LENGTH = 4
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def generate_sequence(letters):
    sequence = []
    for i in range(LENGTH):
        letter = random.choice(letters)
        while letter in sequence:
            letter = random.choice(letters)
        sequence.append(letter)
    return ''.join(sequence)
def get_guess(letters):
    guess = input("Enter da guess: ").upper()
    if len(guess) != LENGTH:
        print("Wrong length. Keep on trying. 4 letters pls.")
        guess = get_guess(letters)
    for letter in guess:
        if letter not in letters:
            print("Wrong Letters. Use only english alphabet.")
            guess = get_guess(letters)
            break
    return guess

def check_guess(guess,sequence):
    response = []
    imperfect = 0
    #check how many letters are perfect and imperfect positions
    for i in range(LENGTH):
        if sequence[i] == guess[i]:
            response.append('P')
        elif sequence[i] in guess:
            imperfect += 1
    for _ in range(imperfect):
        response.append('O')
    print(' '.join(response))

def main():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print("Welcome to da game of MasterMind!")
    sequence = generate_sequence(letters)
    guess_count = 0
    guess = ''
    while guess_count < 10 and guess != sequence:
        guess = get_guess(letters)
        check_guess(guess, sequence)
        guess_count += 1
    if guess == sequence:
        print("You win! Da sequence was " + sequence + " You took " + str(guess_count) + " guesses.")
    else:
        print("You lose! Da sequence was " + sequence)
if __name__ == "__main__":
    main()