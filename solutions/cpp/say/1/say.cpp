#include "say.h"

namespace say {
    std::string in_english(long long unsigned int number_) {
        if (number_ >= 1000000000000) {
            throw std::domain_error("number out of bounds");
        }
        if (number_ == 0) return "zero";

        long long unsigned int number = number_;
        std::string output{};

        // billions
        if (number > 999999999) {
            int chunk_billions = (number % 1000000000000) / 1000000000;
            output += say::convert_chunk(chunk_billions) + " billion";
            if (number % 1000000000 != 0) output += " ";
        }
        
        // millions
        if (number % 10000000 > 999999) {
            int chunk_millions = (number % 1000000000) / 1000000;
            output += say::convert_chunk(chunk_millions) + " million";
            if (number % 1000000 != 0) output += " ";
        }
        
        // thousands
        if (number % 10000 > 999) {
            int chunk_thousands = (number % 1000000) / 1000;
            output += say::convert_chunk(chunk_thousands) + " thousand";
            if (number % 1000 != 0) output += " ";
        }

        // < 1000
        output += say::convert_chunk(number % 1000);
        
        return output;
    }

        std::string convert_chunk(int number) {
            
            std::vector<std::string> under_20 = {
            "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
            std::vector<std::string> tens = {"", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
            
            std::string chunk_string{};
            // hundreds
            if (number % 1000 > 99) {
                chunk_string += under_20[(number % 1000) / 100] + " hundred";
                if (number % 100 != 0) chunk_string += " ";
            }
            
            // right 2 digits
            if ((number % 100) < 20) {
                chunk_string += under_20[number % 100];
            } else {
                if (19 < (number % 100) and (number % 100) < 100) chunk_string += tens[(number % 100) / 10];
                number = number % 10; // need this truncation or errors
                if (number % 10 != 0) chunk_string += "-" + under_20[number];
            }

            return chunk_string;
        }

}  // namespace say
