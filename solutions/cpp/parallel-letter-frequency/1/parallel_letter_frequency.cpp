#include "parallel_letter_frequency.h"

#include <thread>
#include <vector>
#include <map>
#include <cctype>

namespace parallel_letter_frequency {

    void count_letters(const std::vector<std::basic_string_view<char>>& texts, std::vector<std::map<char, int>>& partial_results, int index) {
        std::map<char, int> local_count;
        
        for (char c : texts[index]) {
            if (std::isalpha(static_cast<unsigned char>(c))) {
                char lower = std::tolower(static_cast<unsigned char>(c));
                local_count[lower]++;
            }
        }

        partial_results[index] = std::move(local_count);
    }

    std::map<char, int> frequency(std::vector<std::basic_string_view<char>> texts)
    {
        std::map<char, int> result;
    
        if (texts.empty()) return result;
    
        std::vector<std::thread> threads;
        std::vector<std::map<char, int>> partial_results(texts.size());
    
        // Launch threads
        for (size_t i = 0; i < texts.size(); ++i) {
            threads.emplace_back(count_letters, std::cref(texts), std::ref(partial_results), i);
        }
    
        // Wait for all threads to finish
        for (auto& t : threads) {
            t.join();
        }
    
        // merge all partial_results into 'result'
        for (const auto& partial : partial_results) {
            for (const auto& [letter, count] : partial) {
                result[letter] += count;
            }
        }
    
        return result;
    }
}