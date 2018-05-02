
#A SIMPLE GAME
class Football():

	class_name=''
	desc=''
	objects={}

	def __init__(self, name):
		self.name = name
		Football.objects[self.class_name]=self

	def get_desc(self):
		print(self.class_name + '\n' + self.desc)

class Striker(Football):
	class_name = 'striker'
	desc='scores goals'

class Defender(Football):
	class_name='defender'
	desc='stops striker'

class Ball(Football):
	def __init__(self, name):
		self.class_name='ball'
		self._desc='hollow spherical inflated with air'
		self.status=0
		super().__init__(name)

	@property
	def desc(self): #THE PROPERTY RETURNS ITSELF
		if self.status==0:
			self._desc='hollow spherical inflated with air'
		elif self.status==1:
			self._desc = 'you beat one defender!'
		elif self.status==2:
			self._desc = 'you beat another defender!'
		elif self.status==3:
			self._desc = 'now you beat the goalkeeper!'
		elif self.status>3:
			self._desc = 'IT\'S IN THE BACK OF THE NET!!!!!! GOALLLLLLLLLLLLLLLLLLLL!!!!!!!!!!!!!!!'
		return self._desc

	@desc.setter #THE SETTER TELLS YOU THE VALUE OF THE PROPERTY, 
	#OR THE VALUE OF SOMETHING THAT DETERMINES THE VALUE OF THE PROPERTY
	def desc(self, value):
		self.status = value
		


striker1 = Striker('yekini')
defender1=Defender('uche')
ball01=Ball('addidas')



i = 0

def get_input():

	global i

	if i == 0:
		print('Welcome to my football game!' + '\n' + 'Here you enter a command.' + '\n' + 'Command must comprise two words and must begin with a verb.' + '\n' + 'Only 3 verbs currently available: say, kick and examine.' + '\n' + 'Only 3 items can be examined: striker, defender or ball.' + '\n' + 'Only 1 item can be kicked: ball.' + '\n' + 'Thank you!')
	
		command = (input('Your command please!!!!!!!')).split(' ')

		i += 1


	elif i >= 1:
		command = (input('Your command please!:')).split(' ')



	verbword = command[0]
	if verbword in verbdict:
		verb = verbdict[verbword]
	else:
		print('unknown')
		return

	if len(command)>1:
		nounword = command[1]
		verb(nounword)
	else:
		verb('nothing')

def say(noun):
	print('you said {}'.format(noun))

def examine(noun):
	if noun in Football.objects:
		Football.objects[noun].get_desc()
	else:
		print('there is no {} here'.format(noun))

def kick(noun):
	if noun in Football.objects:
		item = Football.objects[noun]
		if type(item) == Ball:
			item.status += 1
			if item.status == 1:
				print('you kicked the ball!')
			if 2<= item.status <=3:
				print('you kicked the ball again!')
			elif item.status>3:
				print('YOU\'VE SCORED!!!!!!!!!!!')

		else:
			print('you can\'t kick that')
	else:
		print('you can\'t kick that')

verbdict={'say':say, 'examine':examine, 'kick':kick}

while True:
	get_input()
