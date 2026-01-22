namespace targets {
// TODO: Insert the code for the alien class here
    class Alien {
        public:
            int x_coordinate{};
            int y_coordinate{};
            Alien(int x_coordinate_new, int y_coordinate_new){
                x_coordinate = x_coordinate_new;
                y_coordinate = y_coordinate_new;
            }
            int get_health() {
                return health;
            }
            bool hit() {
                if (health > 0) {
                    --health;
                }
                return true;
            }
            bool is_alive() {
                return health > 0;
            }
            bool teleport(int x_coordinate_new, int y_coordinate_new) {
                x_coordinate = x_coordinate_new;
                y_coordinate = y_coordinate_new;
                return true;
            }
            bool collision_detection(targets::Alien alien_2) {
                return x_coordinate == alien_2.x_coordinate && y_coordinate == alien_2.y_coordinate;
            }
        private:
            int health{3};
    };
}  // namespace targets