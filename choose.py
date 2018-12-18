import random
from random import choise

players = []
fileP = open('players.txt', 'r')
players = fileP.read().splitlines()
teams = []
fileT = open('teams.txt', 'r')
teams = fileT.read()

while len(players) > 0:
playerA = choice(players)
teamA = choice(teams)
teamA.append(playerA)
players.remove(playerA)
teams.remove(teamA)

if players ==[]
break
playerB = choice(players)
teamB = choice(teams)
teamB.append(playerB)
players.remove(playerB)
teams.remove(teamB)
if players ==[]
break
playerC = choice(players)
teamC = choice(teams)
teamC.append(playerC)
players.remove(playerC)
teams.remove(teamC)
if players ==[]
break
playerD = choice(players)
teamD = choice(teams)
teamD.append(playerD)
players.remove(playerD)
teams.remove(teamD)
    print (teamA)
	print (teamB)
	print (teamC)
	print (teamD)
    