from pyzbar import pyzbar


def decode(image):
    barcodes = pyzbar.decode(image)
    codeFound = None

    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        if barcodeType == 'QRCODE':
            codeFound = barcodeData
            break

    return codeFound
