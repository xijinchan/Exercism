#include "protein_translation.h"

namespace protein_translation {
    vector<string> proteins(string input) {
        std::map<string, string> codons_map = {
            {"AUG", "Methionine"},
            {"UUU", "Phenylalanine"}, {"UUC", "Phenylalanine"},
            {"UUA", "Leucine"}, {"UUG", "Leucine"},
            {"UCU", "Serine"}, {"UCC", "Serine"}, {"UCA", "Serine"}, {"UCG", "Serine"},
            {"UAU", "Tyrosine"}, {"UAC", "Tyrosine"},
            {"UGU", "Cysteine"}, {"UGC", "Cysteine"},
            {"UGG", "Tryptophan"},
            {"UAA", "STOP"}, {"UAG", "STOP"}, {"UGA", "STOP"}
        };

        string codon = {};
        string protein = {};
        vector<string> output = {};

        for (unsigned long i = 0; i < (input.length() / 3); ++i) {
            codon = input.substr(3 * i, 3);
            protein = codons_map[codon];
            if (protein == "STOP") break;
            output.push_back(protein);
        }
        return output;
    }
}  // namespace protein_translation
