import cv2
import sys
import os
import extractor
import argparse

directory = sys.argv[1]

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--img", required=False, help="path to the image file")
ap.add_argument("-d", "--dir", required=False, help="path to the directory with images")
ap.add_argument("-f", "--filter", required=False, help="Apply filter")
args = vars(ap.parse_args())

def deepDecode(image, filter):
    decoded_data = None

    if 'zoomer' == filter:
        for x in range(1, 10):
            smaller = cv2.resize(image, (0, 0), fx=x / 10, fy=x / 10)
            extracted = extractor.decode(smaller)

            if extracted is not None:
                decoded_data = extracted
                break

    elif 'gray' == filter:
        smaller = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        extracted = extractor.decode(smaller)

        if extracted is not None:
            decoded_data = extracted

    elif 'gray,zoomer' == filter:
        for x in range(1, 10):
            smaller = cv2.resize(image, (0, 0), fx=x / 10, fy=x / 10)
            smaller = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            extracted = extractor.decode(smaller)

            if extracted is not None:
                decoded_data = extracted
                break

    return decoded_data


found = notFound = smartFound = 0

if args["dir"]:
    for filename in os.listdir(args["dir"]):
        if filename.endswith(".jpeg") or filename.endswith(".png"):
            src = cv2.imread(os.path.join(args["dir"], filename))

            if extractor.decode(src):
                found = found + 1
                print(os.path.join(args["dir"], filename), " / QR found (", found, ")")
                continue
            else:
                notFound = notFound + 1
                print(os.path.join(args["dir"], filename), " / QR not found (", notFound, ")")

                if (args["filter"]):
                    print(filename, " / Performing deep analyze (", args["filter"], ")... ")

                    if deepDecode(src, args["filter"]):
                        smartFound = smartFound + 1
                        notFound = notFound - 1

                        print(filename, " / Deep analyze success :) (", smartFound, ") ")
                    else:
                        print(filename, " / Deep analyze no luck :(")
elif args["img"]:
    src = cv2.imread(args["img"])

    if extractor.decode(src):
        found = found + 1
        print(args["img"], " / QR found (", found, ")")
    else:
        notFound = notFound + 1
        print(args["img"], " / QR not found (", notFound, ")")

        if (args["filter"]):
            print(args["img"], " / Performing deep analyze (", args["filter"], ")... ")

            if deepDecode(src, args["filter"]):
                smartFound = smartFound + 1
                notFound = notFound - 1

                print(args["img"], " / Deep analyze success :) (", smartFound, ") ")
            else:
                print(args["img"], " / Deep analyze no luck :(")

print("===Summary==")
print("Fast found: ", found)
print("Smart found: ", smartFound)
print("Not found: ", notFound)
