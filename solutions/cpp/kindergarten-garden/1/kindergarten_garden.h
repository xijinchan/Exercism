#pragma once

#include <string>
#include <array>
#include <algorithm>
#include <map>

using std::string;

namespace kindergarten_garden {
    enum Plants {
        clover,
        grass,
        violets,
        radishes
    };
// TODO: add your solution here
    std::array<Plants, 4> plants(string layout, string student);
}  // namespace kindergarten_garden
