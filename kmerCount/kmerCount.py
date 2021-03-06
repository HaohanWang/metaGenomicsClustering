__author__ = 'Haohan Wang'

import numpy as np
import sys

def generateKmerDic(k=4):
    cs = ['A', 'C', 'G', 'T']
    c = -1
    kmer = {}
    for i in range(len(cs)):
        for j in range(len(cs)):
            for s in range(len(cs)):
                for t in range(len(cs)):
                    c += 1
                    m = cs[i]+cs[j]+cs[s]+cs[t]
                    kmer[m] = c
    return kmer


def kmerCount(s, kmer2Ind):
    data = np.zeros(4**4)
    for i in range(len(s)-4):
        k = s[i:i+4]
        if k in kmer2Ind:
            data[kmer2Ind[k]] += 1
    return data


def processingText(filename):
    kmer2ind = generateKmerDic()
    text = [line.strip() for line in open('/home/haohanw/metagenomics/'+filename)]

    f = open('/home/haohanw/metagenomics/index2sampleID_'+filename[:-6]+'.txt', 'w')
    names = []
    data = []

    c = -1
    for i in range(len(text)):
        if i % 4 == 0:
            c += 1
            f.writelines(str(c) + '\t' + text[i]+'\n')
            names.append(text[i])
        elif i%4 == 1:
            data.append(kmerCount(text[i], kmer2ind))
    data = np.array(data).astype(int)
    np.save('/home/haohanw/metagenomics/kmer/'+filename[:-18], data)
    # return data, names

if __name__ == '__main__':
    filename = sys.argv[1]
    processingText(filename)