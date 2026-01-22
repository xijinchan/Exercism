#include "rna_transcription.h"
#include <stdexcept>

namespace rna_transcription {
    char to_rna(char char_) {
        switch (char_) {
            case 'C':
                return  'G';
            case 'G':
                return  'C';
            case 'A':
                return  'U';
            case 'T':
                return  'A';
            default:
                throw std::invalid_argument("Invalid chain");
        }
    }

    string to_rna(string chain) {
        string rna = "";
        for (int i = 0; i < static_cast<int>(chain.size()); ++i) {
            switch (chain[i]) {
                case 'C':
                    rna += 'G';
                    break;
                case 'G':
                    rna += 'C';
                    break;
                case 'A':
                    rna += 'U';
                    break;
                case 'T':
                    rna += 'A';
                    break;
                default:
                    throw std::invalid_argument("Invalid chain");
            }
        }
        return rna;
    }

}  // namespace rna_transcription
