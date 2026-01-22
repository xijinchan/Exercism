#if !defined(ROBOT_NAME_H)
#define ROBOT_NAME_H
#include <string>
#include <unordered_set>
#include <random>

using std::string;
using std::vector;

namespace robot_name {
    class robot {
        public:
            robot();
            string name_{};
            string name() const;
            void reset();
            string generate_unique_name();
            string generate_name();
    };
}  // namespace robot_name

#endif // ROBOT_NAME_H