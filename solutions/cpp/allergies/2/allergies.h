#if !defined(ALLERGIES_H)
#define ALLERGIES_H
#include <unordered_set>
#include <string>
#include <vector>
#include <cmath>

using std::string;
using std::vector;

namespace allergies {
    class allergy_test {
        public:
            allergy_test(int score_);
            int score{};
        bool is_allergic_to(string ingredient);
        std::unordered_set<string> get_allergies();
    };
}  // namespace allergies

#endif // ALLERGIES_H