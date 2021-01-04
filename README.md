# SecretSanta
A little Python program to randomly choose from a group of people and send out a small file over Facebook anonymously.

Dependencies:
fbchat https://github.com/fbchat-dev/fbchat (which is unfortunately no longer maintained :( )


Participants are hard coded in, may switch to an input style method, but I find this will hold up better if you want to do it year-to-year (also less room for typos).
Therefore different names on Facebook need to be hard coded too.

People with only Messenger accounts need to be handled seperately, just copy/paste the if statement in the section and remember to copy the continue.

User ID's can be found by "Right Click > View Page Source" on www.facebook.com, and searching the name.
Group ID's can be found by in the address bar of www.facebook.com/messages, you DO NOT need to include /t/

Yes, it just fails if the last person drawn gets their own name. If this is run when there are only a few people it won't take that long, and more people mean that this is less likely to happen.

Enjoy and Happy Holidays!
