# Dec 20, 2019
import random

# Start of random facts
list = [
  "You suck!!!",
  "I'm better than you ;)",
  "Banging your head against a wall for one hour burns 150 calories.",
  "The mitochondria is the powerhouse of the cell",
  "In Switzerland it is illegal to own just one guinea pig.",
  "Pteronophobia is the fear of being tickled by feathers.",
  "Snakes can help predict earthquakes.",
  "A flock of crows is known as a murder.",
  "The oldest “your mom” joke was discovered on a 3,500 year old Babylonian tablet.",
  "So far, two diseases have successfully been eradicated: smallpox and rinderpest.",
  "29th May is officially “Put a Pillow on Your Fridge Day”.",
  "Cherophobia is an irrational fear of fun or happiness.",
  "7% of American adults believe that chocolate milk comes from brown cows.",
  "If you lift a kangaroo’s tail off the ground it can’t hop.",
  "Bananas are curved because they grow towards the sun.",
  "Billy goats urinate on their own heads to smell more attractive to females.",
  "The inventor of the Frisbee was cremated and made into a Frisbee after he died.",
  "During your lifetime, you will produce enough saliva to fill two swimming pools.",
  "If Pinocchio says “My Nose Will Grow Now”, it would cause a paradox.",
  "Polar bears could eat as many as 86 penguins in a single sitting…",
  "King Henry VIII slept with a gigantic axe beside him.",
  "Movie trailers were originally shown after the movie, which is why they were called “trailers”.",
  "An eagle can kill a young deer and fly away with it.",
  "Heart attacks are more likely to happen on a Monday.",
  "Tennis players are not allowed to swear when they are playing in Wimbledon.",
  "In 2017 more people were killed from injuries caused by taking a selfie than by shark attacks.",
  "The top six foods that make your fart are beans, corn, bell peppers, cauliflower, cabbage and milk.",
  "There is a species of spider called the Hobo Spider.",
  "A lion’s roar can be heard from 5 miles away.",
  "Saint Lucia is the only country in the world named after a woman.",
  "A baby spider is called a spiderling.",
  "The United States Navy has started using Xbox controllers for their periscopes.",
  "The following can be read forward and backwards: Do geese see God?",
  "A baby octopus is about the size of a flea when it is born.",
  "A sheep, a duck and a rooster were the first passengers in a hot air balloon.",
  "In Uganda, around 48% of the population is under 15 years of age.",
  "The average male gets bored of a shopping trip after 26 minutes.",
  "In the 16th Century, Arab women could initiate a divorce if their husbands didn’t pour coffee for them.",
  "Recycling one glass jar saves enough energy to watch television for 3 hours.",
  "After the premiere of “16 and Pregnant,” teen pregnancy rates dropped.",
  "Approximately 10-20% of U.S. power outages are caused by squirrels.",
  "Facebook, Instagram and Twitter are all banned in China.",
  "95% of people text things they could never say in person.",
  "Honeybees can recognize human faces.",
  "The Battle of Hastings didn’t take place in Hastings.",
  "While trying to find a cure for AIDS, the Mayo Clinic made glow in the dark cats.",
  "A swarm of 20,000 bees followed a car for two days because their queen was stuck inside.",
  "Nearly 3% of the ice in Antarctic glaciers is penguin urine.",
  "Bob Dylan’s real name is Robert Zimmerman.",
  "A crocodile can’t poke its tongue out.",
  "Sea otters hold hands when they sleep so they don’t drift away from each other.",
  "A small child could swim through the veins of a blue whale.",
  "Bin Laden’s death was announced on 1st May 2011. Hitler’s death was announced on 1st May 1945.",
  "Some cats are actually allergic to humans.",
  "There is a fruit that tastes like chocolate pudding.",
  "Competitive art used to be in the Olympics.",
  "A chef's hat has exactly 100 pleats.",
  "The majority of your brain is fat.",
  "Oranges aren't naturally occurring fruits.",
  "Most wasabi we eat in the U.S. isn't really wasabi.",
  "Amelia Earhart and Eleanor Roosevelt once went on a joyride.",
  "Stop signs used to be yellow.",
  "Green Eggs and Ham started as a bet.",
  "Andy Warhol inspired Louboutins' red soles.",
  "Too much water can kill you.",
  "The hottest temperature ever recorded on Earth was 2 billion degrees kelvin.",
  "The moon is (slowly) slowing the Earth's rotation.",
  "High heels were originally worn by men.",
  "You might be drinking water that is older than the solar system.",
  "Queen Elizabeth II is a trained mechanic.",
  "There was a successful Tinder match in Antarctica in 2014.",
  "Moonshiners used “cow shoes” to disguise their footprints during Prohibition.",
  "It takes 364 licks to get to the center of a Tootsie Pop.",
  "Tree rings get wider during wet years.",
  "The hottest inhabited place in the world is in Ethiopia.",
  "Hot water freezes faster than cold water.",
  "Dolphins have names for one another.",
  "The bowler hat was invented as safety measure.",
  "Sea otters hold hands while they sleep."
]
"""
--- Random fact sources ---
1. https://www.thefactsite.com/top-100-random-funny-facts/
2. https://bestlifeonline.com/random-obscure-facts/
"""
# End of random facts

# Start of clear
clear = "\n" * 100
print(clear)
# End of clear

# Start of game
for val in "code":
# Random number generator start
 from random import randrange, uniform
 number = randrange(1, 100)
# Random number generator end
# Start of Game Code
 Highest = 100
 Answer = randrange(1, 100)
 Name = input("Whats your name? ")
 Guess = input("Hello " + Name.capitalize() + " Guess a number from 0 to %d: " %Highest)
 while (int(Guess)!= Answer):
   if (int(Guess) < Answer):
     print("The answer is higher than what you have answered. Please try again!")
   else:
     print("The answer is lower than what you have answered. Please try again!")
   Guess = input("Guess a number from 0 to %d:" %Highest)
 import click
 print(clear)
# Start of one more feature
 print("Hey " + Name.capitalize() + " Guess What???")
 if click.confirm("Press (Y) To Continue. Or Press (N) If You Are A Loser", default=True):
    print( )
    print(random.choice(list))
    print( )
# End of one more feature
 # End of Game Code
 # End of Game
 # Start of Restart
 import click
 if click.confirm("Play Again? ", default=True):
    print("Restarting...")
    print(clear)
# End of Restart
# Start of End
 else:
  print(clear)
  break
print(clear)
print("DONE")
print("Thanks for playing ;)")
print( )
