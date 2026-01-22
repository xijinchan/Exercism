// ERROR: FILE CORRUPTED. Please supply valid C++ Code.
#include <string>
#include <iostream>

#pragma once
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
            int age{};
            star_map::System system{};
            star_map::System current_system{};
            int generation{};
            int busters{};
            Vessel(std::string name_, int age_, star_map::System system_ = star_map::System::Sol, star_map::System current_system_ = star_map::System::Sol, int generation_ = 1) {
                name = name_;
                age = age_;
                system = system_;
                current_system = current_system_;
                generation = generation_;
            }
            heaven::Vessel replicate(std::string name_) {
                return Vessel(name_, 1, star_map::System::Sol, star_map::System::Sol, 2);
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
        if (vessel_1.age > vessel_2.age) {
            // isn't the other vessel older?.. don't get this test
            return vessel_2.name;
            }
        return vessel_1.name;
    }
    bool in_the_same_system(heaven::Vessel vessel_1, heaven::Vessel vessel_2) {
        if (vessel_1.system == vessel_2.system) {
            return true;
        }
        return false;
    }
}

// hp1,üapöhp2ö%Äcountöiöma1,öhp2ö%Älawöhp3öö/önextöstepö%Ädacöiöml1ö%Älawö7ö%Ädacöiömb1ö%Ärandomöö%Äscrö9sö%Äsirö9sö%Äxctöhr1ö%Äaddöiömx1ö%Ädacöiömx1ö%Äswapö%Äaddöiömy1ö%Ädacöiömy1ö%Ärandomö%Äscrö9sö%Äsirö9sö%Äxctöhr2ö%Ädacöiömdyö%Ädioöiömdxö%Äsetupö.hpt,3ö%Älacöranö%Ädacöiömth
