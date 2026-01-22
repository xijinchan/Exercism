#pragma once
#include <string>

namespace star_map {
    enum class System {
        EpsilonEridani,
        BetaHydri,
        Sol,
        AlphaCentauri,
        DeltaEridani,
        Omicron2Eridani
    };
}

namespace heaven {
    class Vessel {
        private:
        public:
            std::string name{};
            int generation{};
            star_map::System current_system{};
            int busters{};
            Vessel(std::string name_, int generation_, star_map::System current_system_ = star_map::System::Sol) {
                name = name_;
                generation = generation_;
                current_system = current_system_;
            }
            heaven::Vessel replicate(std::string name_) {
                return Vessel(name_, generation + 1, current_system);
            }
            void make_buster() {
                ++busters;
            }
            bool shoot_buster() {
                if (busters > 0) {
                    --busters;
                    return true;
                }
                return false;
            }
    };
    std::string get_older_bob(heaven::Vessel vessel_1, heaven::Vessel vessel_2) {
        if (vessel_1.generation > vessel_2.generation) {
            return vessel_2.name;
            }
        return vessel_1.name;
    }
    bool in_the_same_system(heaven::Vessel vessel_1, heaven::Vessel vessel_2) {
        if (vessel_1.current_system == vessel_2.current_system) {
            return true;
        }
        return false;
    }
}
