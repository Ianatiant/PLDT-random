import random
import string

def generate_random_text(text):
    available_characters = list(string.ascii_letters + string.digits)  
    random_text = ''
    for char in text:
        if char == 'x':
            if not available_characters:
                raise ValueError("Not enough unique characters to replace all 'x'")
            chosen_char = random.choice(available_characters)
            random_text += chosen_char
            available_characters.remove(chosen_char) 
        else:
            random_text += char
    return random_text

text = "PLDTHOMEFIBRxxxxx"


random_words = []
for _ in range(10000000):
    randomized_text = generate_random_text(text)
    random_words.append(randomized_text)


output_file_path = "(path to file)"
with open(output_file_path, "w") as file:
    for word in random_words:
        file.write(word + "\n")

print(f"Random words saved to {output_file_path}")
