from gtts import gTTS 
import os 

mytext = 'BHAAG JA BHUTIYA'

language = 'hi'

myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("welcome.mp3") 

os.system("welcome.mp3") 