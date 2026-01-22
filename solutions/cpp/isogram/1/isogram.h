#if !defined(ISOGRAM_H)
#define ISOGRAM_H

#include <string>
#include <algorithm>
#include <cctype>

using std::string;

namespace isogram {
    bool is_isogram(string input) {
        string lowercased{};
        
        for (auto& c : input) {
            if ((64 < c && c < 91) || (96 < c && c < 123)) { // if A-Z or a-z
                lowercased += std::tolower(c);
            }
        }
        
        for (auto& c : lowercased) {
            if (std::count(lowercased.begin(), lowercased.end(), c) > 1) {
                return false;
            } else {
                continue;
            }
        }

        return true;
    }
}  // namespace isogram

#endif // ISOGRAM_H