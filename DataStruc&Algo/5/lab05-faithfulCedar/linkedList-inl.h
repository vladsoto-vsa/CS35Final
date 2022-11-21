/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include <stdexcept>

using std::runtime_error;

// This file defines the methods for two classes: LinkedListNode and LinkedList.
// The LinkedListNode methods have been defined for you.  You are responsible
// for defining the LinkedList methods.

// //////// LinkedListNode /////////////////////////////////////////////////////

template <typename T>
LinkedListNode<T>::LinkedListNode(T val, LinkedListNode<T>* next) {
    this->value = val;
    this->next = next;
}

// //////// LinkedList /////////////////////////////////////////////////////////

template <typename T> LinkedList<T>::LinkedList() {
    this->head = nullptr;
    this->tail = nullptr;
    this->size = 0;
    
}

template <typename T> LinkedList<T>::~LinkedList() {
    while(this->size > 0) {
        this->removeFirst();
    }
    this->head = nullptr;
    this->tail = nullptr;
}

template <typename T> void LinkedList<T>::checkInvariants() {
   LinkedListNode<T>* current_node = this->head;
   int list_size = 0;

   while(current_node != nullptr) { 
       // increments through lists until the last node 
       current_node = current_node->next;
       list_size += 1;
   } 
  
   if(list_size != this->size) {
       throw runtime_error("Size variable not equal to linked_list size");
   } 
}

template <typename T> int LinkedList<T>::getSize() {
    return this->size;
}

template <typename T> bool LinkedList<T>::isEmpty() {
    if(this->head == nullptr) {
        return true;
    } else {
        return false;
    }
}

template <typename T> T LinkedList<T>::getFirst() {
    if(this->size == 0) {
        throw runtime_error("List is empty.");
    }
    return this->head->value;
}

template <typename T> T LinkedList<T>::getLast() {
    if(this->size==0){
        throw runtime_error("List is empty.");
    }
    return this->tail->value;
}

template <typename T> T LinkedList<T>::get(int index) {
    if(this->size == 0) {
        throw runtime_error("List is empty.");
    } else if(index < 0 || index >= this->size) {
        // if accessing an index outside the bounds of the list
        throw runtime_error("Accesing undefined value.");   
    }
    
    LinkedListNode<T>* current_node;
    current_node = this->head;

    for(int i = 0; i < index; i++) {
        current_node = current_node->next;
    }

    return current_node->value;
}

template <typename T> void LinkedList<T>::insertFirst(T value) {
    LinkedListNode<T>* new_node = new LinkedListNode<T>(value, this->head);
    LinkedListNode<T>* first_node = this->head;
    this->head = new_node;
     if(this->size == 0) {
        this->head = new_node;
        this->tail = new_node;
    } 
    else {
        new_node->next = first_node;
        this->head = new_node;

    }
    this->size += 1;
}

template <typename T> void LinkedList<T>::insertLast(T value) {
    LinkedListNode<T>* new_node = new LinkedListNode<T>(value, nullptr);
    LinkedListNode<T>* last_node = this->tail;
    if(this->size == 0) {
        this->tail = new_node;
        this->head = new_node;
    } 
    else {
        last_node->next = new_node;
        this->tail = new_node;
    }

    this->size += 1;
}

template <typename T> T LinkedList<T>::removeFirst() {
    LinkedListNode<T>* current_node = this->head;
    T output;

    if(this->size == 0) {
        throw runtime_error("No items in the list to remove.");
    }

    if(this->size == 1) {
        output = current_node->value;
        this->head = nullptr;
        this->tail = nullptr;
        delete current_node;
    }
    else {
        LinkedListNode<T>* next_node = current_node->next; 
        output = current_node->value; 
        this->head = next_node; // head points to the node after the first was removed
        delete current_node;
    }

    this->size -= 1;
    return output;
}

template <typename T> T LinkedList<T>::removeLast() {
    LinkedListNode<T>* current_node = this->head;
    T output; // the element of the node that will be removed
    
    if(this->size == 0) {
        throw runtime_error("No items in the list to remove.");
    }

    if(this->size == 1) {
        // if there is only one element in the list
        output = current_node->value; 
        delete current_node;
        this->tail = nullptr;
        this->head = nullptr;
    } 
    else {

        for (int i=0; i < this->size-2; i++) {
            current_node = current_node->next;
        }
        
        LinkedListNode<T>* last_node = current_node->next; 
        output = last_node->value; // element of last node 
        current_node->next = nullptr; 
        this->tail = current_node; 
        delete last_node;
    }

    this->size -= 1;
    return output;
}
