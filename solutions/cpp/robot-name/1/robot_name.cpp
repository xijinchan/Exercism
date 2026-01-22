#include "robot_name.h"

namespace robot_name {
    std::unordered_set<string> existing_names;

    robot::robot() {
        name_ = generate_unique_name();
    }

    string robot::name() const {
        return name_;
    }

    void robot::reset() {
        name_ = generate_unique_name();
    }

    string robot::generate_unique_name() {
        string new_name = generate_name();

        // redo new_name while name already taken
        while (existing_names.count(new_name) > 0) {
            new_name = generate_name();
        }
        existing_names.insert(new_name);
        
        return new_name;
    }

    string robot::generate_name() {
        char random_letter_1 = static_cast<char>('A' + rand() % 26);
        char random_letter_2 = static_cast<char>('A' + rand() % 26);
        string random_numbers = std::to_string(rand() % 999);

        if (random_numbers.length() < 2) random_numbers = "00" + random_numbers;
        if (random_numbers.length() < 3) random_numbers = "0" + random_numbers;

        string output{};

        output += random_letter_1;
        output += random_letter_2;
        output += random_numbers;
        
        return output;
    }

}  // namespace robot_name
