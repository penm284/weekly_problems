def DNA(str):
    new = list(str)
    count = -1
    for i in new:
        count += 1

        if i == 'a':
            new[count] = 't'
        if i == 't':
            new[count] = 'a'
        if i == 'g':
            new[count] = 'c'
        if i == 'c':
            new[count] = 'g'

    print(new)
return (new)
DNA('attgc')
