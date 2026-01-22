#if !defined(BINARY_SEARCH_TREE_H)
#define BINARY_SEARCH_TREE_H

#include <vector>
#include <memory>

using std::vector;

namespace binary_search_tree {
    template <typename T>
    class binary_tree {
        using tree_ptr = typename std::unique_ptr<binary_tree<T>>;
    
        private:
            T data_{};
            tree_ptr left_{};
            tree_ptr right_{};
            binary_tree<T>* parent_{};
        public:
            binary_tree(T data) {
                data_ = data;
            }

            binary_tree(T data, binary_tree* parent) {
                data_ = data;
                parent_ = parent;
            }
                
            T& data() {
                return data_;
            }
            tree_ptr& left() {
                return left_;
            }
            tree_ptr& right() {
                return right_;
            }
            // binary_tree<T> parent() {
            //     return parent_;
            // }
            binary_tree<T>* parent() const {
                return parent_;
            }
    
            // void insert(T data) {
            //     binary_tree<T>* current_node = this;
            //     current_node->add_node(current_node, data); 
            // }

            void insert(T data) {
                add_node(this, data);
            }

            void add_node(binary_tree* top_node, T data) {
                binary_tree* current_node = top_node;
                T next_data = data;

                while (current_node != nullptr) {
                    if (next_data <= current_node->data()) {
                        if (current_node->left() == nullptr) {
                            // left_ = new binary_tree(next_data);
                            current_node->left_ = std::unique_ptr<binary_tree<T>>(new binary_tree(next_data, current_node));
                            // left_.parent_ = current_node;
                            break;
                        } else {
                            current_node = current_node->left().get();
                        }
                    }

                    if (next_data > current_node->data()) {
                        if (current_node->right() == nullptr) {
                            // current_node.right_ = binary_tree(next_data);
                            current_node->right_ = std::unique_ptr<binary_tree<T>>(new binary_tree(next_data, current_node));
                            // current_node.right_.parent_ = current_node;
                            break;
                        } else {
                            current_node = current_node->right().get();
                        }
                    }
                }
            }

            // Define the Iterator struct
            struct iterator {
                binary_tree<T>* current_node_;

                iterator(binary_tree<T>* node) : current_node_(node) {}
            
                // Implement necessary iterator methods (e.g., operator++, operator*).
                bool operator!=(iterator &rhs) {
                    return current_node_ != rhs.current_node_;
                }

                iterator &operator++() {
                    if (current_node_->right()) {
                        current_node_ = current_node_->right().get();
                        while (current_node_->left()) {
                            current_node_ = current_node_->left().get();
                        }
                    } else {
                        binary_tree<T>* parent = current_node_->parent();
                        while (parent && current_node_ == parent->right().get()) {
                            current_node_ = parent;
                            parent = parent->parent();
                        }
                        current_node_ = parent;
                    }
                    return *this;
                    
                }

                T& operator*() {
                    return current_node_->data();
                }

            };
            
            // Implement begin() function
            iterator begin() {
                binary_tree<T>* current_node_ = this;
                while (current_node_->left()) {
                    current_node_ = current_node_->left_.get();
                }
                return iterator(current_node_);
            };

            iterator end() {
                return iterator(nullptr);
            };
    
        };

        template <typename T>
        binary_tree<T>* make_tree(vector<T> input) {
            binary_tree<T>* current_node = new binary_tree<T>(input[0]);            
            for (int i = 1; i < static_cast<int>(input.size()); i++) {
                current_node->add_node(current_node, input[i]);
            }
    
            return current_node;
        }
}  // namespace binary_search_tree


#endif // BINARY_SEARCH_TREE_H