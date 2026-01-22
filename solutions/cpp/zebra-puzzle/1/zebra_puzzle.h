#pragma once

#include <string>
#include <vector>
#include <algorithm>

using std::vector;

namespace zebra_puzzle {
    
    struct Solution {
        std::string drinksWater;
        std::string ownsZebra;
    };

    struct Person {
        std::string nationality;
        std::string animal;
        std::string drink;  
        std::string hobbie;
    };

    struct House {
        Person* person;
        int position;
    };
    
    Solution solve();
    bool check_constraints(Person& p1, Person& p2, Person& p3, Person& p4, Person& p5, House& red, House& ivory, House& green, House& yellow, House& blue);
}  // namespace zebra_puzzle
