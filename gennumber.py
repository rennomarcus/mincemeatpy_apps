from sys import argv
import random

def generate_number():
    if len(argv) is not 3:
        print("error. number of arguments is invalid.")
    else:
        file = open(argv[1],  "w")
        size = int(argv[2])
        
        file.truncate()
        for i in range(size):
            file.write(str(random.randint(1, 100)) + "\n")
        file.close()

if __name__ == "__main__":
    generate_number()
