#include "simple_linked_list.h"

#include <stdexcept>

namespace simple_linked_list {

std::size_t List::size() const {
    // Return the correct size of the list.
    return current_size;
}

void List::push(int entry) {
    // Implement a function that pushes an Element with `entry` as data to
    // the front of the list.
    Element* new_entry = new Element(entry);
    new_entry->next = head;
    head = new_entry;
    current_size += 1;
}

int List::pop() {
    // Implement a function that returns the data value of the first
    // element in the list then discard that element.
    int output = head->data;
    if (head->next != nullptr) {
        Element* delete_node = head;
        head = head->next;
        delete delete_node;
    }
    current_size -=1;
    return output;
}

void List::reverse() {
    // Implement a function to reverse the order of the elements in the
    // list.
    Element* previous{};

    if (static_cast<int>(current_size) == 2) {
        Element* n0 = head;
        Element* n1 = head->next;
        
        n1->next = head;
        n0->next = nullptr;
        head = n1;
    } else {    
        for (int i = 0; i < (static_cast<int>(current_size)-2); i++) {
            Element* n0 = head;
            Element* n1 = nullptr;
            Element* n2 = nullptr;
    
            if (i == (static_cast<int>(current_size)-3)) { // if tail node
                head->next = previous;
            } else {
                if (n0->next != nullptr) { // assign n0-n2
                    n1 = n0->next;
                    if (n0->next->next) {
                        n2 = n0->next->next;
                    }
                    n0->next = previous;
                }
        
                if (n1 != nullptr) { // make n1 point to n0
                    n1->next = n0;
                }
        
                if (n2 != nullptr) { // move to n2 for next loop
                    previous = n1;
                    head = n2;
                }
            }
        }
    }
}

List::~List() {
    // TODO: Ensure that all resources are freed on destruction
}

}  // namespace simple_linked_list
