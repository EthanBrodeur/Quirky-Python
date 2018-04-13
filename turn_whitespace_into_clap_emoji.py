#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
hands = ' 👏 '
input_string =  sys.argv[1]
print(input_string.replace(" ", hands))
test_string = "I find my dad in the parking lot. He drives me back to our house and camp is over. So is summer, even though there's two weeks until school starts. This isn't a story about how girls are evil or how love is bad, this is a story about how I learned something and I'm not saying this thing is true or not, I'm just saying it's what I learned. I told you something. It was just for you and you told everybody. So I learned cut out the middle man, make it all for everybody, always. Everybody can't turn around and tell everybody, everybody already knows, I told them. But this means there isn't a place in my life for you or someone like you. Is it sad? Sure. But it's a sadness I chose. I wish I could say this was a story about how I got on the bus a boy and got off a man more cynical, hardened, and mature and shit. But that's not true. The truth is I got on the bus a boy. And I never got off the bus. I still haven't."

output = test_string.replace(" ", hands)

text_file = open("Output.txt", "w")
text_file.write(output)
text_file.close()