import pyqrcode #import libraries
import png
from pyqrcode import QRCode 
k ="https://github.com/srushtishimpi" #Link that represents QR Code
qr = pyqrcode.create(k) #Genereate QR Code
qr.svg("SrushtiShimpiGithub.svg", scale = 8) #Create and save the svg file 
qr.png("SrushtiShimpiGithub.png", scale = 8) #Create and save the png file