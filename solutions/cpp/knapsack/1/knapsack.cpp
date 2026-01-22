#include "knapsack.h"

namespace knapsack {

    template<typename T>
    void generateSubsets(const vector<T>& items, int index, vector<T>& current, int max_weight, int weight_sum, int value_sum, int& value_highest) {
        if (index == static_cast<int>(items.size())) {
            if (weight_sum <= max_weight) {
                value_highest = std::max(value_highest, value_sum);
            }
            return;
        }
    
        // Exclude current item
        generateSubsets(items, index + 1, current, max_weight, weight_sum, value_sum, value_highest);
    
        // Include current item — only if it doesn't exceed weight
        int new_weight = weight_sum + items[index].weight;
        if (new_weight <= max_weight) {
            current.push_back(items[index]);
            generateSubsets(items, index + 1, current, max_weight, new_weight, value_sum + items[index].value, value_highest);
            current.pop_back();  // Always safe: only reached if we included
        }
        // If too heavy, just skip — no need to pop or undo
    }
    
    template<typename T>
    int generatePowerSetRecursive(const vector<T>& items, int max_weight) {
        vector<T> current;
        int value_highest = 0;
        generateSubsets(items, 0, current, max_weight, 0, 0, value_highest);
        return value_highest;
    }
    
    int maximum_value(int max_weight, vector<Item> items) {
        if (items.empty()) return 0;
        return generatePowerSetRecursive(items, max_weight);
    }

}  // namespace knapsack