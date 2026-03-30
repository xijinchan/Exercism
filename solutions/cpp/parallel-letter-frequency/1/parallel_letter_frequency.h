#pragma once

#include <string>
#include <vector>
#include <map>

using std::string;

namespace parallel_letter_frequency {
    std::map<char, int> frequency(std::vector<std::basic_string_view<char>> texts);
}