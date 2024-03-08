def count_words(text):
    """
    Counts the number of words in a given text.
    """
    # Remove punctuation and convert the text to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum() or e.isspace()).lower()

    # Split the cleaned text into words
    words = cleaned_text.split()

    # Count the number of unique words
    word_count = len(set(words))

    return word_count


def main():
    # Prompt the user to enter a sentence or paragraph
    text = input("Enter a sentence or paragraph: ")

    # Check if the input is empty
    if not text:
        print("Error: The input is empty.")
        return

    # Count the number of words in the input
    word_count = count_words(text)

    # Print the word count to the console
    print(f"The number of words in the input is: {word_count}")


if __name__ == "__main__":
    main()

