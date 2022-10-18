# Create and read QR code
  
Module to create and read QR code

*Read this in other languages: [English](Manual_QRReadCreate.md), [Portugues](Manual_QRReadCreate.pr.md), [Español](Manual_QRReadCreate.es.md).*
  
![banner](imgs/Banner_QRReadCreate.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### ReadQR
  
Read a QR code from a PNG file
|Parameters|Description|example|
| --- | --- | --- |
|Path of QR in PNG|Select the PNG file that contains the QR code|C:/Users/user/Desktop/file.png|
|Assign result to variable|Assign the content of the qr code to a variable|variable|

### CreateQR
  
Create a QR code and save it to a PNG file
|Parameters|Description|example|
| --- | --- | --- |
|Path where the image will be stored|Path where the PNG image with the generated QR code will be stored|C:/Users/user/Desktop/file.png|
|Write the QR text|Write the text that will be converted into QR code|htps://rocketbot.com|

### Barcode reader
  
Read a barcode from a PNG or JPG file
|Parameters|Description|example|
| --- | --- | --- |
|PNG file path|PNG file path with the barcode|C:/Users/user/Desktop/file.png|
|Assign result to variable|Assigns the barcode result to a variable|variable|
