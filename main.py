import random

def create_response(user_input):
  responses = [
    "Awesome, I'm glad!",
    "Good to know!",
    "That's pretty cool!",
    "Very interesting!",
    "What a surprise!",
    "Are you sure about that?"
  ]
  return random.choice(responses)

def init_chat():
  quit_button = "X"

  user_input = input("Hi, how's it going?\n\n")

  while user_input != quit_button:
    user_input = input(create_response(user_input) + "\n\n")

if __name__ == "__main__":
  init_chat()