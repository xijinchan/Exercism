#pragma once

#include <random>
#include <ctime>
#include <algorithm>
#include <cmath>

namespace dnd_character {
    int roll_dice();
    int modifier(int input);
    int ability();

    class Character {
        public:
            Character() {
                strength = roll_dice();
                dexterity = roll_dice();
                constitution = roll_dice();
                intelligence = roll_dice();
                wisdom = roll_dice();
                charisma = roll_dice();
                hitpoints = 10 + ((constitution - 10) / 2);
            }
            int strength{};
            int dexterity{};
            int constitution{};
            int intelligence{};
            int wisdom{};
            int charisma{};
            int hitpoints{};
    };

// TODO: add your solution here
}  // namespace dnd_character
