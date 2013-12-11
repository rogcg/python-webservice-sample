#-*- encoding: iso-8859-1 -*-

import xmlrpclib, getpass, hashlib

client = xmlrpclib.ServerProxy('http://localhost:8082')
user = raw_input('User: ')
passwd = hashlib.sha256(getpass.getpass('Password: ')).hexdigest()
if client.login(user, passwd):
    print 'You are logged.'
else:
    print 'The user doesnt exists. Trying to register..'
    # make a call to try to register the user
    result = client.register(user, passwd)
    if result == 'user_exists':
	print 'Oops..username already exists.'
    else:
        print 'You are now registered. please login.'
