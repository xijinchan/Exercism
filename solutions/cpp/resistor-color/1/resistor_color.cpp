#include "resistor_color.h"

#include <stdexcept>

namespace resistor_color {

// TODO: add your solution here
    std::vector<string> color_values = {
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"
    };
    
    int color_code(string input) {
        auto it = std::find(color_values.begin(), color_values.end(), input);
        if (it != color_values.end()) {
            return std::distance(color_values.begin(), it);
        }
        throw std::out_of_range("Color Not Found");
    }

    std::vector<string> colors() {
        return color_values;
    }
}  // namespace resistor_color
