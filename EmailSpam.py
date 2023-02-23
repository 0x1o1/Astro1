import time
from email.message import EmailMessage
import ssl
import smtplib
from getpass import getpass


def run():
    counter = 0
    while(counter<spam):
        em = EmailMessage() # EmailMessage object
        em['From'] = email_sender
        em['To'] = email_reciever
        em['Subject'] = subject # عنوان الرسالة
        em.set_content(body)

        context = ssl.create_default_context()
        counter+=1 # incrementing the counter
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            try:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_reciever, em.as_string()) # em is the object that contains the body
                print('attempt {}, send successfully!'.format((counter)), end='\r')
                time.sleep(1)
            except:
                print('attempt {}, failed.'.format((counter)))

while(True):    
    try:

        email_sender = input('write the email sender: ') #'welcometofear1@gmail.com' # you need to activate the 2fa and then permit python to access by apppasswords
        if email_sender.upper() == 'Q':
            break
        
        email_password = getpass('Password: ') #'xeregsixiquimabg' the 16 space password
        
        email_reciever = input('write the email reciever: ') #'0e4ac34ec5@boxmail.lol'

        while(True):
            subject =input('header of the message: ')
            if len(subject)==0:
                continue
            else:
                break
        while(True):
            body = input('the main body of the message: ')
            if len(body)==0:
                continue
            else:
                break
        while(True):
            spam = int(input('how many times you want to send the message: ')) #the desired number of  mails to send
            spam=spam//1 # to prevent floating numbers
            if spam<0:
                print("negative numbers are not acceptable!")
                continue
            else:
                break
        run()
        break
    except:
        print('the entered password is wrong for {}.\n"(Q)" if you want to quit'.format(email_sender))
        continue