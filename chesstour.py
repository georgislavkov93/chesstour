import random

class Player:
	gamesPlayed = 0
	points = 0
	wins = 0
	draws = 0
	losses = 0
	def __init__(self,name):
		self.name = name

	@staticmethod
	def game(a,b):
		print("%s (white pieces) is playing against %s (black pieces). The result is: " %(a.name,b.name))
		result = input()
		if result == '1':
			a.points = a.points + 1
			a.wins = a.wins + 1
			b.losses = b.losses + 1
		elif result == '2':
			b.points = b.points + 1
			b.wins = b.wins + 1
			a.losses = a.losses + 1
		elif result == 'x':
			a.points = a.points + 0.5
			b.points = b.points + 0.5
			a.draws = a.draws + 1
			b.draws = b.draws + 1
		a.gamesPlayed = a.gamesPlayed + 1
		b.gamesPlayed = b.gamesPlayed + 1


numOfPlayers = int(input("How many players will participate? "))
allPlayers = [Player("") for i in range(numOfPlayers)]
rounds = 0
for i in range(numOfPlayers):
	print("Enter name of player %d " %int(i+1))
	tempName = input()
	allPlayers[i].name = tempName
	rounds = rounds + ((numOfPlayers-1) - i)
rounds = rounds * 2#since we have a first leg with the white pieces and the second leg with the black pieces
random.shuffle(allPlayers)

if len(allPlayers) % 2 == 1:
	p1 = Player("Dummy")#if we have an odd number of players we create a Dummy so we can match him against the 'resting' player without counting the game
	allPlayers.append(p1)
n = len(allPlayers)
matches = []
fixtures = []
secLeg = []
for fixture in range(1, n):
	for i in range(int(n/2)):
		matches.append((allPlayers[i], allPlayers[n - 1 - i]))
		secLeg.append((allPlayers[n - 1 - i], allPlayers[i]))
	allPlayers.insert(1, allPlayers.pop())
	fixtures.insert(int(len(fixtures)/2), matches)
	fixtures.append(secLeg)
	matches = []
	secLeg = []

roundCounter = 1
for r1 in fixtures:
	for r2 in r1:
		if r2[0].name != "Dummy" and r2[1].name != "Dummy":
			print("Round %d out of %d" %(roundCounter,rounds))
			Player.game(r2[0],r2[1])
			roundCounter = roundCounter + 1

allPlayers.sort(key=lambda x: x.points, reverse=True)

print("Final result:\nPosition\tName\tWins\tDraws\tLosses\tPoints")
for i in range(numOfPlayers):
	print("%d\t\t%s\t%d\t%d\t%d\t%g" %(i+1,allPlayers[i].name,allPlayers[i].wins,allPlayers[i].draws,allPlayers[i].losses,allPlayers[i].points))

if allPlayers[0].points > allPlayers[1].points:
	print("The winner is %s!" %allPlayers[0].name)
elif allPlayers[0].points == allPlayers[1].points:
	print("There should be a tiebreak between %s and %s to decide the winner." %(allPlayers[0].name,allPlayers[1].name))
input("End of the tournament!")

