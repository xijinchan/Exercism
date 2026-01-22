#include "speedywagon.h"

namespace speedywagon {

// Enter your code below:

// Please don't change the interface of the uv_light_heuristic function
int uv_light_heuristic(std::vector<int>* data_array) {
    double avg{};
    for (auto element : *data_array) {
        avg += element;
    }
    avg /= data_array->size();
    int uv_index{};
    for (auto element : *data_array) {
        if (element > avg) ++uv_index;
    }
    return uv_index;
}

bool connection_check(pillar_men_sensor* sensor) {
    if (sensor == nullptr) { return false;}
    return true;
}

int activity_counter(pillar_men_sensor* sensor, int array_capacity) {
    if (connection_check(sensor) == false) { return false;}

    int activity = sensor->activity;

    if (array_capacity > 1) {
        for (int i = 1; i < array_capacity; i++) {
            pillar_men_sensor* next_element(sensor + i);
            activity += next_element->activity;
        }        
    }
        
    return activity;
}

bool alarm_control(pillar_men_sensor* sensor) {
    if (connection_check(sensor) == false) { return false;}

    if (sensor->activity > 0) {return true;}
    return false;
}

bool uv_alarm(pillar_men_sensor* sensor) {
    if (connection_check(sensor) == false) { return false;}

    std::vector<int>* data_{&sensor->data};

    if (uv_light_heuristic(data_) > sensor->activity) {
        return true;
    }

    return false;
}

}  // namespace speedywagon
