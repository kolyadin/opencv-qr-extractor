from pyzbar import pyzbar
import cv2
import sys
import os
from shutil import copyfile

directory = 'samples/'

def decode(file):
    image = cv2.imread(file)
    barcodes = pyzbar.decode(image)

    codeFound = None

    # if len(barcodes) > 0:
    #     print(file + " / QR found")
    # else:
    #     print(file + " / QR not found")

    for barcode in barcodes:

        # (x, y, w, h) = barcode.rect
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        if (barcodeType == 'QRCODE'):
            codeFound = 1

        # text = "{} ({})".format(barcodeData, barcodeType)
        # cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # print("[INFO] found {} barcode {}".format(barcodeType, barcodeData))

    if (codeFound == 1):
        return True
        # print("QR found")
    else:
        return False
        # print("QR not found")


found = notFound = 0

for filename in os.listdir(directory):
    if filename.endswith(".jpeg") or filename.endswith(".png"):
        if decode(os.path.join(directory, filename)):
            found = found + 1
            print(os.path.join(directory, filename), " / QR found (", found, ")")
            copyfile(os.path.join(directory, filename), "found/" + filename)
            continue
        else:
            notFound = notFound + 1
            print(os.path.join(directory, filename), " / QR not found (", notFound, ")")
            copyfile(os.path.join(directory, filename), "notfound/" + filename)
            continue
    else:
        continue

# for filename in os.listdir('samples/'):

# decode(sys.argv[1])
# print('samples/' + filename)

# image = cv2.imread(filename)

# mask = cv2.inRange(image, (0, 0, 0), (200, 200, 200))
# thresholded = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
# inverted = 255 - thresholded

# barcodes = pyzbar.decode(image)
# print(barcodes)


# for barcode in barcodes:
#     # (x, y, w, h) = barcode.rect
#     # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#     barcodeData = barcode.data.decode("utf-8")
#     barcodeType = barcode.type
#     # text = "{} ({})".format(barcodeData, barcodeType)
#     # cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
#     print("[INFO] found {} barcode {}".format(barcodeType, barcodeData))

# cv2.imwrite("new_img.jpg", image)
