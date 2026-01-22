#if !defined(CLOCK_H)
#define CLOCK_H
#include <string>
#include <vector>

using std::string;

namespace date_independent {
    class clock {
        private:
            clock(int hour_new, int min_new);
            int hour{};
            int min{};
        public:
            static clock at(int hour_new, int min_new);
            std::pair<int, int> cycle(int hour_, int min_);
            operator string() const;
            bool operator==(const clock& other_clock) const;
            bool operator!=(const clock& other_clock) const;
            clock& plus(int& mins);
            clock& cycle();
    };
}  // namespace date_independent

#endif // CLOCK_H