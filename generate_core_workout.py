import argparse
import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument("number", help="Enter the number of exercises you would like to do here.", type=int)
arg = parser.parse_args()

EXERCISES = ["Elbow Plank",
"Elbow Side Plank",
"High Plank",
"High Side Plank",
"Back Plank",
"High Plank with Arm Extensions",
"Elbow Plank with Arm Extensions",
"High Plank with Opposite Arm/Leg Extensions",
"Elbow Plan with Opposite Arm/Leg Extensions",
"Elbow Side Plank with Knee Drives",
"High Side Plank with Knee Drives",
"Elbow Side Plank with Top Leg Lifts",
"High Side Plank with Top Leg Lifts",
"Elbow Side Plank with Internal Rotation",
"High Side Plank with Internal Rotation",
"Pushups",
"Wide Pushups",
"Triangle Pushups",
"Spiderman Pushups",
"V Ups",
"Russian Twists",
"Toe Taps (Penguin Slides)",
"Boats",
"Accordions",
"Supermans",
"Leg Lifts",
"Flutters",
"Scissors",
"Opposite Elbow to Knee Hold, other leg extended",
"Mountain Climbers",
"Swiss Ball Pikes",
"Swiss Ball Side Tucks",
"Swiss Ball Single Leg Drives",
"Swiss Ball Stir the Pot",
"Swiss Ball Glute Bridge Leg Extensions (shoulders on ball)",
"Swiss Ball Hip Extensions",
"Swiss Ball Rollouts",
"Medicine Ball Pushups",
"Fire Hydrants",
"Donkey Kicks",
"Side Lying Hip Abbduction",
"Side Lying Hip Adduction",
"Bird Dogs"
]

if arg.number > len(EXERCISES):
    print "Too many exercises selected. We'll go with " + str(len(EXERCISES)) + " instead."
    arg.number = len(EXERCISES)

chosen = np.random.choice(EXERCISES, arg.number, replace = False)

print "\nYour workout:"
for c in chosen:
    print "\t" + c
print "\n"
