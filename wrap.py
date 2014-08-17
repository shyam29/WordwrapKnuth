import sys

L = 0
INF = 1000

def printSol(words, total, p):
    start = p[total]
    end = total

    if start != 1:
        printSol(words, start - 1, p)

#   print from start to end in one line
    global L
    for i in xrange(start, end+1):
        sys.stdout.write(words[i-1])
        if i != end:
            sys.stdout.write(' ')
    sys.stdout.write('\n')

def printSolJustified(words, total, p):
    start = p[total]
    end = total
    
    if start != 1:
        printSolJustified(words, start - 1, p)

#   print from start to end in one line
    totalLen = 0
    global L
    for i in xrange(start, end+1):
        totalLen += (len(words[i-1]) + 1)
    totalLen -= 1

    spaceLeft = L - totalLen
    extraSpace = 0
    if spaceLeft > 0:
        extraSpace = (spaceLeft / (end - start))
        if spaceLeft % (end - start) != 0:
            extraSpace += 1
#   print (spaceLeft, extraSpace)

#   distribute the spaces
    for i in xrange(start, end+1):
        sys.stdout.write(words[i-1])
#       print extra spaces to right justify
        for j in xrange(extraSpace):
            if spaceLeft > 0:
                sys.stdout.write(' ')
                spaceLeft -= 1
        if i != end:
            sys.stdout.write(' ')
    sys.stdout.write('\n')


def main():
    if len(sys.argv) != 3:
        print "Usage: wrap.py <filename> <maxwidth>"
        sys.exit(-1)
    
    try:
        fin = open(sys.argv[1], 'r')
    except:
        print "Error: Cannot open file " + sys.argv[1]
        sys.exit(-1)

    fileStr = fin.read()
    words = fileStr.split()
    total = len(words)
    fin.close()

    print 'Original print:: \n'
    print fileStr + '\n'

    global L
    try:
        L = int(sys.argv[2])
    except:
        print "Usage: wrap.py <filename> <maxwidth>"
        sys.exit(-1)

    # calculate e(i,j) for all pair of words
    e = [[0 for x in xrange(total+1)] for x in xrange(total+1)]
    for i in xrange(1, total+1):
        for j in xrange(i, total+1):
            for k in xrange(i, j+1):
                e[i][j] += (len(words[k-1]) + 1)
            e[i][j] -= 1; #remove one for last space
            e[i][j] = L - e[i][j] #calculate 'slack' for each line
            if e[i][j] < 0:
                e[i][j] = INF
            e[i][j] = e[i][j]**2

#   print 'e is ' + repr(e)

    #calculate the number of words in each line
    p = [0 for x in xrange(total+1)]
    c = [0 for x in xrange(total+1)]
    c[0] = 0
    for j in xrange(1, total+1):
        c[j] = INF*INF
        for i in xrange(1, j+1):
            if c[i-1] + e[i][j] < c[j]:
                c[j] = c[i-1] + e[i][j]
                p[j] = i

#    print 'c is ' + repr(c)
#    print 'p is ' + repr(p)
#    print '\n\n'

    print 'Pretty print:: \n'
    printSol(words, total, p)
    print '\n'
    print 'Justified print:: \n'
    printSolJustified(words, total, p)
    print '\n'

if __name__ == "__main__":
    main()
