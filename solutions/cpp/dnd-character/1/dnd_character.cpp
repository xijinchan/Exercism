#include "dnd_character.h"

namespace dnd_character {

// TODO: add your solution here
    int roll_dice() {
        static std::mt19937 rng(static_cast<unsigned>(std::time(nullptr)));
        std::uniform_int_distribution<int> dice(1, 6);

        int rolls[4] = {dice(rng), dice(rng), dice(rng), dice(rng)};
        std::sort(rolls, rolls + 4, std::greater<int>());
        return rolls[0] + rolls[1] + rolls[2]; // Sum top 3
    }
    
    int modifier(int input) {
        double input_double = input;
        return std::floor((input_double - 10) / 2);
    }
    
    int ability() {
        return roll_dice();
    }
}  // namespace dnd_character
