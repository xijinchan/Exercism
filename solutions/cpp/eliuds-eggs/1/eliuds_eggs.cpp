#include "eliuds_eggs.h"

#include <string>
#include <bitset>

namespace chicken_coop {

// TODO: add your solution here
    int positions_to_quantity(int n) {
        std::bitset<32> binary(n);
        std::string binary_string = binary.to_string();

        int count{};

        for (char c : binary_string) {
            if (c == 49) {
            count += 1;
            }
        }

        return count;
    }
}  // namespace chicken_coop