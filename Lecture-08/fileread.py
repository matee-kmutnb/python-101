def main():
    infile = open('philosephers.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)
    main()