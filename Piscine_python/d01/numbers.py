def print_nb():
    with open("numbers.txt") as file:
        line = file.read()
        line = line.replace(", ", "\n")
        print(line)
        

if __name__ == '__main__':
    print_nb()