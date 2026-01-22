#include "high_scores.h"

#include <algorithm>

namespace arcade {

std::vector<int> HighScores::list_scores() {
    // TODO: Return all scores for this session.
    return scores;
}

int HighScores::latest_score() {
    // TODO: Return the latest score for this session.
    return scores.back();
}

int HighScores::personal_best() {
    // TODO: Return the highest score for this session.
    return *std::max_element(scores.begin(), scores.end());
}

std::vector<int> HighScores::top_three() {
    // TODO: Return the top 3 scores for this session in descending order.
    int m1{0}, m2{0}, m3{0};
    
    for (int i = 0; i < static_cast<int>(scores.size()); i++) {
        if (scores[i] > m1) {
            m3 = m2;
            m2 = m1;
            m1 = scores[i];
        } else if (scores[i] > m2) {
            m3 = m2;
            m2 = scores[i];
        } else if (scores[i] > m3) {
            m3 = scores[i];
        }
    }

    if (scores.size() == 2) {
        return {m1, m2};
    }
    if (scores.size() == 1) {
        return {m1};
    }
    return {m1, m2, m3};
}

}  // namespace arcade
