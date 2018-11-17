import random
import os
from datetime import datetime
def generateRandomness(lowerBound,upperBound):
    random.seed(datetime.now())
    randNumber = random.randint(0,upperBound)
    return randNumber
