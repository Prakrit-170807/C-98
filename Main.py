def count():
    FileName = input("Please Enter The File name >>>")
    counter = 0 
    File = open(FileName)
    for f in File:
        words = f.split()
        counter = counter + len(words)
    print (words, counter)
count()