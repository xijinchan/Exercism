#include "two_fer.h"

namespace two_fer
{
    std::string two_fer(std::string name) {
        std::string name_one {};
        
        if (name == "") {
            name_one = "you";
        } else {
            name_one = name;
        }

        std::string output = "One for " + name_one + ", one for me.";
        return output;
    }
} // namespace two_fer

