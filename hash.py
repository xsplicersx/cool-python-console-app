import hashlib
import datetime
import sys
import os
# coding: utf8
def sha_hash():

        print("type the text or password you want to hash using sha256 .")

        input2 = raw_input()

        pwd = (input2)

        hash = hashlib.sha256(str.encode(pwd)).hexdigest()
        print(hash)

        if input2 == "md5":
            md5_hash()
        elif input2 == "sha1":
            sha1_hash()
        elif input2 == "sha224":
            sha224_hash()
        elif input2 == "sha384":
            sha384_hash()
        elif input2 == "sha512":
            sha512_hash()


def md5_hash():
        print("type the text or password you want to hash using md5.")

        input1 = raw_input()

        pwd1 = (input1)

        hash1 = hashlib.md5(str.encode(pwd1)).hexdigest()

        print(hash1)

        if input1 == "sha256":
            sha_hash()
        elif input1 == "sha1":
            sha1_hash()
        elif input1 == "sha224":
            sha224_hash()
        elif input1 == "sha384":
            sha384_hash()
        elif input1 == "sha512":
            sha512_hash()

def sha1_hash():
        print("type the text or password you want to hash using sha1")

        sha1_input = raw_input()

        sha1 = (sha1_input)

        shahash = hashlib.sha1(str.encode(sha1)).hexdigest()

        print(shahash)

        if sha1_input == "md5":
            md5_hash()
        elif sha1_input == "sha256":
            sha_hash()
        elif sha1_input == "sha224":
            sha224_hash()
        elif sha1_input == "sha384":
            sha384_hash()
        elif sha1_input == "sha512":
            sha512_hash()

def sha224_hash():
        print("type the text or password you want to hash using sha224")

        sha224_input = raw_input()

        sha224 = (sha224_input)

        sha224hash = hashlib.sha224(str.encode(sha224)).hexdigest()

        print(sha224hash)

        if sha224_input == "md5":
            md5_hash()
        elif sha224_input == "sha1":
            sha1_hash()
        elif sha224_input == "sha256":
            sha_hash()
        elif sha224_input == "sha384":
            sha384_hash()
        elif sha224_input == "sha512":
            sha512_hash()

def sha384_hash():
        print("type the text or password you want to hash using sha384")

        sha384_input = raw_input()

        sha384 = (sha384_input)

        sha384hash = hashlib.sha384(str.encode(sha384)).hexdigest()

        print(sha384hash)

        if sha384_input == "md5":
            md5_hash()
        elif sha384_input == "sha1":
            sha1_hash()
        elif sha384_input == "sha224":
            sha224_hash()
        elif sha384_input == "sha256":
            sha_hash()
        elif sha384_input == "sha512":
            sha512_hash()

def sha512_hash():
        print("type the text or password you want to hash using sha512")

        sha512_input = raw_input()

        sha512 = (sha512_input)

        sha512hash = hashlib.sha512(str.encode(sha512)).hexdigest()

        print(sha512hash)

        if sha512_input == "md5":
            md5_hash()
        elif sha512_input == "sha1":
            sha1_hash()
        elif sha512_input == "sha224":
            sha224_hash()
        elif sha512_input == "sha384":
            sha384_hash()
        elif sha512_input == "sha256":
            sha_hash()


def help_h():
    print("Remove a file or folder in a directory type (remove)")
    print("Make a file or folder in a directory type (make)")
    print("if you wish to shutdown your computer then type (shutdown)")


    help1 = raw_input()

    if help1 == "remove":
        remove_file()
    elif help1 == "make":
        make_file()
    elif help1 == "shutdown":
        shutdown_computer()


def remove_file():
    print("type the file you want to Remove.")
    print("note: don not drag and drop file youhave to type manualy, backslashes are not supported")

    rmfile = raw_input()


    os.remove(rmfile)

def make_file():
    print("type the file you want to make.")
    print("note: don not drag and drop file youhave to type manualy")


    makefile = raw_input()

    open((makefile),"w+")

def shutdown_computer():


    os.system("shutdown -h now")





while True:

    print '\033[1;32m if you want sha256 bit hashing then type (sha256) \033[1;m'
    print '\033[1;33m if you want md5 hashing then type (md5)\033[1;m'
    print '\033[1;35m if you want sha1 hashing then type (sha1)\033[1;m'
    print '\033[1;34m if you want sha244 hashing then type (sha244)\033[1;m'
    print '\033[1;36m if you want sha384 hashing then type (sha384)\033[1;m'
    print '\033[1;31m if you want sha512 hashing then type (sha512)\033[1;m'
    print("or type (help) for more options")


    hash_input = raw_input()


    if hash_input == "sha256" :
        sha_hash()
    elif hash_input == "md5":
        md5_hash()
    elif hash_input == "sha1":
        sha1_hash()
    elif hash_input == "sha224":
        sha224_hash()
    elif hash_input == "sha384":
        sha384_hash()
    elif hash_input == "sha512":
        sha512_hash()
    if hash_input == "help":
        help_h()
    if hash_input == "remove":
        remove_file()
    if hash_input == "make":
        make_file()
    if hash_input == "shutdown":
        shutdown_computer()
    elif hash_input == "**":
        print("that is not reconized as a command")
