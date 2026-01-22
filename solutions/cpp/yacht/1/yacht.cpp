#include "yacht.h"

namespace yacht {

// TODO: add your solution here
    int score(vector<int> input, string category) {
        if (category == "yacht") {
            if (input[0] == input [1] &&
                input[1] == input [2] &&
                input[2] == input [3] &&
                input[3] == input [4]) {
                    return 50;
                }
        }
        if (category == "choice") {
            int sum{};
            for (int i : input) {
                sum += i;
            }
            return sum;
        }
        if (category == "big straight") {
            int sum{};
            for (int i : input) {
                if (i != 1) {
                    int count = std::count(input.begin(), input.end(), i);

                    if (count == 1) {
                        sum += i;
                    }
                }
            }

            if (sum == 20) {
                return 30;
            }
        }
        if (category == "little straight") {
            int sum{};
            for (int i : input) {
                if (i != 6) {
                    int count = std::count(input.begin(), input.end(), i);

                    if (count == 1) {
                        sum += i;
                    }
                }
            }

            if (sum == 15) {
                return 30;
            }
        }
        if (category == "four of a kind") {
            for (int i : input) {
                int count = std::count(input.begin(), input.end(), i);

                if (count >= 4) {
                    return 4 * i;
                }
            }
        }
        if (category == "full house") {
            int sum{};
            bool valid = true;

            for (int i : input) {
                int count = std::count(input.begin(), input.end(), i);

                if (count == 2 || count == 3) {
                    sum += i;
                } else {
                    valid = false;
                    break;
                }
            }

            if (valid == true) {
                return sum;
            }
        }
        if (category == "sixes") {
            int count{};
            
            for (int i :input) {
                if (i == 6) {
                    count += 1;
                }
            }
            return count * 6;
        }
        if (category == "fives") {
         int count{};
            
            for (int i :input) {
                if (i == 5) {
                    count += 1;
                }
            }
            return count * 5;
        }
        if (category == "fours") {
        int count{};
            
            for (int i :input) {
                if (i == 4) {
                    count += 1;
                }
            }
            return count * 4;
        }
        if (category == "threes") {
        int count{};
            
            for (int i :input) {
                if (i == 3) {
                    count += 1;
                }
            }
            return count * 3;
        }
        if (category == "twos") {
            int count{};
            
            for (int i :input) {
                if (i == 2) {
                    count += 1;
                }
            }
            return count * 2;
        }
        if (category == "ones") {
        int count{};
            
            for (int i :input) {
                if (i == 1) {
                    count += 1;
                }
            }
            return count;
        }
        return 0;
    }
}  // namespace yacht
