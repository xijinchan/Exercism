#include "matching_brackets.h"

namespace matching_brackets {
    bool check(string input) {
        string brackets_open = "([{";
        string brackets_close = ")]}";
        vector<char> brackets_vector{};
        int brackets_vector_index = 0;
        std::map<char, char> brackets_map = {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'}
        };
        
        for (char c : input) {
            if (brackets_open.find(c) != std::string::npos) {
                brackets_vector.push_back(c);
                brackets_vector_index += 1;
            } else if (brackets_close.find(c) != std::string::npos) {
                if (brackets_vector_index == 0) return false; // if opens with closing bracket
                brackets_vector_index -= 1;
                if (c == brackets_map[brackets_vector[brackets_vector_index]]) { // if matching bracket
                    auto it = brackets_vector.begin() + brackets_vector_index;
                    brackets_vector.erase(it);
                } else {
                    return false;
                }
            }
        }

        if (brackets_vector.size() == 0) {
            return true;
        } else {
            return false;
        }
    }
}  // namespace matching_brackets
