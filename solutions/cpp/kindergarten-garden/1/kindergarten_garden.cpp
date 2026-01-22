#include "kindergarten_garden.h"

namespace kindergarten_garden {

// TODO: add your solution here
    std::array<Plants, 4> plants(string layout, string student) {

        std::array<string, 12> students = {"Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"};
        std::map<string, Plants> plants_key;

        plants_key["C"] = Plants::clover;
        plants_key["G"] = Plants::grass;
        plants_key["V"] = Plants::violets;
        plants_key["R"] = Plants::radishes;
        
        auto student_number = std::find(students.begin(), students.end(), student);
        int index{};
        
        if (student_number != students.end()) {
            index = std::distance(students.begin(), student_number);
        }

        int char_index{};
        std::array<Plants, 4> output{};
        int output_index = 0;
        for (char c : layout) {
            if (char_index == index * 2 || char_index == (index * 2) + 1) {
                string s(1, c);
                
                output[output_index] = plants_key[s];
                output_index += 1;
            }
            if (c == '\n') {
                char_index = 0;
            } else {
                char_index += 1;
            }
        }
        
        return output;
    }
}  // namespace kindergarten_garden
