# -*- coding: utf-8 -*- 
import math

def split_tweet(too_long_string):
	too_long_string = too_long_string.rstrip('\n')
	if len(too_long_string) <= 140:
		return [too_long_string]

	elif len(too_long_string) <= 134*9:
		ret =[]
		num = int(math.ceil(len(too_long_string)/134.0))
		split = too_long_string.split()
		for x in range(num):
			#abandoned the below 2 lines since they didn't cut Tweets at the nearest word boundary
			#cut = too_long_string[x*134:(x*134+134)] + (' (%(current_level)s/%(total_tweets)s)' % \
			#{'current_level': x+1, 'total_tweets': num})
			#ret.append(cut)
			length_of_tweet = 0
			tweet = ""
			while length_of_tweet < 134:
				if length_of_tweet + len(split[0]) < 134:
					if len(tweet) != 0:
						tweet += " " + split[0]
						length_of_tweet += len(split[0]) + 1
					else: #don't need a leading space for the first word in a tweet
						tweet += split[0] 
						length_of_tweet += len(split[0])
					del split[0]
					if len(split) == 0:
						break
				else:
					break
			tweet += (' (%(current_level)s/%(total_tweets)s)' % {'current_level': x+1, 'total_tweets': num})		
			ret.append(tweet)
		return ret , alt_ret

	elif len(too_long_string) <= 132*99:
		ret = []
		num = int(math.ceil(len(too_long_string)/132.0))
		split = too_long_string.split()
		for x in range(num):
			#cut = too_long_string[x*132:(x*132+132)] + (' (%(current_level)s/%(total_tweets)s)' % \
			#{'current_level': x+1, 'total_tweets': num})
			#ret.append(cut)
			length_of_tweet = 0
			tweet = ""
			while length_of_tweet < 132:
				if length_of_tweet + len(split[0]) < 132:
					if len(tweet) != 0:
						tweet += " " + split[0]
						length_of_tweet += len(split[0]) + 1
					else: #don't need a leading space for the first word in a tweet
						tweet += split[0] 
						length_of_tweet += len(split[0])
					del split[0]
					if len(split) == 0:
						break
				else:
					break
			tweet += (' (%(current_level)s/%(total_tweets)s)' % {'current_level': x+1, 'total_tweets': num})		
			ret.append(tweet)
		return ret

	else:
			print("why are you trying to Tweet a novel?")

#Long case
test_string = '''After so many study guides, so many practice tests and proficiency and achievement tests, it would have been impossible for us not to learn something, but we forgot everything almost right away and, I’m afraid, for good. The thing that we did learn, and to perfection—the thing that we would remember for  the rest of our lives-was how to copy on tests. Here I could easily ad-lib an homage to the cheat sheet, all  the test material reproduced in tiny but legible script on a minuscule bus ticket. But that admirable  workmanship would have been worth very little if we hadn’t also had the all-important skill and audacity  when the crucial moment came: the instant the teacher lowered his guard and the ten or twenty golden seconds began. At our school in particular, which in theory was the strictest in Chile, it turned out that copying was  fairly easy, since many of the tests were multiple choice. We still had years to go before taking the  Academic Aptitude Test and applying to university, but our teachers wanted to familiarize us right away  with multiple-choice exercises, and although they designed up to four different versions of every test,  we always found a way to pass information along. We didn’t have to write anything or form opinions or  develop any ideas of our own; all we had to do was play the game and guess the trick. Of course we studied,  sometimes a lot, but it was never enough. I guess the idea was to lower our morale. Even if we did nothing  but study, we knew that there would always be two or three impossible questions. We didn’t complain.  We got the message: cheating was just part of the deal. I think that, thanks to our cheating, we were able to let go of some of our individualism and become a  community. It’s sad to put it like that, but copying gave us solidarity. Every once in a while we  suffered from guilt, from the feeling that we were frauds—especially when we looked ahead to the future-but our indolence and defiance prevailed'''
#medium case
test_string2 = '''After so many study guides, so many practice tests and proficiency and achievement tests, it would have been impossible for us not to learn something, but we forgot'''
