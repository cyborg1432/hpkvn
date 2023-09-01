import random

jokes = ["I'm reading a book on anti-gravity – it's impossible to put down.",
         "Parallel lines have so much in common – it's a shame they'll never meet.",
         "I used to play piano by ear, but now I use my hands.",
         "Why don't scientists trust atoms? Because they make up everything.",
         "I told my wife she was drawing her eyebrows too high. She seemed surprised.",
         "I'm friends with all electricians – we have great current connections.",
         "Want to hear a construction joke? Oh, never mind, I'm still working on that one.",
         "Why don't skeletons fight each other? They don't have the guts.",
         "Did you hear about the claustrophobic astronaut? He just needed a little space.",
         "I used to be a baker, but I couldn't make enough dough."
         ]

random_num = random.randint(0,9)


print(f"today random joke is {random_num} \n ")
print(jokes[random_num])