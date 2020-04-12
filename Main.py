import FileLoadAndRead

def main():
    file = FileLoadAndRead.loadFile("alice.txt")
    for line in file:
        print(line)
    file.close()

if __name__ == "__main__":
    main()