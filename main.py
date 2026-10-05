name = input("What is your name? ").strip()

if name == "":
    name = "Developer"

goal = input("Why are you learning python? ").strip()

if goal == "":
    goal = "Explore what I can build with Python."

    
print(f"Hi, I'm {name}!")
print(f"My learning goal: {goal}")