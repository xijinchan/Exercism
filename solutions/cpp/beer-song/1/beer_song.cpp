#include "beer_song.h"

namespace beer_song {
    string verse(int no_of_bottles) {
        string output{};
            
        vector<string> phrase_1 = {" bottle of beer on the wall", " bottles of beer on the wall"};
        vector<string> phrase_2 = {"Go to the store and buy some more, ", "Take it down and pass it around, ", "Take one down and pass it around, "};

        if (no_of_bottles > 1) {
            output = output + std::to_string(no_of_bottles) + phrase_1[1] + ", " + std::to_string(no_of_bottles) + phrase_1[1].substr(0, 16) + ".\n" + phrase_2[2];
        } else if (no_of_bottles == 1) {
            output = output + std::to_string(no_of_bottles) + phrase_1[0] + ", " + std::to_string(no_of_bottles) + phrase_1[0].substr(0, 15) + ".\n" + phrase_2[1];
        } else {
            output = output + "No more" + phrase_1[1] + ", " + "no more" + phrase_1[1].substr(0,16) + ".\n" + phrase_2[0] + "99" + phrase_1[1] + ".\n";
            return output;
        }

        no_of_bottles -= 1;
        
        if (no_of_bottles > 1) {
            output = output + std::to_string(no_of_bottles) + phrase_1[1] + ".\n";
        } else if (no_of_bottles == 1) {
            output = output + std::to_string(no_of_bottles) + phrase_1[0] + ".\n";
        } else {
            output = output + "no more" + phrase_1[1] + ".\n";
        }
        
        return output;
    }

    string sing(int start_verse, int end_verse) {
        string output{};
        for (int i = start_verse; i >= end_verse; --i) {
            output += verse(i);
            if (i > end_verse) {
                output += "\n";
            }
        }

        return output;
    }
}  // namespace beer_song
