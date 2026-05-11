'''
✅ TASK 4: Basic Chatbot

Goal:
Create a simple rule-based chatbot.

Concepts Used:
- if-elif
- functions
- loops
- input/output
'''

print("Simple Chatbot")

#Create Function for chatbot replies
def chatbot():

    while True:#use while loop

        # Take input from user
        user = input("\nYou :- ").lower()

        # Conditions
        if user == "hello":
            print("Bot :- Hi!")

        elif user == "how are you":
            print("Bot :- I am fine, thanks!")

        elif user == "bye":
            print("Bot :- Goodbye!")
            break

        else:
            print("Bot :- I don't understand.")

# Call The ChatBoat function
chatbot()
