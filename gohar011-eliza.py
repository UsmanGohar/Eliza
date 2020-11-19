
# Programming Assignment 1
# Usman Gohar, Intro. to Natural Language Processing
# Eliza Program

import random    #import random library
import re        #import regular expression library
temp1="empty"    
print"This is Eliza The Academic Advisor, programmed by Usman Gohar\n\n\n"
e=0;     # all of these variables are checks to make sure sentences are not always repeated by Eliza
c=0;
d=0;
f=0;
print '\n[Eliza]- Hi, I am an academic advisor. What is your name?'
name= raw_input("<")
print "Hi, " + name + "." " What's your major?"

while(e!=1):     #Repeat until e==1, i.e. until exit is typed by user

	Exit=['>Thank you, your bill is $200','>Bye. Stay in touch','>Glad I could help']  #Different responses to typing exit
	Repeat=[">Stop repeating yourself!",">I got you! Move on!",">Don't waste my time, other students need me"]   #Different responses if someone repeats his/herself
	more=[">Please tell me more", ">That's interesting", ">I see"]   #When none of the keywords match

	check=random.randint(0,2)  #Randomly select response to user repeating his/herself
        response=raw_input("< ")   #Prompt user
	if temp1==response:        #Check whether user repeating his/herself
		print Repeat[check]
		continue
	temp1=response             #Store previous response for the if statement above

	p1=re.compile(r'\bComputer Science\b|\bElectrical Engineering\b|\bMathematics\b', re.IGNORECASE)    #Check for name of major
	p2=re.compile('undecided') 	#When major is undecided
	p3=re.compile('question')	#The first time a question is formally asked i.e Can I ask a question?
	p11=p1.search(response)
	p22=p2.search(response)
	p33=p3.search(response)

	if p11 and c==0:
		print ">That's good. Do you like it?"          #Replies to the questions above i.e major, undecided, question etc
		c=1;
		continue
	if p22:
		print ">Which major is on your mind?"
		continue
	if p33 and d==0:
		print ">Sure, how can I help?"
		d=1
		continue

	p4= re.compile('[0-9]+ [a-z]+')       #Search for gibberish typed
	p5= re.compile('don\'t know')         # If user says he/she doesn't know
	p44= p4.search(response)
	p55= p5.search(response)
	if p44:
		print ">Sorry, can you rephrase that?"
		continue
	if p55:
		print ">That's what I'm here for"
		continue

	# The following below are the different rules applied in this Eliza Program. Most of them are self explanatory

	r1=re.sub(r"I can't (.*)",r">Perhaps you could if you tried harder, maybe?",response)
	r2=re.sub(r"(.*)computer(.*)",">Do you think computers are any less human?",response)    
	r3=re.sub(r'I have (.*)',r'>So you have \1, what will you do about it?',response)
	r4=re.sub("(.*)\?",">I think your question answers itself.",response)
	r5=re.sub("I think (.*)",">But you're not really sure?",response)
	r6=re.sub("Why (.*) major (.*)?",">It's usually a personal preference but it pays well",response)
	r7=re.sub(r"(.*) \bquestion\b (.*)",r">Sure, how can I help you?",response)
	r8=re.sub(r"Is it (.*)", r'>If it were \1, what would you do?',response)             
        r9=re.sub(r'No', r'>Why not?',response)         
        r10=re.sub("(.*) sorry (.*)", "There are times when no apology is needed",response)
	r11=re.sub("Because (.*)", "Is that the real reason",response)
	r12=re.sub("Yes", "Hmm, you seem quite sure",response)
	r13=re.sub(r"I feel (.*)",r"When do you usually feel \1?", response)
	r14=re.sub(r"How can I logout?", r"Type exit and you're good to go",response)
        n=re.compile('exit',re.IGNORECASE) #convert to object
        q=n.search(response)   #search keyword "exit" in response


        if r1!=response:         # If any of the responses have been substituted, print substitute else ask something random
                print r1
		continue
        elif r2!=response:
                print r2
		continue
        elif r3!=response:
                print r3
		continue
        elif r4!=response:
                print r4
		continue
	elif r5!=response:
		print r5
		continue
	elif r6!=response:
		print r6
		continue
	elif r7!=response:
		print r7
		continue
	elif r8!=response:
		print r8
		continue
	elif r9!=response:
		print r9
		continue
	elif r10!=response:
		print r10
		continue
	elif r11!=response:
		print r11
		continue
	elif r12!=response:
		print r12
		continue
	elif r13!=response:
		print r13
		continue
	elif r14!=response:
		print r14
		continue
        elif q:
                e=1      #Exit
		num1=random.randint(0,2)  #Generate random number to pick random response when exit is typed
		print Exit[num1]
                break
        else:

		if f==0:
			f=1
			print ">So where are you from, " + name + "?"
		else:
			num=random.randint(0,2)  #pick random response to when no keywords found
                	print more[num]

