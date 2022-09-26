# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'QRReadCreate' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

"""
    Funciones
"""
def read_qr_code(filename):
    import cv2

    img = cv2.imread(filename)
    detect = cv2.QRCodeDetector()
    value, points, straight_qrcode = detect.detectAndDecode(img)

    return value

def create_qr_code(data, filename):
    import qrcode
    img = qrcode.make(data)
    img.save(filename)
    
def read_bar_code(filename):
    import cv2
    from pyzbar.pyzbar import decode

    img = cv2.imread(filename)
    barcodes = decode(img)

    text = ""
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text += barcodeData
    
    return text


"""
    Obtengo variables
"""
if module == "QRRead":

    path = GetParams('path')
    res = GetParams('result')
    try:
        
        data = read_qr_code(path)
        if data:
            SetVar(res, data)
        else:
            SetVar(res, "QR code cannot be read")   

    except Exception as e:
        PrintException()
        raise e

if module == "QRCreate":
    path = GetParams("path")
    text = GetParams("text")
    
    try:
        create_qr_code(text, path)
    except Exception as e:
        PrintException()
        raise e

if module == "readBarcode":
    path = GetParams("path")
    result = GetParams("result")
    
    try:
        text = read_bar_code(path)
    except Exception as e:
        PrintException()
        raise e

    SetVar(result, text)