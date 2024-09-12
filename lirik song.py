import random

# Define a list of words and phrases for the lyrics
words = ["love", "heart", "pain", "tears", "smile", "laugh", "cry", "dream", "night", "day"]
phrases = ["in the dark", "with you", "without you", "forever", "never", "always", "sometimes", "maybe"]

# Define a function to generate a random lyric line
def generate_lyric_line():
    line = ""
    num_words = random.randint(2, 5)
    for i in range(num_words):
        word = random.choice(words)
        line += word + " "
    phrase = random.choice(phrases)
    line += phrase
    return line.capitalize()

# Define a function to generate a song lyrics
def generate_lyrics(num_lines):
    lyrics = ""
    for i in range(num_lines):
        line = generate_lyric_line()
        lyrics += line + "\n"
    return lyrics

# Generate a song lyrics with 8 lines
lyrics = generate_lyrics(8)
print(lyrics)