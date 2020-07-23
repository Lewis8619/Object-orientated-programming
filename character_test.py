
from character import Enemy

derek = Enemy("Derek", "A smelly zombie!")
derek.describe()

# Add some dialogue for Derek for when he is spoken to
derek.set_conversation("What's up dude?")
derek.talk() # Trigger a conversation with Derek

# Set a weakness
derek.set_weakness("penicilin")

# Fight with Derek
print("What is your weapon of choice?")
weapon = input()
derek.fight(weapon)
