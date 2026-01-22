#pragma once

#include <memory>
#include <optional>
#include <iostream>

namespace linked_list {
    template <typename T>

    class List {
        private:
        public:
            List(){}
    
            std::optional<T> value{};
            List<T>* next{};
            List<T>* previous{};
    
            void push(T input) {
                List<T>* new_node = new List<T>;
                new_node->value = input;
                
                List<T>* last_node{};
                if (!value.has_value()) {
                    value = input;
                } else if (next == nullptr) {
                    next = new_node;
                    new_node->previous = this;
                } else {
                    last_node = next;
                    while (last_node->next) {
                        last_node = last_node->next;
                    }
                    last_node->next = new_node;
                    new_node->previous = last_node;
                }
            }
            std::optional<T> pop() {
                List<T>* last_node{};
                List<T>* second_last_node{};
                std::optional<T> output{};

                if (!value.has_value()) {
                    return std::nullopt;
                }
                
                if (next == nullptr) {
                    output = value;
                    value = std::nullopt;
                } else {
                    last_node = next;
                    while (last_node->next) {
                        last_node = last_node->next;
                    }
                    output = last_node->value;
                    second_last_node = last_node->previous;
                    second_last_node->next = nullptr;
                }
                return output;
            }
            std::optional<T> shift() {
                std::optional<T> output{};
                output = value;

                if (next == nullptr) {
                    value = std::nullopt;
                    return output;
                }
                
                List<T>* second_node = next;
                if (second_node->next) {
                    second_node->next->previous = this;
                }
                value = second_node->value;
                next = second_node->next;
                
                delete second_node;
                second_node = nullptr;
                return output;
            }
            void unshift(T input) {
                // create duplicate first node
                List<T>* duplicate_first_node = new List<T>;
                duplicate_first_node->value = value;
                duplicate_first_node->next = next;

                // update 2nd node to link to duplicate first node
                if (next) {
                    List<T>* old_second_node = next;
                    old_second_node->previous = duplicate_first_node;
                }
                // update original first node with new node data, link to duplicate first node
                value = input;
                next = duplicate_first_node;
            }
            int count() {
                if (!value) {
                    return 0;
                }
                int count = 1;
                List<T>* current_node = this;
                while (current_node->next) {
                    count += 1;
                    current_node = current_node->next;
                }
                return count;
            }
            void erase(T input) {
                List<T>* current_node = this;
                    if (current_node->value == input) { // if first node is a match
                        if (current_node->next == nullptr && current_node->previous == nullptr){ // if first node is only node
                            value = std::nullopt;
                        } else if (current_node->next) { // if there is a 2nd node
                            List<T>* next_node = current_node->next;
                            current_node->value = next_node->value;
                            current_node->next = next_node->next;
                            if (next_node->next) { // if there is a 3rd node
                                next_node->next->previous = current_node;
                            }
                            delete next_node;
                        }
                    } else if (current_node->next) { // if there is more than one node, search through nodes
                        while (current_node->next) {
                            current_node = current_node->next;
                            if (current_node->value == input) {
                                if (current_node->next) { // if match is not last node
                                    current_node->previous->next = current_node->next;
                                    current_node->next->previous = current_node->previous;
                                    delete current_node;
                                    break;
                                } else { // if match is last node
                                    current_node->previous->next = nullptr;
                                    delete current_node;
                                    break;
                                }
                            }
                        }
                    }
            }
    };
}  // namespace linked_list
