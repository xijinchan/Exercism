#pragma once

#include <vector>
#include <algorithm> 



using std::vector;

namespace knapsack {
        struct Item {
            Item(int weight_, int value_) {
                weight = weight_;
                value = value_;
            }
            int weight;
            int value;
            bool operator<(const Item& other) const {
                // Example: Sort by value-to-weight ratio (descending)
                // return (double)value / weight > (double)other.value / other.weight;
                // Or sort by value: return value < other.value;
                // Or sort by weight:
                return weight < other.weight;
            }
    };

    int maximum_value(int max_weight, vector<Item> items);

}  // namespace knapsack