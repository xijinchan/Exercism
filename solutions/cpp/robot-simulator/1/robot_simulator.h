#if !defined(ROBOT_SIMULATOR_H)
#define ROBOT_SIMULATOR_H

#include <utility>
#include <string>

namespace robot_simulator {

    enum Bearing {
        NORTH,
        EAST,
        SOUTH,
        WEST,
    };
    
    class Robot {
        private:
            std::pair<int, int> position;
            robot_simulator::Bearing bearing;
            Bearing bearings_list[4] = {NORTH, EAST, SOUTH, WEST};
        public:
            Robot(std::pair<int, int> robot_position, robot_simulator::Bearing robot_bearing) {
                position = robot_position;
                bearing = robot_bearing;
            }
            Robot() {}
            std::pair<int, int> get_position() const {
                return position;
            }
            Bearing get_bearing() const {
                return bearing;
            }
            void turn_right() {
                for (int i = 0; i < 4; i++) {
                    if (bearings_list[i] == bearing) {
                        bearing = bearings_list[(i + 1) % 4];
                        break;
                    }
                }
            }
            void turn_left() {
                for (int i = 0; i < 4; i++) {
                    if (bearings_list[i] == bearing) {
                        bearing = bearings_list[((((i - 1) % 4) + 4) % 4)];
                        break;
                    }
                }
            }
            void advance() {
                if (bearing == NORTH) { position.second += 1;}
                if (bearing == EAST) { position.first += 1;}
                if (bearing == SOUTH) { position.second -= 1;}
                if (bearing == WEST) { position.first -= 1;}
            }
            void execute_sequence(std::string sequence) {
                for (auto c : sequence) {
                    if (c == 'A') { advance();}
                    if (c == 'L') { turn_left();}
                    if (c == 'R') { turn_right();}
                }
            }
    };
}  // namespace robot_simulator

#endif // ROBOT_SIMULATOR_H