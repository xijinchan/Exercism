// #if !defined(LEAP_H)
// #define LEAP_H
#pragma once
namespace leap {
    bool is_leap_year(int year) {
        if (year % 4 == 0) {
            if (year % 100 == 0) {
                if (year % 400 == 0) {
                    return true;
                }
                return false;
            }
        return true;
        }
        return false;
    }
}  // namespace leap

// #endif // LEAP_H