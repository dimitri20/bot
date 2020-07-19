
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("firebaseKEY.json")
firebase_admin.initialize_app(cred, {

		'databaseURL' : 'https://bot-v1-6a6d4.firebaseio.com/sw/qJg9BHMSF9fzB6zRkb3k'

	})



class createPath:
	def __init__(self, path=''):
		self.ref = db.reference(path)

	def teach(self, sentence, keys):
		ref = self.ref
		data = {
			'sentence': sentence,
			'keys': keys
		}
		ref.push(data)
		print(a.key)
		


#cr = createPath()
#cr.teach(sentence='როგორი ამინდია ხვალ', keys=['ამინდ', 'ხვალ'])

text = "როგორი ამინდია ხვალ"
text = text.split()
for item in text:
	item.


"""
ref.set({

		'Employee': {
			'emp1':{
				'name':['dito', 'me', 'you', 'it'],
				'lname':'gulue',
				'age':2
			},

			'emp2':{
				'name':'dito1',
				'lname':'gulue1',
				'age':21
			},

			'emp3':{
				
				'lname':'gulue25584684684646855'
				
			}
		}

	})
"""

