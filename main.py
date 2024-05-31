import sys
from collections import defaultdict
import os

def group_anagrams(words):
    # Create a dictionary to store anagrams, with a default value of an empty list
    anagrams = defaultdict(list) 
    # Iterate over each word
    for word in words:
        if not is_word_alphabetic(word):
            # Raise an error if the word contains non-alphabetic characters
            raise ValueError(f"Error: Words should not contain special characters or numbers.")
        sorted_word = ''.join(sorted(word))  # Sort the characters of the word to get the anagram key
        if word not in anagrams[sorted_word]:  # Check for duplicate sorted words
            anagrams[sorted_word].append(word) # Append the word to the list of anagrams for the sorted key
    return anagrams

def is_word_alphabetic(word):
    return word.isalpha() # Check if the word consists only of alphabetic characters

def write_anagrams_to_file(anagrams, input_filename):
    # Write the grouped anagrams to the input file
    with open(input_filename, 'w') as file:
        for i, group in enumerate(anagrams.values()):
            file.write(' '.join(group))
            if i < len(anagrams) - 1:
                file.write('\n')
                
def process_chunk(chunk, input_filename):
    words = chunk.split()  # Split the chunk into words
    anagrams = group_anagrams(words)# Group the words into anagrams
    write_anagrams_to_file(anagrams, input_filename)  # Write the anagrams to the file

def process_file_for_anagrams(input_filename):
    # Set the chunk size for processing the file in chunks
    chunk_size=10000
    # Check if file is txt file and if it exist
    if not input_filename.endswith('.txt') and not os.path.isfile(input_filename):
        raise ValueError("Error: File must exist and must be a text file with a .txt extension")  
    # check if file is not empty
    with open(input_filename, 'r') as file:
        words = [line.strip() for line in file if line.strip() != '']
    if not words:
        raise ValueError("Error: File provided is empty") 
    with open(input_filename, 'r') as file:
        chunk = ''
        # Read input file line by line
        for line in file:
            chunk += line
            # Process the chunk if it reaches the chunk size
            if len(chunk.split()) >= chunk_size:
                process_chunk(chunk, input_filename)
                chunk = ''
        if chunk:
            process_chunk(chunk, input_filename)
    print(f"Anagrams grouped and written to {input_filename}")

if __name__ == '__main__':
     # Check if the program is run with exactly one argument
    if len(sys.argv) == 2:       
        input_filename = sys.argv[1]
        process_file_for_anagrams(input_filename)
    else:
        # Display error in command line if error occurs when wrong argument is provided
        print("Error: Wrong Arguments or Format Provided\n"
              "Please follow this example format - python example.py data.txt")
        sys.exit(1)