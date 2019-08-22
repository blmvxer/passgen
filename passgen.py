#passgen 0.4.6#
import sys, random, string, subprocess, time, hashlib, binascii
from random import choice
from os import urandom

print('''
.---..---..---..---..---..---..-..-.
| |-'| | | \ \  \ \ | |'_| |- | .` |
`-'  `-^-'`---'`---'`-'-/`---'`-'`-'
               0.4.6''')

def KeyGenerate():
	while True:
		try:
			result = ''.join(random.sample(char_set*6, int(bit_len)))
			print(result)
		except (KeyboardInterrupt):
			exit()

def Hex2Bin():
    while True:
        try:
            result = ''.join(random.sample(char_set*6, int(bit_len)))
            decoded  = ''.join(chr(int(result[i:i+2], 16)) for i in range(0, len(result), 2))
            print(decoded)
        except (KeyboardInterrupt):
            exit()

def NonConsecutive():
    NCKey = []
    index = int(bit_len)
    result = ''.join(random.sample(char_set*6, int(1)))
    NCKey.insert(0, str(result))
    while True:
        try:
            while len(NCKey) < index:
                result = ''.join(random.sample(char_set*6, int(1)))
                if NCKey[0] != str(result):
                    NCKey.insert(0, str(result))
                else:
                    result = ''.join(random.sample(char_set*6, int(1)))
            else:
                print((''.join(NCKey)))
                NCKey = []
                NCKey.insert(0, str(result))
        except (KeyboardInterrupt):
            exit()

def ntlm():
    while True:
        try:
            result = ''.join(random.sample(char_set*6, int(bit_len)))
            hash2 = hashlib.new('md4',str(result).encode('utf-16le')).digest()
            hash3 = binascii.hexlify(hash2)
            print(("Hash: " + hash3 + " " + "Password: " + result))
            if hash3 == hash1:
                print("Found matching hash and password")
                print(result)
                exit()
            else:
                continue
        except(KeyboardInterrupt):
            exit()

def aircrack():
    arglist()
    characterset = input('Enter permutation set: ')
    bit_len = input('Enter character size: ')
    bssid = input('Enter bssid: ')
    capfile = input('Enter capfile: ')
    try:
        cmd = (['python passgen.py ' + characterset + ' | sudo aircrack-ng --bssid ' + bssid + ' -w- ' + capfile])
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        while proc.poll() == None:
            pcrackOut = proc.stdout
            nextline = proc.stdout.readlines()
            print(nextline)
            exit()
    except KeyboardInterrupt:
        proc.terminate()
        proc.wait()
        return
        exit()
    except Exception as e:
        print(e)
        proc.terminate()
        proc.wait()
        exit()
def arglist():
	print ('''options:\n -b32 [num] base32\n -h [num] hexdigits\n -l [num] lowercase\n -lU [num] lower and uppercase\n -l1 [num] lower and numerals\n -U [num] upper ascii\n -U1 [num] upper and numerals\n -lU1 [num] lower upper, and numerals\n -C [char] [num] custom character set and length\n -a aircrack-ng\n -NC [-char] [num] Nonconsecutive character permutations\n SpeedTest is a speed test...\n --help this list\n''')

def SpeedTest():
    char_set = string.ascii_letters + string.digits
    keylist = []
    while True:
        mytime = time.time()
        try:
            while int(time.time() - int(mytime)) != 1:
                result = ''.join(random.sample(char_set*6, 8))
                keylist.append(str(result))
                KeysAsec = len(keylist) + 1
            print((str(KeysAsec) + "k/s"))
            keylist = []
        except (KeyboardInterrupt):
            exit()

args = sys.argv[1:]
try:
    if args:
        for arg in args:
            if arg == '-l':
                char_set = string.ascii_lowercase
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == 'SpeedTest':
                SpeedTest()
            elif arg == '-b32':
                char_set = 'abcdefghijklmnopqrstuvwxyz234567'
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == '-h':
                char_set = string.hexdigits
                if sys.argv[2] == "-b":
                    bit_len = sys.argv[3]
                    Hex2Bin()
                else:
                    bit_len = sys.argv[2]
                    KeyGenerate()
            elif arg == '-lU':
                char_set = string.ascii_letters
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == '-l1':
                bit_len = sys.argv[2]
                char_set = string.ascii_lowercase + string.digits
                KeyGenerate()
            elif arg == '-U1':
                char_set = string.ascii_uppercase + string.digits
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == '-lU1':
                char_set = string.ascii_letters + string.digits
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == '-U':
                char_set = string.ascii_uppercase
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == '-ntlm':
                while True:
                    chars = sys.argv[2]
                    if chars == "-l":
                        char_set = string.ascii_lowercase
                    elif chars == '-b32':
                        char_set = 'abcdefghijklmnopqrstuvwxyz234567'
                    elif chars == '-h':
                        char_set = string.hexdigits
                    elif chars == '-lU':
                        char_set = string.ascii_letters
                    elif chars == '-l1':
                        char_set = string.ascii_lowercase + string.digits
                    elif chars == '-U1':
                        char_set = string.ascii_uppercase + string.digits
                    elif chars == '-lU1':
                        char_set = string.ascii_letters + string.digits
                    elif chars == '-U':
                        char_set = string.ascii_uppercase
                    bit_len = sys.argv[3]
                    hash1 = input("Insert Windows Hash: ")
                    ntlm()
            elif arg == '-NC':
                while True:
                    try:
                        chars = sys.argv[2]
                        if chars == "-l":
                            char_set = string.ascii_lowercase
                        elif chars == '-b32':
                            char_set = 'abcdefghijklmnopqrstuvwxyz234567'
                        elif chars == '-h':
                            char_set = string.hexdigits
                        elif chars == '-lU':
                            char_set = string.ascii_letters
                        elif chars == '-l1':
                            char_set = string.ascii_lowercase + string.digits
                        elif chars == '-U1':
                            char_set = string.ascii_uppercase + string.digits
                        elif chars == '-lU1':
                            char_set = string.ascii_letters + string.digits
                        elif chars == '-U':
                            char_set = string.ascii_uppercase
                        bit_len = sys.argv[3]
                        NonConsecutive()
                    except(KeyboardInterrupt):
                        exit()
            elif arg == '--help':
                arglist()
            elif arg == '-a':
                aircrack()
            elif arg == '-C':
                while True:
                    try:
                        char_set = sys.argv[2]
                        char_len = sys.argv[3]
                        result = ''.join([random.choice(char_set) for _ in range(int(char_len))])
                        print(result)
                    except (IndexError):
                        print((IndexError, "Make sure you've added your character map and length"))
                        exit()
                    except (ValueError):
                        print((ValueError, 'ValueError: sample larger than population'))
                        exit()
                    except (KeyboardInterrupt):
                        exit()
    else:
        arglist()
except IndexError:
    arglist()
