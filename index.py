def analyze_text(text):
    # Split the text into words
    words = text.split()

    # Count the total number of words
    total_words = len(words)

    # Count the occurrences of each word
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return total_words, word_counts

def main():
    print("Welcome to the Word Analyzer!")

    while True:
        # Get input text from the user
        text = input("Please enter the text you want to analyze (or type 'exit' to quit): ")

        # Check if the user wants to exit
        if text.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        # Analyze the text
        total_words, word_counts = analyze_text(text)

        # Print the analysis results
        print("\nAnalysis Results:")
        print("Total words:", total_words)
        print("Word counts:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()
