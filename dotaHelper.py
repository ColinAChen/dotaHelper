import dota2api
import cv2

api = dota2api.Initialise("620766337952AEED4D6ED6A3DED155D1")
match = api.get_match_details(match_id = 4028008613)

#print (match['players'][9]['ability_upgrades'])

'''
for hero in heroes['heroes']:
	print (hero['localized_name'] , hero['id'])
'''
def getVictor(match):
	if(match['radiant_win']):
		return 'Radiant'
	else:
		return 'Dire'

def secondsToMinutes(minutes,seconds):
	if (seconds > 60):
		minutes += 1
		secondsToMinutes(minutes,seconds-60)
	else:
		return (minutes,seconds)


def parseInputHero(hero):
	hero = hero.lower()
	for char in hero:
		if char == '-':
			hero.remove(char)
	return hero


def itemName(itemID):
	try:
		itemID = int(itemID)
	except:
		print ('Item ID must be an integer')
		return 0
	items = api.get_game_items()['items']
	#print (items)
	for item in items:
		#print (item['id'])
		if (itemID == item['id']):
			#print('Found match!')
			return item['localized_name']

def matchHero(myHero,myHeroID):
	myHero = parseInputHero(myHero)


	heroIds = api.get_heroes() #dictionaty
	
	for heroDict in heroIds['heroes']:
		if heroDict['localized_name'] == myHero or heroDict['hero_id'] == myHeroID:
			return heroDict


def heroNameToID(heroName):
	heroIds = api.get_heroes()

	for heroDict in heroIds['heroes']:
		if heroDict['localized_name'].lower().find( heroName.lower()) != -1:
			return heroDict['id']
	return 0

def swapHeroInfo(heroInfo):
	heroes = api.get_heroes()
	try:
		heroInfo = int(heroInfo)
		
		for hero in heroes['heroes']:
			if hero['id'] == heroInfo:
				return hero['localized_name']
	except:
		
		return heroNameToID(heroInfo)

#returns a list with the radiant heroes at index 0 and dire heroes at index 1
def assignHeroes(match):
	heroesOnTeams = [] #radiant,dire
	tempRadiant = []
	heroes = match['players']
	for hero in heroes:
		tempRadiant.append(hero)
		heroes.remove(hero)
	heroesOnTeams.append(tempRadiant)
	heroesOnTeams.append(heroes)
	
	

	return heroesOnTeams
	
#print (assignHeroes(match)[0][0])
def goldDifference(match):
	goldDiff = 0
	return 0

def imFeelingLucky(myHero):
	
	matchNotFound = True
	sampleSize = 0
	try:
		myhero = int(myHero)
	except:
		print ('Changing name to ID')

		myHero = heroNameToID(myHero)
	print ('Finding a guide for:', swapHeroInfo(myHero), myHero)
	if myHero < 1:
		print ('Hero not found. HeroID must be greater than 0')
		return 0
	while (matchNotFound and sampleSize < 4300):

		sampleSize += 100
		print ('Current sample size:',sampleSize)
		sample = api.get_match_history_by_seq_num(sampleSize)

		for sampleMatch in sample['matches']: #iterate through each match
			#print (sampleMatch['game_mode'])
			#if (sampleMatch['game_mode'] == 1): #only check if the type of match is the same
			print ('\n\n\n\n')	
			for player in sampleMatch['players']:
				
				print (swapHeroInfo( player['hero_id']))
				if player['hero_id'] == myHero: #find a matching hero
					print ('found a hero match')
					
					if (sampleMatch['radiant_win'] and player['player_slot'] < 5):
						print ('WIN')
						matchNotFound = False
						return sampleMatch
						
					elif (player['player_slot'] > 4):
						print ('WIN')
						matchNotFound = False
						return sampleMatch
							
	
	return 

#assume the match has found a matching hero
#returns a score out of 100.0
#a perfectly matched game (all ten heroes match with the same game mode) is 100.0
'''
def calcSimilarityScore(myHeroID,myMatch,foundMatch): #returns a score based on how good of a fit the old match is to the new one
	
	finalScore = 0

	myMatchTeams = assignHeroes(myMatch)
	foundMatchTeams = assignHeroes(foundMatch)

	myTeam = myMatch['players']['hero_id']
	myEnemyTeam = 
	if (myMatch['game_mode'] == foundMatch['game_mode']):
		finalScore += 20
	for 

	return finalScore
'''
#print (api.get_heroes()['heroes'][0]['localized_name'])


'''
myHero uses unique hero ids because not all names are there

myGameMode Values
Value	Description
0	Unknown
1	All Pick
2	Captain’s Mode
3	Random Draft
4	Single Draft
5	All Random
6	Intro
7	Diretide
8	Reverse Captain’s Mode
9	The Greeviling
10	Tutorial
11	Mid Only
12	Least Played
13	New Player Pool
14	Compendium Matchmaking
15	Custom
16	Captains Draft
17	Balanced Draft
18	Ability Draft
19	Event (?)
20	All Random Death Match
21	Solo Mid 1 vs 1
22	Ranked All Pick
'''
def getSample(number,MMR,myHero,myGameMode): #returns sample of matches that contain the same hero_id as parameter
	matchesSample = []
	sample = api.get_match_history_by_seq_num(number)
	for sampleMatch in sample['matches']: #iterate through each match
		#if (sampleMatch['radiant_win']):
			#for player in sampleMatch['players']
		if (sampleMatch['game_mode'] == myGameMode): #only check if the type of match is the same
			for player in sampleMatch['players']:
				

				if player['hero_id'] == myHero: #find a matching hero
					print ('found a hero match')
					matchesSample.append(sampleMatch)
					if (sampleMatch['radiant_win'] and player['player_slot'] < 5):
						print ('WIN')
					elif (player['player_slot'] > 4):
						print ('WIN')
			
	return matchesSample   
def listener():
	userInput = input('Wuss poppin: ')
	while(userInput.lower() != 'done'):
		if (userInput.find('lucky') != -1):

			heroIn = input('What is your hero? ')

			print (parseMatch(imFeelingLucky(heroIn)))
		elif (userInput.lower().find('lookup') != -1):
			heroIn = input('Enter a hero ID or name: ')
			print (swapHeroInfo(heroIn))

		elif (userInput.find('ID') != -1):

			heroIn = input('what is your hero? ')
			print (heroNameToID(heroIn))

		elif (userInput.lower().find('item') != -1):
			itemIn = input ('Enter an item ID: ')
			print (itemName(itemIn))

		userInput = input ('What else is poppin? ')

def parseMatch(match):
	if match == 0:
		return 0
	if (match['radiant_win']):
		print ('Radiant win')
	else:
		print ('Dire Win')
	print ('Game mode:', match['game_mode'])
	print ('Duration:', match['duration'])
	print ('Number of human players', match['human_players'])

	teams = assignHeroes(match)
	for team in teams:

		for player in team:
			#print (player)

			print (swapHeroInfo( player['hero_id']))
			#print (player[])
			print ('Level',player['level'])
			print ('Gold', player['gold'])
			print ('Inventory:')
			for item in range(0,6):
				key = 'item_' + str(item)
				print (itemName(player[key]))
			print ('\n')
			if (player['deaths'] > 0):
				print ('Kill/Death ratio', (player['kills']/player['deaths']),'(',player['kills'],player['deaths'],')')
			else:
				print ('kils / deaths',player['kills'],'/',player['deaths'])
			print ('Level Order')
			for level in player['ability_upgrades']:
				print (level)
			print ('\n')
		print ('\n')
		print ('\n')
		print ('\n')

	return 

print (parseMatch(match))
#listener()
'''
def findSingleMatch(match,myMatch):

	while(#score is not met):
		#search 100 matches
	#return match that meets criteria
'''

#print (getSample(100,0))
