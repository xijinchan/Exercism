#include "food_chain.h"

namespace food_chain {
    vector<string> animals = {"fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"};
    vector<string> second_lines = {"I don\'t know why she swallowed the fly. Perhaps she\'ll die.\n",
        "It wriggled and jiggled and tickled inside her.\n",
        "How absurd to swallow a bird!\n",
        "Imagine that, to swallow a cat!\n",
        "What a hog, to swallow a dog!\n",
        "Just opened her throat and swallowed a goat!\n",
        "I don\'t know how she swallowed a cow!\n",
        "She\'s dead, of course!\n"
    };

    string middle_lines(string animal, int animal_index) {
        if (animal == "spider") {
            return "She swallowed the " + animals[animal_index+1] + " to catch the " + animal + " that wriggled and jiggled and tickled inside her.\n";
        } else {
            return "She swallowed the " + animals[animal_index+1] + " to catch the " + animal + ".\n";
        };
    }

    string verse(int number) {
        return verses(number, number);
    }

    string verses(int start, int end) {
        string output = "";
        for (int verse = start; verse <= end; verse++) {
            for (int animal_index = verse-1; animal_index >= 0; animal_index--) {
                string animal = animals[animal_index];
                if (animal_index == 7) {
                    output += "I know an old lady who swallowed a " + animal + ".\n";
                    output += second_lines[7];
                    break;
                }
                if (animal_index == verse-1) {
                    output += "I know an old lady who swallowed a " + animal + ".\n";
                } else if (animal_index == verse-2) {
                    output += second_lines[animal_index+1];
                    output += middle_lines(animal, animal_index);
                } else {
                    output += middle_lines(animal, animal_index);
                };

                if (animal_index == 0) output += second_lines[0];
                if (start != end and animal_index == 0) output += "\n";
            };
        };
        return output;
    }

    string sing() {
        return verses(1, 8);
    }
}  // namespace food_chain
