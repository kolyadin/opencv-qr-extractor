import cv2
import sys
import os
import extractor

directory = sys.argv[1]

found = notFound = smartFound = 0

for filename in os.listdir(directory):
    if filename.endswith(".jpeg") or filename.endswith(".png"):
        src = cv2.imread(os.path.join(directory, filename))

        if extractor.decode(src):
            found = found + 1
            print(os.path.join(directory, filename), " / QR found (", found, ")")
            continue
        else:
            notFound = notFound + 1
            print(os.path.join(directory, filename), " / QR not found (", notFound, ")")
            print("Performing deep analyze... ")

            deepDecode = extractor.deepDecode(src)

            if deepDecode:
                smartFound = smartFound + 1
                notFound = notFound - 1
                print("success (", smartFound ,")")
                print(deepDecode)
            else:
                print("no luck :(")


print("Summary")
print("Fast found: ", found)
print("Smart found: ", smartFound)
print("Not found: ", notFound)
