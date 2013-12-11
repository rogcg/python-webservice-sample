#-*- encoding: iso-8859-1 -*-

import SimpleXMLRPCServer
db = 'users.txt'
passwds = 'passwds.txt'
def login(theUser, password): 
    try:
        rowUser = open(db,'r').read()
        rowPasswds = open(passwds, 'r').read()
    except:
        # Return False in case it cant open the file
        return False
    
    # make the validation.
    for row in rowUser.split('\n'):
        for rowPasswd in rowPasswds.split('\n'):
            user = row
            passwd = rowPasswd
            if user == theUser and passwd == password:
                return True
    return False

def register(theUser, password): 
	
    userExists = False
   
    if login(theUser, password):
        return False

    try:
        rowUser = open(db,'r').read()
	# fetch for the username in the file
        for row in rowUser.split('\n'):	
	    if row == theUser:
	        userExists = True
		break
	
	if not userExists:
            connection = open(db,'a')
            connection2 = open(passwds,'a')
            connection.write('%s\n'%theUser)
            connection2.write('\n%s'%password)
            connection.close()
            connection2.close()
            return True  
        else:
            return 'user_exists'  
    except IOError as e:

	# if we reach this part, it means the file doesn't exist yet,
	# so we may proceed with the registration
        connection = open(db,'a')
        connection2 = open(passwds,'a')
        connection.write('%s\n'%theUser)
        connection2.write('\n%s'%password)
        connection.close()
        connection2.close()		

server = SimpleXMLRPCServer.SimpleXMLRPCServer(('localhost',8082), allow_none=True)
server.register_function(login)
server.register_function(register)
server.serve_forever()
