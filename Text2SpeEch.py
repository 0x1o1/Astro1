# Import Google Text to Speech
from gtts import gTTS

import shutil

# Import Audio method from IPython's Display Class
from IPython.display import Audio

class Text2SpeEch:
    def run():
# Provide the string to convert to speech
        text = gTTS(input("please enter the text : "))

            # save the file by any name you want
        text1 = (input("please enter name of the file contiand .wav : "))

            # save the string converted to speech as a .wav file
        text.save(text1) 

            # opening the file
        sound_file = text1

            # Autoplay = True will play the sound automatically
        Audio(sound_file, autoplay=False) 

            # to locate the file after install it from google!       
        source_files = "C:\\Users\\F15pr\\{}".format(text1)

            #to move the file from source path to (text2speech record) file
        destination_folder = 'C:\\Users\\F15pr\\OneDrive\\سطح المكتب\\Main project 1\\text2speech record\\{}'.format(text1)
        #lib for moving
        shutil.move(source_files , destination_folder)


        print("check text2speech file & see you next time :)")