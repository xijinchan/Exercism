#pragma once

#include <string>
#include <memory>

namespace troy {

struct artifact {
    // constructors needed (until C++20)
    artifact(std::string name) : name(name) {}
    std::string name;
};

struct power {
    // constructors needed (until C++20)
    power(std::string effect) : effect(effect) {}
    std::string effect;
};

struct human {
    std::unique_ptr<artifact> possession;
    std::shared_ptr<power> own_power;
    std::shared_ptr<power> influenced_by;
};

void give_new_artifact(human& human_, std::string artifact_name);
void exchange_artifacts(std::unique_ptr<artifact>& human_1_possession, std::unique_ptr<artifact>& human_2_possession);
void manifest_power(human& human_, std::string new_power_);
void use_power(human& caster, human& target);
int power_intensity(human& human);

}  // namespace troy
