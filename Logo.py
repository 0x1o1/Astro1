from pyfiglet import figlet_format
import random


style = ['standard', 'cybermedium', 'big', 'isometric3'] # 4 different styles
class Logo:
        
    def run(path):
        print(figlet_format(path, random.choice(style)))