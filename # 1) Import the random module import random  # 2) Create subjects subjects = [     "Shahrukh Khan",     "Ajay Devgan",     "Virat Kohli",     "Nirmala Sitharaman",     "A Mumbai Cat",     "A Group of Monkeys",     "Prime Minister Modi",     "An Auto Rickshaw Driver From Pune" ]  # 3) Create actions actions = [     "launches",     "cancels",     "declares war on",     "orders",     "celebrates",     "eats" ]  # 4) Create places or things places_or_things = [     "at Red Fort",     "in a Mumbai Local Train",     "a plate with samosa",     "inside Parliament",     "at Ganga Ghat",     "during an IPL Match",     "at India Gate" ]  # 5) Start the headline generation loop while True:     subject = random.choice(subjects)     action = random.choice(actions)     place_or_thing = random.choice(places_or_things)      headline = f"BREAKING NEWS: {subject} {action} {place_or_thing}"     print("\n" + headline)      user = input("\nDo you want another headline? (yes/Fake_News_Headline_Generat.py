# 1) Import the random module
import random

# 2) Create subjects
subjects = [
    "Shahrukh Khan",
    "Ajay Devgan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "An Auto Rickshaw Driver From Pune"
]

# 3) Create actions
actions = [
    "launches",
    "cancels",
    "declares war on",
    "orders",
    "celebrates",
    "eats"
]

# 4) Create places or things
places_or_things = [
    "at Red Fort",
    "in a Mumbai Local Train",
    "a plate with samosa",
    "inside Parliament",
    "at Ganga Ghat",
    "during an IPL Match",
    "at India Gate"
]

# 5) Start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user == "no":
        break

# 6) Goodbye message
print("\nThanks for using the Fake News Headline Generator. Have a fun day!")
