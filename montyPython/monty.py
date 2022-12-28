import random
jokes = open("montyPython/jokeList.txt", "r")
joke = jokes.readlines()

jokeList = []
jokeIDX = 0
for j in joke:
    jokeList.append(j.strip())
    jokeIDX+=1
jokeNum = random.randint(0,jokeIDX)
if jokeNum < 1:
    jokeNum = 1
elif jokeNum > jokeIDX:
    jokeNum = jokeIDX
randomJoke = jokeList[jokeNum]
print(randomJoke)