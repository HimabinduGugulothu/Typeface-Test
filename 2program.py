from phonetics import Phonetics
import numpy as np

def levenshtein(sequence1, sequence2):  
    size_x = len(sequence1) + 1
    size_y = len(sequence2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in xrange(size_x):
        matrix [x, 0] = x
    for y in xrange(size_y):
        matrix [0, y] = y

    for x in xrange(1, size_x):
        for y in xrange(1, size_y):
            if sequence1[x-1] == sequence2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])
    
    Moorthy", "Moorthi", "Murthi" 
word1 = Phonetics("Moorthy")
word2 = Phonetics("Moorthi")
print ("Comparing %s with %s" % (word1.getText(), word2.getText()))
codeList1 = word1.phoneticCode()
codeList2 = word2.phoneticCode()
weight = {
    "soundex": 0.2,
    "caverphone": 0.2,
    "metaphone": 0.5,
    "nysiis": 0.1
}
algorithms = ["soundex", "caverphone", "metaphone", "nysiis"]
total = 0.0
for entry in algorithms:
    code1 = codeList1[entry]
    code2 = codeList2[entry]
    lev = levenshtein (code1, code2)
    currentWeight = weight[entry]
    print ("comparing %s with %s for %s (%0.2f: weight %0.2f)" % (code1, code2, entry, lev, currentWeight))
    subtotal = lev * currentWeight
    total += subtotal
print ("total: %0.2f" % total)
