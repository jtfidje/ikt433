#-----------------------------------------------------#
#				   	 Information                      #
#-----------------------------------------------------#

dict = {
'ID': ['1','2','3','4','5','6','7'],
'Dep': ['1','2','3','2','1','3','2'],
'F_Name': ['Henrik','Ole','Ali','Mark','Even','Thomas','Thor'],
 'L_Name': ['Waagsnes','Olsen','Johansen','Hansen', 'Ellefsen', 'Natten', 'Fidje'],
 'Phone': ['97421128','47098754','97656786','99443322','65676567','57569273','23232323'],
 'email': ['henrik.waagsnes@gmail.com','ole@student.uia.no','ali@uia.no','mark@uia.no','even@studen.uia.no','thomas@student.uia.no','thor@husovd.no']
 };

#-----------------------------------------------------#
#				   	 Functions	                      #
#-----------------------------------------------------#
def request_phone(args):
	if args[0] in dict['ID']:
		pos = dict['ID'].index(args[0])
		return 'Phone: ' + dict['Phone'][pos]
	else:
		return 'No number registerd!'

		
def request_email_by_ID(args):
	if str(args[0]) in dict['ID']:
		pos = dict['ID'].index(str(args[0]))
		return 'Email: ' + dict['email'][pos]
	else:
		return 'There is no such ID'

def request_email_by_name(args1,args2):
	print args1
	print args2
	pos1 = dict['F_Name'].index(args1)
	pos2 = dict['L_Name'].index(args2)
	if pos1 == pos2:
		return 'Email: ' + dict['email'][pos1]
	else:
		return 'No match'

def Find_all_emails_by_dep(args):
	count = dict['Dep'].count(str(args[0]))
	length = len(dict['Dep'])
	if  count > 0 and count <= length:
		indices = [i for i, x in enumerate(dict['Dep']) if x == str(args[0])]
		liste = [dict['email'][x] for x in indices ]
		return liste
	else:
		return ['Not a valid department ID']