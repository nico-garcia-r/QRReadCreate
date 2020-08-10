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
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'QRReadCreate' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

"""
    Obtengo variables
"""
if module == "QRRead":

    path = GetParams('path')
    res = GetParams('result')
    try:
        import cv2
        img = cv2.imread(path)
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)
        print(data, "\n", bbox)
        SetVar(res, data)
    except Exception as e:
        PrintException()
        raise e

if module == "QRCreate":
    path = GetParams("path")
    text = GetParams("text")
    try:
        import qrcode
        import PIL
        img = qrcode.make(text)
        img.save(path)
    except Exception as e:
        PrintException()
        raise e

if module == "readBarcode":
    from pyzbar import pyzbar
    import argparse
    import cv2

    path = GetParams("path")
    result = GetParams("result")
    # load the input image
    image = cv2.imread(path)

    # find the barcodes in the image and decode each of the barcodes
    barcodes = pyzbar.decode(image)
    # loop over the detected barcodes
    text = ""
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text += barcodeData

    # Set variable
    SetVar(result, text)