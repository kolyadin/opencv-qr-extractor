import cv2
import extractor


def zoomer(image):
    decoded_data = None

    for x in range(1, 10):
        smaller = cv2.resize(image, (0, 0), fx=x / 10, fy=x / 10)
        smaller = cv2.cvtColor(smaller, cv2.COLOR_BGR2GRAY)

        extracted = extractor.decode(smaller)

        if extracted is not None:
            decoded_data = extracted
            break

    return decoded_data


def gray(image):
    decoded_data = None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # extracted = extractor.decod(gray)

    if extracted is not None:
        decoded_data = extracted

    return decoded_data
