from __future__ import print_function
import cv2
import sys
import os
import extractor
import argparse
import optimizer


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


directory = sys.argv[1]

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required=False, help="path to the directory with images")
ap.add_argument("-f", "--filter", required=False, help="Apply filter")
args = vars(ap.parse_args())


def deepDecode(image, filter):
    decoded_data = None

    if 'zoomer' == filter:
        decoded_data = optimizer.zoomer(image)

    elif 'gray' == filter:
        decoded_data = optimizer.gray(image)

    elif 'gray,zoomer' == filter:
        decoded_data = optimizer.gray(image)

        if decoded_data is None:
            decoded_data = optimizer.zoomer(image)

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
                f = open('notfound.txt', 'a')
                f.write(filename + "\n")
                f.close()

                if (args["filter"]):
                    print(filename, " / Performing deep analyze (", args["filter"], ")... ")

                    if deepDecode(src, args["filter"]):
                        smartFound = smartFound + 1
                        notFound = notFound - 1

                        print(filename, " / Deep analyze success :) (", smartFound, ") ")
                    else:
                        print(filename, " / Deep analyze no luck :(")
                        f = open('notfound_smart.txt', 'a')
                        f.write(filename + "\n")
                        f.close()

overall = found + smartFound + notFound

print("===Summary==")
print("Overall: ", overall)
print("Fast found: ", found)
print("Smart found: ", smartFound)
print("Not found: ", notFound)

print("Efficiency: ", (found + smartFound) * 100 / overall, "%")
