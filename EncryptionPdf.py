
from PyPDF2 import PdfReader, PdfWriter
from getpass import getpass

class EncryptionPdf:
# open the pdf file
    def run():
        #pdfbefore = input("please enter the name of PDF file : ")

        #pdfpath = "C:\\Users\\F15pr\\Downloads\\{}".format(pdfbefore)
        
        with open(pdfName:=input("enter the pdf name and its extension: "), "rb") as input_file: #enter the full extended address to run
            
                # creaete object to read from the file
                input_pdf = PdfReader(input_file)

                # create object and write previous file to new file
                output_pdf = PdfWriter(input_pdf)
                output_pdf.append_pages_from_reader(input_pdf)

                # write your password and encrypt the file
                output_pdf.encrypt(password:=getpass("enter the password for the file: ")) 
        
        
                # open the new encrypted file 
        with open("C:\\Users\\F15pr\\OneDrive\\سطح المكتب\\Main project 1\\PDF Encrypion\\safepdf.pdf" , "wb") as out_file:
            output_pdf.write(out_file)
            print('woooow pdf is saved!!!')
            