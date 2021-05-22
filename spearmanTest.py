import random
from datetime import datetime
from scipy import stats


testData = [
    "Margaret",
    "Will",
    "Abe",
    "Jennifer",
    "Sally",
    "Brock",
    "Liam",
    "Connor",
    "Vanessa",
    "Xray"
]

def genRandomList() -> list:
    shuffledData = random.sample(testData,len(testData))
    return shuffledData

a = genRandomList()
b = genRandomList()
print(a)
print(b)

print(stats.spearmanr(a, b))