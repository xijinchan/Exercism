#if !defined(ANAGRAM_H)
#define ANAGRAM_H

#include <string>
#include <vector>
#include <algorithm>

using std::string;
using std::vector;

namespace anagram {
    class anagram {
        private:
            string target{};
            vector<string> anagrams{};
        public:
            anagram(string input);
            vector<string> matches(vector<string> candidates);
    };
}  // namespace anagram

#endif // ANAGRAM_H