#if !defined(QUEEN_ATTACK_H)
#define QUEEN_ATTACK_H
#include <stdexcept>
#include <cmath>

namespace queen_attack {
    class chess_board {
        public:
            std::pair<int, int> white_{};
            std::pair<int, int> black_{};
            chess_board(std::pair<int, int> white_new, std::pair<int, int> black_new) {
                if (white_new.first < 0 or white_new.first > 7 or white_new.second < 0 or white_new.second > 7 or
                    black_new.first < 0 or black_new.first > 7 or black_new.second < 0 or black_new.second > 7 or
                    white_new == black_new)
                    {
                        throw std::domain_error("invalid coordinates");
                    }
                white_ = white_new;
                black_ = black_new;
            }
            std::pair<int, int> white() const {
                return white_;
            }
            std::pair<int, int> black() const {
                return black_;
            }
            bool can_attack() const {
                if (white_.first == black_.first) return true;
                if (white_.second == black_.second) return true;
                
                std::pair<int, int> diagonal_UR{};
                std::pair<int, int> diagonal_DR{};
                std::pair<int, int> diagonal_UL{};
                std::pair<int, int> diagonal_DL{};

                for (int i = 1; i <= 8; ++i) {
                    diagonal_UR = {white_.first + i, white_.second + i};
                    if (diagonal_UR == black_) return true;
                
                    diagonal_DR = {white_.first + i, white_.second - i};
                    if (diagonal_DR == black_) return true;

                    diagonal_UL = {white_.first - i, white_.second + i};
                    if (diagonal_UL == black_) return true;

                    diagonal_DL = {white_.first - i, white_.second - i};
                    if (diagonal_DL == black_) return true;
                }

                return false;
            }
    };
    
}  // namespace queen_attack

#endif // QUEEN_ATTACK_H