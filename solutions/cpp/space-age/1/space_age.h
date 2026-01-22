#if !defined(SPACE_AGE_H)
#define SPACE_AGE_H

namespace space_age {
    class space_age {
        public:
            double seconds_{};
            space_age(double seconds_new) {
                seconds_ = seconds_new;
            }
            double seconds() const {
                return seconds_;
            }
            double on_mercury() const {
                return seconds_ / 31557600 / 0.2408467;
            }
            double on_venus() const {
                return seconds_ / 31557600 / 0.61519726;
            }
            double on_earth() const {
                return seconds_ / 31557600;
            }
            double on_mars() const {
                return seconds_ / 31557600 / 1.8808158;
            }
            double on_jupiter() const {
                return seconds_ / 31557600 / 11.862615;
            }
            double on_saturn() const {
                return seconds_ / 31557600 / 29.447498;
            }
            double on_uranus() const {
                return seconds_ / 31557600 / 84.016846;
            }
            double on_neptune() const {
                return seconds_ / 31557600 / 164.79132;
            }
    };
}  // namespace space_age

#endif // SPACE_AGE_H