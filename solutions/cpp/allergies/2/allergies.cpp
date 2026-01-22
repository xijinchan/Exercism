#include "allergies.h"

namespace allergies {
    allergy_test::allergy_test(int score_) {
        score = score_;
    };

    bool allergy_test::is_allergic_to(string ingredient) {
        std::unordered_set allergies = allergy_test::get_allergies();
        return allergies.find(ingredient) != allergies.end();
    }

    std::unordered_set<string> allergy_test::get_allergies() {
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

}  // namespace allergies
