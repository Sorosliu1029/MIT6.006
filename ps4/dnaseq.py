#!/usr/bin/env python2.7

import kfasta
from dnaseqlib import *

### Utility classes ###

# Maps integer keys to a set of arbitrary values.
class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        self.d = dict()
        for p in pairs:
            self.put(p[0], p[1])

    # Associates the value v with the key k.
    def put(self, k, v):
        self.d.setdefault(k, []).append(v)

    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    def get(self, k):
        return self.d.get(k, [])

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)
def subsequenceHashes(seq, k):
    i = 0
    for sub in kfasta.subsequences(seq, k):
        yield (RollingHash(sub).current_hash(), (sub, i))
        i += 1

# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)
def intervalSubsequenceHashes(seq, k, m):
    i = 0
    for sub in kfasta.subsequences(seq, k):
        if (i % m) == 0:
            yield (RollingHash(sub).current_hash(), (sub, i))
        i += 1

# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k, m):
    # d = Multidict(subsequenceHashes(a, k))
    d = Multidict(intervalSubsequenceHashes(a, k, m))
    for (h, (sub_b, i_b)) in subsequenceHashes(b, k):
        for (sub_a, i_a) in d.get(h):
            if sub_b == sub_a:
                yield (i_a, i_b)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0]))
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[3], (500,500), sys.argv[1], sys.argv[2], 8, 100)
