import Logo

if __name__ == '__main__': # to make Main.py the main and the first to run class
    pass

class Main(Logo.Logo):
    def run(self):
            
        Logo.Logo.run(path='FaWaZ')
        
        print('**\t\t   Welcome to Hacker Fawaz tool\t\t**\n\nEnter a number to choose a tool : \n\n1 - Port scanner.\t\t2 - Email spamming tool.\t\t3 - DDOS tool.\t\t4 - Text2SpeEch tool.\t\t5 - EnCrYpTion tool.\n\n')
        inp = input("Choose a tool: ")

        if inp=='1':
            print()
            Logo.Logo.run(path='port Scanner')
            print('\t\twelcome to Port scanner tool\n')
            import PortScanner
            print("PORT    STATE   SERVICE   VERSION")
            PortScanner.run()

        elif inp == '2':
            print()
            Logo.Logo.run(path='Email spam')
            import EmailSpam
            EmailSpam.run()

        elif inp == '3':
            print()
            Logo.Logo.run(path='DDoS tool')
            import DDoSTool
            DDoSTool.run()
        
        elif inp == '4':
            print()
            Logo.Logo.run(path='Text2SpeEch tool')
            import Text2SpeEch
            Text2SpeEch.Text2SpeEch.run()
        
        elif inp == '5':
            print()
            Logo.Logo.run(path='Encryption tool')
            import EncryptionPdf
            EncryptionPdf.EncryptionPdf.run()
            
        else:
          print('the command {} is not recognized!'.format(inp))

a = Main()
while(True):
    
    a.run()
    escape = input("\n(Q) to quit: ")

    if escape.upper() == 'Q':
        break
    else:
        print("the input is not correct!!")
        