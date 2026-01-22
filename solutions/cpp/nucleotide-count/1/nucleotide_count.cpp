#include "nucleotide_count.h"

namespace nucleotide_count {
    std::map<char, int> count(string chain) {
        int A_count = 0;
        int C_count = 0;
        int G_count = 0;
        int T_count = 0;

        for (int i = 0; i < static_cast<int>(chain.size()); ++i) {
            switch (chain[i]) {
                case 'A':
                    ++A_count;
                    break;
                case 'C':
                    ++C_count;
                    break;
                case 'G':
                    ++G_count;
                    break;
                case 'T':
                    ++T_count;
                    break;
                default:
                    throw std::invalid_argument("invalid chain");
                    break;
            }
        }

        std::map<char, int> results = {
            {'A', A_count},
            {'C', C_count},
            {'G', G_count},
            {'T', T_count}
        };

        return results;
    }
}  // namespace nucleotide_count
