#if !defined(SCRABBLE_SCORE_H)
#define SCRABBLE_SCORE_H

#include <map>
#include <string>

using std::string;

namespace scrabble_score {
    int score(string word){
        std::map<char, int> score_map = {
            {'A', 1}, {'E', 1}, {'I', 1}, {'O', 1}, {'U', 1}, {'L', 1}, {'N', 1}, {'R', 1}, {'S', 1}, {'T', 1},
            {'D', 2}, {'G', 2},
            {'B', 3}, {'C', 3}, {'M', 3}, {'P', 3},
            {'F', 4}, {'H', 4}, {'V', 4}, {'W', 4}, {'Y', 4},
            {'K', 5},
            {'J', 8}, {'X', 8},
            {'Q', 10}, {'Z', 10},
        };

        int score{};
        for (auto& c : word) {
            if (c > 96) { // if lower_case, make upper_case
                score += score_map[c - 32];
            } else {
                score += score_map[c];
            }
        }
        
        return score;
    }
}  // namespace scrabble_score

#endif // SCRABBLE_SCORE_H