#include "clock.h"

namespace date_independent {
    clock::clock(int hour_new, int min_new) {
        std::pair<int, int> time_cycled{};
        
        time_cycled = cycle(hour_new, min_new);
        hour = time_cycled.first;
        min = time_cycled.second;
    };

    std::pair<int, int> clock::cycle(int hour_, int min_) {
        int min_cycled{};
        int hour_cycled{};
        int hour_adjust{};

        if (min_ < 0) {
            min_cycled = (min_ + (60 * ((min_ / -60) + 1))) % 60;
            hour_adjust = ((min_ / -60) + 1);
        } else {
            min_cycled = min_;
        }

        hour_cycled = hour_ - hour_adjust;
        
        if (hour_cycled < 0) {
            hour_cycled = ((hour_cycled + (24 * ((hour_cycled / -24) + 1)))) % 24;
        }
        
        hour_ = (hour_cycled + (min_cycled / 60)) % 24;
        min_ = min_cycled % 60;

        return std::make_pair(hour_, min_);
    };

    clock clock::at(int hour_new, int min_new) {
        return clock(hour_new, min_new);
    };

    clock::operator string() const {
        string output{};
        
        if (hour < 10) {
            output = "0" + std::to_string(hour) + ":";
        } else {
            output = std::to_string(hour) + ":";
        }
        if (min < 10) {
            output = output + "0" + std::to_string(min);
        } else {
            output = output + std::to_string(min);  
        }
        return output;
    }

    clock& clock::plus(int& mins_add) {
        std::pair<int, int> time_cycled{};
        
        time_cycled = cycle(hour, min + mins_add);
        hour = time_cycled.first;
        min = time_cycled.second;
        return *this;
    }

    bool clock::operator==(const clock& other_clock) const {
        return (hour == other_clock.hour and min == other_clock.min);
    }

    bool clock::operator!=(const clock& other_clock) const {
        return (hour != other_clock.hour or min != other_clock.min);
    }
}  // namespace date_independent