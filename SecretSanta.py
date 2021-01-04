#import fbchat
import os
import random

receivers = {
	# Name:Address
	"Alice":"123 Main Street",
	"Bob":"456 South Avenue",
	"Carol":"789 Park Place",
	"Dan":"1000 Paper Street"
}

givers = [''] * len(receivers)

for i,key in enumerate(receivers):
	givers[i] = key

path = os.getcwd()
path = path+"/Secret Santa"

if not os.path.exists(path):
	os.mkdir(path)

master_list = ""

for receiver in receivers:
	rand = random.randint(0,len(givers)-1)
	
	if len(givers) != 1:
		while givers[rand] == receiver:
			rand = random.randint(0,len(givers)-1)

	#print to file
	chimney = path+"/"+givers[rand]
	if not os.path.exists(chimney):
		os.mkdir(chimney)
	file = open(chimney+"/"+givers[rand]+".txt","w")
	file.write("Congrats! Buy a gift for " + receiver + ", and send it to them at " + receivers.get(receiver) +
"\n\n     _[_]_\n" +
'      (">\n' +
"  `--( : )--'\n" +
"    (  :  )\n" +
'  "" -...- ""\n')
	file.close()

	master_list = master_list + givers[rand] + " -> " + receiver + "\n"

	#if last person gets last person
	if givers[rand] == receiver:
		print("FAILURE")
		os.rename(path, os.getcwd()+"/FAILURE")
		exit()

	givers.remove(givers[rand]);

file = open(path+"/ Master List.txt","w")
file.write(master_list)

#send out files
from fbchat import Client
from fbchat.models import *
email = raw_input("What is your Facebook email? : ")
password = raw_input("What is your Facebook password? : ")
client = Client(email, password)

for key in receivers:
	if not client.isLoggedIn():
		client.login(email, password)

	#Dumb people with no facebook accounts, but messenger accounts.
	#find ID by "Right Click > View Page Source" on www.facebook.com, search name
	if key == "Bob": #123456789
		client.sendLocalFiles(
	    	path+"/"+key+"/"+key+".txt",
	    	message=Message(text="Merry Christmas!"),
	    	thread_id="123456789",
	    	thread_type=ThreadType.USER,
		)
		continue

	#people who changed names
	if key == "Alice":
		key = "Alex"

	#pick first person after searching for another user
	#if popularly named, change key with more specific name (or hard code with Dumb People)
	users = client.searchForUsers(key)
	person = users[0]

	#unchange names
	if key == "Alex":
		key = "Alice"

	client.sendLocalFiles(
	    path+"/"+key+"/"+key+".txt",
	    message=Message(text="Merry Christmas!"),
	    thread_id="{}".format(person.uid),
	    thread_type=ThreadType.USER,
	)

client.send(Message(text="Hey Everyone! Your Secret Santa's should have been messaged to you! To keep it fair " + 
	"and secret, generating and sending out the files was automated, but let me know if there was a problem and " + 
	"I can manually give it to you."),
	thread_id='0123456789ABCDEF',
	thread_type=ThreadType.GROUP)
