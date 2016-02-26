import json

#-----------------------------------------------------#
#				   	 Information                      #
#-----------------------------------------------------#

# Load all data from file
people = json.load(open('people.json'))	

#-----------------------------------------------------#
#				   	 Functions	                      #
#-----------------------------------------------------#
def request_phone(args):
	if args[0] in people['ID']:
		pos = people['ID'].index(args[0])
		return 'Phone: ' + people['Phone'][pos]
	else:
		return 'No number registerd!'
		
def request_email_by_ID(args):
	if str(args[0]) in people['ID']:
		pos = people['ID'].index(str(args[0]))
		return 'Email: ' + people['email'][pos]
	else:
		return 'There is no such ID'

def request_email_by_name(args1,args2):
	print args1
	print args2
	pos1 = people['F_Name'].index(args1)
	pos2 = people['L_Name'].index(args2)
	if pos1 == pos2:
		return 'Email: ' + people['email'][pos1]
	else:
		return 'No match'

def Find_all_emails_by_dep(args):
	count = people['Dep'].count(str(args[0]))
	length = len(people['Dep'])
	if  count > 0 and count <= length:
		indices = [i for i, x in enumerate(people['Dep']) if x == str(args[0])]
		liste = [people['email'][x] for x in indices ]
		return liste
	else:
		return ['Not a valid department ID']

def login(user):
	if user in people['email']:
		return True
	else:
		return False

def get_online(threads):
	users = [user for user in threads.keys()]
	return '\n'.join(users)