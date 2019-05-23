import time

print """This Brooklyn 99-themed Text Adventure was lovingly created as a way to practice Python, have some fun writing, and pay homage to an amazing show. In this choose your own adventure-meets-madlibs game, you'll fill in words and make decisions to progress. I you have as much fun running this silly little program as I did writing it!"""
time.sleep(8)

noun_1 = raw_input("To start your adventure, choose a noun: ").lower()
food = raw_input("Cool, good choice. Now choose a food: ").lower()

print """Welcome to the 99! It's your first day. As you step off the elevator and scan the bullpen, you see that you've arrived at a chaotic time. Jake and Charles have arrested a pair of burglars who keep trying to fight one another, Rosa is interviewing a witness whose two young children are playing tag in between the desks, and Sergeant Jeffords is upset because he can't find the papier mache %s that Cagny and  Lacey made him for Father's Day - even though he was sure he put it on his desk right next to his yogurt. As you make your way toward Captain Holt's office, narrowly avoiding tripping over one of Rosa's witness's  kids, you smell something peculiar. You turn your head in the direction of the smell and see a rotting %s on Scully's desk. Without looking, Hitchcock reaches over to take a bite.""" % (noun_1, food)

def stop_hitchcock():
  answer_1 = raw_input("Do you try to stop him? ").lower()

  if answer_1 == "yes" or answer_1 == "y": #Stop Hitchcock = Yes
	print """You dodge the witness's kid, leap over a chair with the prowess of an Olympic hurdler, and grab Hithcock\'s hand just in time to stop him from making a terrible mistake. \"Don\'t eat that!\" you exclaim. \"It\'s definitely gone bad.\" Hitchcock replies \"Are you kiddin\' me? This %s is barely six weeks old!\" He grabs it and takes a bite. Horrified, you quickly return to your previous errand, namely finding Captain Holt.""" % (food)
	time.sleep(8)

	print """As you approach Captain Holt's office you notice Gina has actually put down her phone and is staring at you. \"You have some nice moves,\" she says. \"Not as good as mine, obvi, but the gods of dance do not bless everyone equally. How would you like to be a backup dancer in my one-woman dance extravaganza, OutSTAGEous?\""""

	def dance():
	  answer_2 = raw_input("Do you want to strut your stuff onstage? Behind Gina, of course. ").lower()

	  if answer_2 == "yes" or answer_2 == "y": #Dance = Yes
		print """\"Sure,\" you reply. \"Great,\" Gina says. \"Meet me downstairs in exactly 17 minutes for our first practice.\" You start to protest that you have a conflict - namely, your job - but Gina is already composing a tweet and has forgotten that you're standing there."""
		time.sleep(5)

	  elif answer_2 == "no" or answer_2 == "n": #Dance = No
		print """\"I\'m actually not that much of a dancer,\" you reply. \"Shame,\" Gina says. You open your mouth to ask if she means it\'s a shame or you should be ashamed, but she just says \"SHAME\" louder and picks up her phone."""
		time.sleep(5)

	  else:
		print """Don\'t be shy, tell Gina how you really feel."""
		dance()

	dance()

  elif answer_1 == "no" or answer_1 == "n": #Stop Hitchcock = No
  	print """You decide to mind your own business. It is only your first day, after all. Suddenly, you hear a shout, and you turn just in time to see one of the burglars throw Sergeant Jeffords\'s papier mache %s at the other burglar. You take two quick steps, dive, and intercept it in midair. The burglar is so stunned he freezes in place, allowing Jake the opportunity to take him down. Meanwhile, Charles comes to help you up.""" % (noun_1)
  	time.sleep(8)

  	print """\"That was some catch!\" Charles exclaims. \"These two just can\'t get along, which is a shame, considering how they made such a good team before, with all the burglaries. Say, speaking of teams, Genevieve and I are looking for a third for trivia tomorrow night. My first choice was obviously Jake, but he hates the trivia pressure. I asked Amy, but she already promised her friend Kylie she would be on her team, and Gina - my former lover and current sister - can't be without her phone for more than fourteen seconds. Would you want to be on our team?\""""
  	time.sleep(8)

  	def trivia():
  		answer_3 = raw_input("Do you think you have what it takes to be on Boyle\'s trivia team? ").lower()

  		if answer_3 == "yes" or answer_3 == "y": #Trivia = Yes
  			print """It seems like a good idea to get to know your coworkers, so you agree. Boyle is psyched! \"Hear that, Jake? We\'re finally going to have a threesome at trivia!\" Jake replies, \"That\'s great, buddy. You may want to think of another way to say it when you tell Genevieve, though.\""""
  			time.sleep(5)

  		elif answer_3 == "no" or answer_3 == "n": #Trivia = No
  			print """You thank Charles for the offer, but tell him you have plans tomorrow night. \"Aw, darn!\" he says. \"What about next Tuesday?\" Before you have to think up another excuse to let Boyle down easy, one of the unruly children falls and scrapes its knee, prompting Charles's paternal instincts to kick in, and he goes to comfort the bawling little rugrat."""
  			time.sleep(5)

  		else:
  			print """You can't leave Boyle hanging!"""
  			trivia()

  	trivia()				

  else:
  	print """You gotta make a call, detective."""
  	stop_hitchcock()
  	
stop_hitchcock()

clothing = raw_input("It's time to choose more things to continue your adventure. Choose an article of clothing: ").lower()
job = raw_input("Pick a job: ")
kitchen = raw_input("Pick a kitchen utensil: ")
celebrity = raw_input("Choose a celebrity, too: ")

print """At that moment, Captain Holt emerges from his office wearing a %s bearing a picture of his dog, Cheddar. When he sees you he says, \"Ah, good, you made it. Please forgive my unprofessional attire. It has been a rather unusual morning.\" After you assure Captain Holt that you understand, he gives you your first assignment: there was a robbery at a bar called The %s\'s %s during a %s look-alike contest and the prize money was stolen. You and Detective Peralta are to go to down to The %s\'s %s, interview witnesses, and get to the bottom of the missing money.""" % (clothing, job, kitchen, celebrity, job, kitchen)
time.sleep(8)

money = raw_input("While you're on the way to the bar, you have some time to choose more things. Pick a number: ")
noun_2 = raw_input("Now pick an object you can see right now: ").lower()
body_part = raw_input("Finally, choose a body part: ").lower()

print """You arrive at The %s\'s %s and start interviewing members of the staff that were working during the %s look-alike contest. When you compare notes with Jake, you find that several of the staff members mentioned a nervous-looking man with a tattoo of a %s on his %s lurking around near the back of the bar where the money was.""" % (job, kitchen, celebrity, noun_2, body_part)
time.sleep(5)

print """One of the bar tenders approaches and admits he knows the guy with the %s tattoo. The guy is a giggle pig dealer the bar tender used to buy from. The bar tender swears he doesn\'t do that stuff anymore, but the dealer kept trying to convince him. He seemed like he really needed to make a sale, like he needed money. The bar tender told him to get lost, and he did - taking the $%s in prize money with him, no doubt about it. The bar tender tells you where you can find the suspect, and off you go.""" % (noun_2, money)
time.sleep(5)

print """You spot the suspect on the corner. Jake turns to you and says, \"This is your show, how do you want to play it? Confront him and see if he breaks, or play it cool and pretend we're looking to score?\""""

def suspect():
	answer_4 = raw_input("What's it gonna be? Contfront him or play it cool? ").lower()

	if answer_4 == "confront" or answer_4 == "confront him" or answer_4 == "confront suspect" or answer_4 == "confront the suspect" or answer_4 == 1: #Suspect = confront
		print """You tell Jake you want to be direct and confront the suspect. You approach and Jake says \"NYPD, we'd like to ask you a few questions.\" The suspect admits to being at the bar, but denies stealing any money. You're starting to think this just might be a dead end when suddenly a packet of giggle pig falls out of the suspect's pocket. He bolts, with you and Jake on his heels."""
		time.sleep(5)

		print """The suspect runs across the street, narrowly avoiding getting hit by a bus. The bus moves just in time for you to see the suspect disappear into an abandoned building. When you get inside, there is a flight of stairs leading up and down. You and Jake will have to split up."""

		def stairs():
			answer_5 = raw_input("Which way are you going, up or down?").lower()

			if answer_5 == "up" or answer_5 == "upstairs" or answer_5 == 1: #Stairs = Up
				print """You run up the stairs. You round the corner in the stairwell just in time to see the door to the third floor close. You draw your weapon and step through carefully. The suspect is attempting to climb out the window. You command him to freeze, and raises his hands, defeated. \"Alright, you got me,\" he says. \"So I indulge in some giggle pig from time to time, that don\'t make me a thief!\" You say, \"You\'re right, stealing the prize money from a %s look-alike contest makes you a thief.\" You call Jake on your radio and tell him you apprehended the suspect."""
				time.sleep(8)

				print """When Jake arrives, you search the suspect and find more giggle pig, as well as a hundred-dollar bill in the suspect\'s wallet with a serial number that matches the missing prize money. The case is closed - or is it? The suspect continues to insist that he\'s innocent. Jake doesn\'t believe him, but in your gut, you do. You ask the suspect if he sold giggle pig to anyone at the bar that night. At first, he\'s reluctant to snitch on his customers, but once you make him understand the seriousness of his predicament, he admits that he did in fact sell some giggle pig to the bartender. Once the suspect has been delivered to the precinct, you and Jake decide it\'s time to have another chat with the bartender."""
				time.sleep(8)

			elif answer_5 == "down" or answer_5 == "downstairs" or answer_5 == 2:
				print """You run down the stairs. You find yourself in a dark basement filled with old furniture. It's cold and smells slightly moldy. You draw your weapon and command the suspect to come out with his hands up. As your eyes adjust you see a shadow move off in the corner. You approach slowly. You kick a broken shelf aside with one foot and there's the suspect, cowering with his arms over his head. \"Please, don\'t shoot! I\'ll tell you everything! I don\'t know who stole your money, but I can tell you where I get the drugs, and who buys it! I sold some to the bartender at the %s\'s %s just last night!\"""" % (job, kitchen)
				time.sleep(8)

				print """You stop in your tracks as the pieces begin to fit together. You ask the suspect if he has the money on him, and he throws you his wallet. The serial numbers on the bills are consistent with the stolen prize money. You call Jake on your radio and tell him you have the suspect, and that once you book him, you\'ll have another stop to make."""
				time.sleep(8)

			else:
				print """Quick, he's getting away! Up or down?"""
				stairs()

		stairs()		

	elif answer_4 == "play it cool" or answer_4 == "2" or answer_4 == 2 or answer_4 == "play" or answer_4 == "cool": #Suspect = play it cool
		print """You tell Jake you want to play it cool. Jake tells you his undercover identity is Max Archer, and he turned to drugs to cope with his rough childhood, raised by a single mother after his father left, and man this is getting way too real okay what\'s your name?"""

		identity = raw_input("What's your undercover name? ")

		print """You get out of the car and casually approach the suspect. Jake gives him a nod and says, \"Hey, my name is Max Archer and this is my buddy %s, and we\'re hoping you could help us out. We heard you might know where to find some giggle pig.\" The suspect turns and bolts. \"We got a rabbit!\" Jake exclaims, and you chase after him. He runs into an alley and you hear a door slam. When you round the corner you see there are two doors, one on the right and one on the left. You and Jake will have to split up.""" % (identity)

		def doors():
			answer_6 = raw_input("Which door are you going through, left or right? ").lower()

			if answer_6 == "left" or answer_6 == "l": #Door = Left
				print """You go left and Jake goes right. You find yourself in the kitchen of a Chinese restaurant. You flash your badge at the bewildered chefs and ask if they saw a man just run through. One of them points, and you hear a crash. You run through the kitchen and see that the suspect has collided with a waitress and is on the floor. You shout, \"NYPD, don\'t move!\" The suspect looks up in surprise and relief. He says, \"NYPD? I thought you were trying to kill me!\" You ask what he means, and he tells you that he\'s a process server who just started working for the debt collection agency down the block. The night before, he served a bartender at the %s\'s %s and the man made threats.""" % (job, kitchen)
				time.sleep(8)

				print """You call Jake on the radio and tell him what the man with the %s tattoo said. You reach the same conclusion: the bartender at the %s\'s %s definitely stole the money.""" % (noun_2, job, kitchen)
				time.sleep(5)

			elif answer_6 == "right" or answer_6 == "r": #Door = Right
				print """You go right and Jake goes left. You find yourself in a stairwell. You don't hear footsteps, so if the suspect came this way he must've only gone up one floor. You run up the stairs and emerge in a hallway lined with apartment doors. The suspect is at the end of the hall, and you hear a ding - the elevator! You radio Jake to cover the front door, then you run back into the stairwell, down the stairs, and around to the front of the building. Jake has the perp on the ground."""
				time.sleep(8)

				print """\"I swear, I didn\'t steal any money!\" the suspect shouts. You say, \"Multiple witnesses saw you at the %s\'s %s last night. Do you deny it?\" The suspect says, \"I was there, but I didn\'t steal any money. I was there to talk to my sponsee - he\'s a bartender there. I heard he was using again, and I was trying to help. He told me if I didn\'t leave him alone he\'d send his friends after me. That\'s why I ran when I thought you asked about giggle pig.\" """ % (job, kitchen)
				time.sleep(8)

				print """You and Jake share a look as the realization dawns on you that the bartender at the %s\'s %s stole the money.""" % (job, kitchen, noun_2)
				time.sleep(3)

			else:
				print """He's getting away! Quick, pick a door!"""
				doors()

		doors()			

	else:
		print """You have to make a call, detective."""
		suspect()

suspect()

print """You and Jake speed back to the bar. On the way, choose some more things!"""

brand = raw_input("Choose a high-end brand: ")
bottle = raw_input("Choose a type of alcohol: ")

print """You pull up in front of the %s\'s %s and see a brand new %s motorcycle parked in the front. The bartender walks out the front door with a helmet under his arm. When he sees your car he turns and runs back inside. Jake laments, \"Why do they always run!?\" as you jump out of the car and give chase. Jake covers the back while you run through the front. The bartender gets desperate! He uses his helmet to smash through a window and is about to get away. You grab a bottle of %s from behind the bar and throw it. It catches the bartender in the back of the knee and he topples.""" % (job, kitchen, brand, bottle)
time.sleep(8)

print """\"Bingpot!\" you whisper, then you move in to read the perp his rights. Jake emerges from the back and declares your takedown \"Noice!\" In fact, you might even get an \"Oh damn\" when you tell the story back at the precinct!"""
time.sleep(5)

print """Not bad for your first day at the 99, new guy! Keep up the good work!"""

