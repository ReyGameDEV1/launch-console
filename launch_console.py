name = input("What's your name? ").strip()
if not name:
    name = "Stranger"

print(f"Welcome to {name}'s Launch Console!")

running = True
while running:
    print("\n1) About me")
    print("2) My goals")
    print("3) Fun fact")
    print("4) Exit")
    choice = input("Pick 1-4: ").strip()

    if choice == "1":
        print("I'm a high school student in Houston. I do FRC robotics,")
        print("run a math club, and write for a student math magazine.")
    elif choice == "2":
        print("Short term: ship more projects and get better at Python.")
        print("Long term: research math/CS and eventually teach it.")
    elif choice == "3":
        print("Fun fact: a graph with n nodes can have n^(n-2) spanning trees.")
        print("That's Cayley's formula — 16 for just 4 nodes.")
    elif choice == "4":
        print(f"Goodbye, {name}! Console shutting down.")
        running = False
    else:
        print("Please pick 1, 2, 3, or 4.")