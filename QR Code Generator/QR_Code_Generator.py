#Standard Qr Code generator using By Krish Lalwani
#github.com/krishlalwani0


#importing Libraries
import qrcode
from PIL import Image

#Introduction to Programs
print ("------------------------QR CODE MAKER---------------------------\n\n")
text = input("Enter text or Link you want to create QR Code of: \n")
qr_name = input("Enter name of saved QR Image:\n")
color = input("Enter color of QR Code:\n\n1 for Standard Black&White.\n2 for Red.\n3 for green.\n")

#Characterising the QR Code 
qr = qrcode.QRCode(version=1,
error_correction=qrcode.constants.ERROR_CORRECT_H,
border=4
)

#Adding the Data to Qr code
qr.add_data(text)
qr.make(fit=True)

#Defining the color of the Qr Code
img = qr.make_image()
if color == 1:
	img = qr.make_image(fill_color="black", back_color="white")
elif color == 2:
	img = qr.make_image(fill_color="red", back_color="white")
elif color == 3:
	img = qr.make_image(fill_color="green", back_color="white")

#Saving the QR Code.
#The image will be saved in png by default.
img.save(qr_name + ".png")

#End of Program...