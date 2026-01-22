#include "twelve_days.h"

namespace twelve_days {

// TODO: add your solution here
    string recite(int start, int end) {

        vector<string> items = {
            "a Partridge in a Pear Tree.\n",
            "two Turtle Doves, ",
            "three French Hens, ",
            "four Calling Birds, ",
            "five Gold Rings, ",
            "six Geese-a-Laying, ",
            "seven Swans-a-Swimming, ",
            "eight Maids-a-Milking, ",
            "nine Ladies Dancing, ",
            "ten Lords-a-Leaping, ",
            "eleven Pipers Piping, ",
            "twelve Drummers Drumming, "};

        vector<string> nths = {
            "first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
            };

        string recitation = "";

        for (int i = start - 1; i < end; i++) {
            recitation += "On the " + nths[i] + " day of Christmas my true love gave to me: ";
            if (i == 0) {
                recitation += items[0];
            } else {
                for (int k = i; k > -1; k--) {
                    if (k == 0) {
                        recitation += "and ";
                    }
                    recitation += items[k];
                }    
            }
            
            if (i < end - 1) {
                recitation += "\n";
            }
        }
        
        return recitation;
    }
}  // namespace twelve_days
