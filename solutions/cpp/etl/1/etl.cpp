#include "etl.h"

namespace etl {
    std::map<char, int> transform(std::map<int, std::vector<char>> old) {
        std::map<char, int> output{};

        int points{};
        for (auto kv : old) {
            points = static_cast<int>(kv.first);
            for (char c : kv.second) {
                output.insert({std::tolower(c), points});
            }
        }

        return output;
    }
}  // namespace etl
