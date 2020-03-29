import random

def randnuclgen(len = 10):
    
    '''This returns a random nucleotide sequence with only argument length
    Example: print(randnuclgen(12))
    Default value of len is set to 10'''

    bases = "ATGC"
    result = ""
    for i in range(len):
        result = result + bases[random.randint(0,3)]
    return result
