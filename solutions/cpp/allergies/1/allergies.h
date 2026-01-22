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
            int score{};
            allergy_test(int score_) {
                score = score_;
            }
        bool is_allergic_to(string ingredient) {
            std::unordered_set allergies = get_allergies();
            return allergies.find(ingredient) != allergies.end();
        }
        std::unordered_set<string> get_allergies() {
            vector<string> items = {"eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"};

            int items_size = static_cast<int>(items.size());
            int subtotal = score % static_cast<int>(std::pow(2, items_size));
            std::unordered_set<string> allergies = {};

            // check for each ingredient in items list
            for (int i = 0; i < items_size; ++i) {
                if (subtotal >= std::pow(2, (items_size - 1 - i))) {
                    allergies.insert(items[items_size - 1 - i]);
                    subtotal -= std::pow(2, (items_size - 1 - i));
                }
            }
            return allergies;
        }
    };
}  // namespace allergies

#endif // ALLERGIES_H