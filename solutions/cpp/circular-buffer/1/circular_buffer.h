#if !defined(CIRCULAR_BUFFER_H)
#define CIRCULAR_BUFFER_H

#include <vector>
#include <stdexcept>

namespace circular_buffer {
    template <typename T>
    class circular_buffer {
        private:
            std::vector<T> buffer{};
            int write_head = 0;
            int overwrite_head = 0;
            int read_head = 0;
            int buffer_item_count = 0;
        public:
            circular_buffer(int size){
                buffer.resize(size);
            }
            T read(){
                if (buffer.size() == 0 || buffer_item_count == 0) {
                    throw std::domain_error("Error");
                }
                T output = buffer[read_head];
                buffer_item_count -= 1;
                read_head = (read_head + 1) % buffer.size();
                overwrite_head = (overwrite_head + 1) % buffer.size();
                return output;
            }
            void write(T input){
                if (static_cast<int>(buffer.size()) == buffer_item_count) {
                    throw std::domain_error("Buffer Full");
                }
                buffer[write_head] = input;
                write_head = (write_head + 1) % buffer.size();
                buffer_item_count += 1;
            }
            void clear(){
                buffer_item_count = 0;
                write_head = 0;
                read_head = 0;
                overwrite_head = 0;
            }
            void overwrite(T input){
                if (static_cast<int>(buffer.size()) != buffer_item_count) {
                    write(input);
                } else {
                    buffer[overwrite_head] = input;
                    overwrite_head = (overwrite_head + 1) % buffer.size();
                    read_head = (read_head + 1) % buffer.size();
                }
            }
    };
}  // namespace circular_buffer

#endif // CIRCULAR_BUFFER_Ha