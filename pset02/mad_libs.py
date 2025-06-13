import random
templates = [
    {
        "text": "The :color :flower looks :adjective outside.",
        "author": "Lucy Dacus"
    },
    {
        "text": ":singer is :verb(ing) at the :place on :day",
        "author": "Pheobe Bridgers"
    },
    {
        "text": "Even the :color :animal loves a :adjective :noun",
        "author": "Julien Baker"
    },
    {
        "text": ":person goes to the :adjective :place with friends.",
        "author": "Lorde"
    },
    {
        "text": "The :adjective :person :verb(ed) over a :color :object",
        "author": "Dora Jar"
    },
    {
        "text": ":verb like a :adjective :animal in the :place",
        "author": "Mitski"
    },
    {
        "text": ":person and :person are :adjective best friends at the :event",
        "author": "Gracie Abrams"
    },
    {
        "text": ":person :verb(s) under the :adjective sky.",
        "author": "Imogen Heap"
    },
    {
        "text": "On :day :person is :verb(ing) in :adjective :city",
        "author": "SZA"
    },
    {
        "text": ":pronoun waits for :person to :verb at the :event", 
        "author": "Ariana Grande"
    

    }
]

yes_answers = {
    "yes", "si", "oui", "sure", "yeah", "yep"
}


def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if 1 <= len(user_input) <= 30:
            return user_input
        else:
            print("Input must be between 1 and 30 characters long. Please try again.")


def fill_template(template):
    filled_template = template["text"]
    placeholders = [word for word in filled_template.split() if word.startswith(':')]
    # this means give me every word from the filled template and starts with a colon
    
    for placeholder in placeholders:
        description = placeholder[1:]  # Remove the colon
        user_input = get_user_input(f"Please enter a {description}: ")
        filled_template = filled_template.replace(placeholder, user_input, 1)
    
    print("\n" + filled_template)
    print(f"\nAuthor: {template['author']}\n")


while True:
    template = random.choice(templates)
    fill_template(template)
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again not in yes_answers:
        print("Thanks for playing!")
        break

