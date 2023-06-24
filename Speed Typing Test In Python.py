import time

def run_typing_test():
    # Prompt the user to enter a passage to type
    passage = input("Enter the passage to type:\n")

    # Print empty lines to clear the screen
    print("\n" * 50)

    # Start the timer
    start_time = time.time()

    # Prompt the user to start typing
    input("Start typing. Press Enter when finished.\n")

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Calculate the number of words typed
    words = passage.split()
    word_count = len(words)

    # Calculate the typing speed in words per minute (WPM)
    typing_speed = word_count / (elapsed_time / 60)

    # Print the typing speed and elapsed time
    print(f"\nElapsed Time: {elapsed_time:.2f} seconds")
    print(f"Word Count: {word_count}")
    print(f"Typing Speed: {typing_speed:.2f} WPM")

run_typing_test()
