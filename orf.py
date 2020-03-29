from seqgen import randnuclgen as sq

myseq = sq(100)

print(myseq)

for i in range(0, len(myseq)):
    if myseq[i:i+3] == "ATG":
        print("Start Condon at", i)

        for i in range(i, len(myseq)):
            if myseq[i:i+3] == "TAA" or myseq[i:i+3] == "TGA" or myseq[i:i+3] == "TAG":
                print(myseq[i:i+3], "Termiantor at", i)

