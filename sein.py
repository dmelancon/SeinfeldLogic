import sys
import random
text = open('untitled.html')  # source code for "http://www.expss.com/Seinfeld/SeinfeldEpisodes.htm"
words = list()
plot = list()
sentence =dict()
i=0
x=0
#parsing episode descriptions from the HTML source 
for line in text :
	line = line.strip()
	words.append(line)
for i in range(73,1452):
	if (i-65) % 	7 == 0:
		words[i] = words[i][44:-12].replace("Description</B>", "")
# parse episodes descriptions into individual sentences and put them into a list		
		if "pisode" not in words[i]:
			words[i] = words[i].strip()
			words[i] = words[i].split(".")
			for l in words[i]:
				if l[:-1] == ".":
					l = l-"."
				if l != "" and l != "." and l != " ":	
					plot.append(l)
#put each line of the episdoe description into a dictionary
for line in plot:
	sentence[str(x)] = line
	x+=1
#randomly prints 3 lines to create new logical statement. "If this and this, than this. Unless, that is, this. "

print "If" + sentence[str(random.randrange(509))] + " and " + sentence[str(random.randrange(509))] + ", than " + sentence[str(random.randrange(509))] +". Unless, that is, " +  sentence[str(random.randrange(509))] +"."
