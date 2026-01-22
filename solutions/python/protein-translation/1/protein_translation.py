def proteins(strand):
    output = []
    n = 3
    codon_list = [strand[i:i+n] for i in range(0, len(strand), n)]

    protein_codons_dict = {
        'Methionine' : 'AUG',
        'Phenylalanine': ['UUU', 'UUC'],
        'Leucine': ['UUA', 'UUG'],
        'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
        'Tyrosine': ['UAU', 'UAC'],
        'Cysteine': ['UGU', 'UGC'],
        'Tryptophan': 'UGG',
        'STOP': ['UAA', 'UAG', 'UGA'],
}
    print("codon_list is ", codon_list)
    stop = False
    
    for codon in codon_list:
        if stop == True: break
        for protein in protein_codons_dict:
            if codon in protein_codons_dict[protein]:
                if protein == 'STOP':
                    stop = True
                    break
                else:
                    print('else!')
                    output.append(protein)

    print(output)
    return output