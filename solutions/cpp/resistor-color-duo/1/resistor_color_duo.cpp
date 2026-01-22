#include "resistor_color_duo.h"

#include <iostream>

namespace resistor_color_duo {

// TODO: add your solution here
    int value(std::vector<string> input) {
        std::map<std::string, int> colorMap = {
            {"black", 0},
            {"brown", 1},
            {"red", 2},
            {"orange", 3},
            {"yellow", 4},
            {"green", 5},
            {"blue", 6},
            {"violet", 7},
            {"grey", 8},
            {"white", 9}
        };

        string output{};
        
        for (int i = 0; i < 2; i++) {
            output += std::to_string(colorMap[input[i]]);
        }

        return std::stoi(output);
    };
}  // namespace resistor_color_duo
