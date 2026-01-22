#include "anagram.h"

namespace anagram {
    anagram::anagram(string input) {
        string input_lower{};
        for (char c : input) {
            input_lower += std::tolower(c);
        }
        target = input_lower;
    }
    vector<string> anagram::matches(vector<string> candidates) {
        vector<string> output{};
        
        for (auto element : candidates) {
            bool is_anagram = true;
            
            if (element.size() != target.size()) {
                continue;
            }

            string candidate_lower{};
            
            for (char c : element) {
                char c_lower = std::tolower(c);
                candidate_lower += c_lower;
                
                int count_candidate = std::count(element.begin(), element.end(), c);
                int count_target = std::count(target.begin(), target.end(), c_lower);
                
                if (target.find(c_lower) == string::npos || count_candidate != count_target || candidate_lower == target) {
                    is_anagram = false;
                    break;
                } else {
                    continue;
                }
            }

            if (is_anagram == true) {
                output.push_back(element);
            }
        }
        
        return output;
    }
}  // namespace anagram
