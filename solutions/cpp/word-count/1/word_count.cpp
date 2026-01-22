#include "word_count.h"

namespace word_count {
    map<string, int> words(string input) {
        map<string, int> output{};
        std::vector<std::string> results;
        string input_formatted = input;

        if (input_formatted[0] == '\'' && input_formatted[input_formatted.size() - 1] == '\'') {
            input_formatted = input.substr(1, input_formatted.size() - 2);
        }

        boost::split(results, input_formatted, boost::is_any_of("\t, \n:!&@$%^&."));

        for (const auto& word : results) {
            if (word != "" && word != "\'") {
                string word_lower{};
                for (int i = 0; i < static_cast<int>(word.size()); i++) {
                    if (word[i] == '\'' && i == 0) continue;
                    if (word[i] == '\'' && i == static_cast<int>(word.size()) - 1) continue;
                    word_lower += std::tolower(word[i]);
                }
                output[word_lower]++;                                    
            }
        }
        
        return output;
    }
}  // namespace word_count
