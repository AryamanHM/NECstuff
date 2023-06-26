from collections import Counter

def get_top_words(file_path, top_n):
    # Read the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Remove punctuation marks and convert to lowercase
    text = text.lower()
    text = ''.join(c if c.isalnum() else ' ' for c in text)

    # Split the text into words
    words = text.split()

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Sort the words based on occurrences in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Display the top N words
    top_words = sorted_words[:top_n]

    for word, count in top_words:
        print(f"{word}: {count}")

# Test the function
file_path = 'example.txt'  # Replace with the path to your text file
top_n = 10

get_top_words(file_path, top_n)
