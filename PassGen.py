import secrets
import hashlib
import sys
import cv2
import os
import argparse

def get_arg():
    parser = argparse.ArgumentParser(description='Generate Password From An Image')
    parser.add_argument('--length', '-l', type=int, nargs='?', help='The intended length of the generated password')
    args= parser.parse_args()
    if not args.length:
        try:
            length = int(input("Enter password length: "))
        except ValueError:
            sys.exit("Invalid input")

    else:
        length = args.length

    return length


def take_picture():
    camera = cv2.VideoCapture(0)

    # return a single frame in variable `frame`
    ret, frame = camera.read()
    if not ret:
        print("failed to grab frame")

    cv2.imwrite("temp.jpg", frame)
    camera.release()
    cv2.destroyAllWindows()


def hash_file():
    """ "This function returns the SHA-1 hash
    of the file passed into it"""

    # make a hash object
    h = hashlib.sha256()

    # open file for reading in binary mode
    with open("temp.jpg", "rb") as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b"":
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


def pass_generate(length, hash):
    # try:
    #     length = int(input("Enter password length: "))
    # except ValueError:
    #     sys.exit("Invalid input")

    password = "".join(secrets.choice(hash + str.upper(hash)) for i in range(length))
    print(password)


def remove_tmp():
    try:
        os.remove("temp.jpg")
    except:
        pass


def main():
    take_picture()
    pass_generate(get_arg(), hash_file())
    remove_tmp()


if __name__ == "__main__":
    main()
