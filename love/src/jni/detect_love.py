import sys
from os import path

def main(argv):
    if len(argv) > 0:
        if path.isdir(f"{argv[0]}/love") and path.isfile(
            f"{argv[0]}/love/Android.mk"
        ):
            print("yes")
        else:
            print("no")
    else:
        print("no")

if __name__ == "__main__":
    main(sys.argv[1:])
