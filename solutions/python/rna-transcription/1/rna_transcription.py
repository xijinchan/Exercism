def to_rna(dna_strand):
    rna_compliment = ''

    for letter in dna_strand:
        match letter:
            case 'G':
                rna_compliment += 'C'
            case 'C':
                rna_compliment += 'G'
            case 'T':
                rna_compliment += 'A'
            case 'A':
                rna_compliment += 'U'

    return rna_compliment
