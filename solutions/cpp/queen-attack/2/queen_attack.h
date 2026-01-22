#if !defined(QUEEN_ATTACK_H)
#define QUEEN_ATTACK_H
#include <stdexcept>
#include <cmath>

namespace queen_attack {
    class chess_board {
        public:
            std::pair<int, int> white_{};
            std::pair<int, int> black_{};
            chess_board(std::pair<int, int> white_new, std::pair<int, int> black_new);
            std::pair<int, int> white() const {return white_;};
            std::pair<int, int> black() const {return black_;};
            bool can_attack() const;
    };
}  // namespace queen_attack

#endif // QUEEN_ATTACK_H