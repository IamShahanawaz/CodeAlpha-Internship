import random

def hangman():
    words = ["python", "code", "alpha", "intern", "script"]
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("🎮 Welcome to Hangman! You have 6 lives.")
    
    while attempts > 0 and '_' in guessed:
        print("\nCurrent Word:", ' '.join(guessed))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("⚠️ Already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed[idx] = guess
        else:
            print("❌ Wrong guess!")
            attempts -= 1
            print(f"Lives left: {attempts}")

    if '_' not in guessed:
        print(f"\n🎉 You won! The word was '{word}'.")
    else:
        print(f"\n💀 You lost! The word was '{word}'.")
