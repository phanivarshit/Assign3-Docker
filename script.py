import os
import collections
import socket

# File paths
file1_path = "/home/data/IF-1.txt"
file2_path = "/home/data/AlwaysRememberUsThisWay-1.txt"
output_path = "/home/data/output/result.txt"

# Function to read file and count words
def count_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        words = file.read().lower().split()
        return collections.Counter(words)

# Function to handle contractions
def expand_contractions(text):
    contractions = {"I'm": "I am", "can't": "cannot", "don't": "do not"}
    for contraction, full_form in contractions.items():
        text = text.replace(contraction, full_form)
    return text

# Process files
counts1 = count_words(file1_path)
counts2 = count_words(file2_path)

# Grand total words
total_words_file1 = sum(counts1.values())
total_words_file2 = sum(counts2.values())
grand_total = total_words_file1 + total_words_file2

# Top 3 words in file1
top_3_file1 = counts1.most_common(3)

# Expand contractions and count words in file2
with open(file2_path, 'r', encoding='utf-8') as file:
    expanded_text = expand_contractions(file.read().lower())
    counts2 = collections.Counter(expanded_text.split())

top_3_file2 = counts2.most_common(3)

# Get IP Address
ip_address = socket.gethostbyname(socket.gethostname())

# Prepare output
output = f"""
Total words in IF-1.txt: {total_words_file1}
Total words in AlwaysRememberUsThisWay-1.txt: {total_words_file2}
Grand total words: {grand_total}

Top 3 words in IF-1.txt:
{top_3_file1}

Top 3 words in AlwaysRememberUsThisWay-1.txt (after handling contractions):
{top_3_file2}

Machine IP Address: {ip_address}
"""

# Write output to file
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(output)

# Print to console
print(output)