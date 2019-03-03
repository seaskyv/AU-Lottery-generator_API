import re
import random
import time
import math
import sys
import logging

class OZLotto:
	def __init__(self,data,number,system):
		self.data = data
		self.number = number
		self.system= system
	'''def loadingOZData(self):
		print "Loaded history data.\n";
		f = open(self.data,'rb')
		reader = csv.reader(f)	def __init__(self,data,number):
		R = {}
		for row in reader:
			if not re.match('.*Format.*',row[0]):
				#print row
				#print row[1]
				R[row[1]] = {}
				R[row[1]]['number'] = []
				for k in range(2,9):
					#if re.match('20051018',row[1]):
					R[row[1]]['number'].append(int(row[k]))

		#print R['20051018']
		f.close()
		return(R)
	def analyzeData(self,R):
		print "Analyzing history date...\n";
		for year in R:
			R[year]['numberString'] = ''
			R[year]['number'].sort()
			for n in R[year]['number']:
				R[year]['numberString'] = R[year]['numberString'] + "," + str(n)
			R[year]['numberString'] = R[year]['numberString'] + ","
		#print R['20051018']
		return R'''

	def Generator(self):
		#R = self.loadingOZData()
		#R = self.analyzeData(R)
		#print("run callGames OZLotto G")
		logging.info("Generating OZLotto numbers ...")
		logging.debug("Generating " + str(self.system) + " system OZLotto " + str(self.number) + " games...")
		result=[]
		for i in range(0,int(self.number)):
			#while True:
				#print "set " + str(i) + " numbers are : "
			#mySeed = self.data + int(time.time())
			mySeed = self.data +  random.randrange(sys.maxsize)
			#a = long(_hexlify(_urandom(2500)), 16)
			#a = long(_hexlify(_urandom(2500)), 16)
			random.seed(mySeed)
			nums = random.sample(range(1,46),self.system)
			tempString = ''
			nums.sort()
			for k in nums:
				tempString = tempString + "," + str(k)
			tempString = tempString + ","
			tempString=re.sub(r'^,','',tempString)
			tempString=re.sub(r',$','',tempString)
			#print (tempString)
			result.append({'numbers': tempString})


			'''for year in R:
				if R[year]['numberString'] == tempString:
					print "this number appeared on " + year
			print nums
			break'''
			i +=1
		logging.debug(result)
		return result

class Powerball:
	def __init__(self,data,number,system):
		self.data = data
		self.number = number
		self.system= system
	
	'''def loadingOZData(self):
		f = open(self.data,'rb')
		reader = csv.reader(f)
		print ("Loaded history data.\n");
		R = {}
		for row in reader:
			if not re.match('.*Format.*',row[0]):
				#print row
				#print row[1]
				R[row[1]] = {}
				R[row[1]]['number'] = []
				R[row[1]]['powerball'] = 0
				R[row[1]]['system'] = 0
				if row[7] == '-':
					R[row[1]]['system'] = 5
					for k in range(2,6):
						R[row[1]]['number'].append(int(row[k]))

				else:
					R[row[1]]['system'] = 6
					for k in range(2,7):
						R[row[1]]['number'].append(int(row[k]))

		f.close()
		return(R)

	def analyzeData(self,R):
		print ("Analyzing history date...\n");
		for year in R:
			R[year]['numberString'] = ''
			R[year]['number'].sort()
			for n in R[year]['number']:
				R[year]['numberString'] = R[year]['numberString'] + "," + str(n)
			R[year]['numberString'] = R[year]['numberString'] + ","
		#print R['20051018']
		return R'''

	def Generator(self):
		#R = self.loadingOZData()
		#R = self.analyzeData(R)
		#print("run callGames Powerball G")
		logging.info("Generating Powerball numbers ...")
		logging.debug("Generating " + str(self.system) + " system Powerball " + str(self.number) + " games...")
		result=[]
		for i in range(0,int(self.number)):
			#while True:
			#print ("set " + str(i) + " numbers are : ")
			mySeed = self.data +  random.randrange(sys.maxsize)
			#a = long(_hexlify(_urandom(2500)), 16)
			#a = long(_hexlify(_urandom(2500)), 16)
			random.seed(mySeed)
			nums = random.sample(range(1,36),self.system)
			tempString = ''
			nums.sort()
			for k in nums:
				tempString = tempString + "," + str(k)
			tempString = tempString + ","
			#print tempString
			tempString=re.sub(r'^,','',tempString)
			tempString=re.sub(r',$','',tempString)
			#print (tempString)
			'''for year in R:
				if R[year]['numberString'] == tempString:
					print ("this number appeared on " + year)
				elif re.match(R[year]['numberString'],tempString):
					(print "this number appeared on " + year)'''

			pb = random.randint(1,20)
			result.append({'numbers': tempString,'powerball':pb})

			#print (nums)  
			#print ("PB : " + str(pb))
			#break
			i +=1
		logging.debug(result)
		return result
	

class Lotto:
	def __init__(self,data,number,system):
		self.data = data
		self.number = number
		self.system= system
	
	'''def loadingOZData(self):
		f = open(self.data,'rb')
		reader = csv.reader(f)
		print "Loaded history data.\n";
		R = {}
		for row in reader:
			if not re.match('.*Format.*',row[0]):
				#print row
				#print row[1]
				R[row[1]] = {}
				R[row[1]]['number'] = []
				for k in range(2,8):
					#if re.match('20051018',row[1]):
					R[row[1]]['number'].append(int(row[k]))

		#print R['20051018']
		f.close()
		return(R)
	def analyzeData(self,R):
		print "Analyzing history date...\n";
		for year in R:
			R[year]['numberString'] = ''
			R[year]['number'].sort()
			for n in R[year]['number']:
				R[year]['numberString'] = R[year]['numberString'] + "," + str(n)
			R[year]['numberString'] = R[year]['numberString'] + ","
		#print R['20051018']
		return R'''

	def Generator(self):
		#R = self.loadingOZData()
		#R = self.analyzeData(R)
		#print ("Generating  Lotto numbers ...\n")
		logging.info("Generating Lotto numbers ...")
		logging.debug("Generating " + str(self.system) + " system Lotto" + str(self.number) + " games...")
		result=[]
		for i in range(0,int(self.number)):
			#while True:
			print ("set " + str(i) + " numbers are : ")
			mySeed = self.data +  random.randrange(sys.maxsize)
			#a = long(_hexlify(_urandom(2500)), 16)
			#a = long(_hexlify(_urandom(2500)), 16)
			random.seed(mySeed)
			nums = random.sample(range(1,36),self.system)
			tempString = ''
			nums.sort()
			for k in nums:
				tempString = tempString + "," + str(k)
			tempString = tempString + ","
			tempString=re.sub(r'^,','',tempString)
			tempString=re.sub(r',$','',tempString)
			#print (tempString)
			result.append({'numbers': tempString})
			#print tempString


			'''for year in R:
				if R[year]['numberString'] == tempString:
					print "this number appeared on " + year
			print nums
			break'''
						
			i +=1
		logging.debug(result)
		return(result)

class PlayGame:
	def __init__(self,game,magic,num,system):
		self.game = game
		self.magic = magic
		self.num = num
		self.system = system
		self.result = []
	def callGames(self):
		#print("run callGames")
		# URL request should be case sensitive !
		# if self.game.lower() == "lotto" :
		if self.game == "lotto" :
			#print("run callGames Lott")
			L = Lotto(self.magic,self.num,self.system)
			result = L.Generator()
			return(result)
		elif self.game == "OZLotto":
			#print("run callGames OZLott")
			OZ = OZLotto(self.magic,self.num,self.system)
			result = OZ.Generator()
			#print(result)
			return(result)
		elif self.game == "Powerball":
			#print("run callGames Powerball")
			PB = Powerball(self.magic,self.num,self.system)
			result = PB.Generator()
			return(result)
		else :
			logging.error("Game type not defined")
    
