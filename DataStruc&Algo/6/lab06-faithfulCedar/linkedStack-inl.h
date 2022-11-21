/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include "linkedStack.h"

using namespace std;

// NOTE: Most of the method bodies in this class will only require a single line
// of code!

template <typename T> LinkedStack<T>::LinkedStack() {
}

template <typename T> void LinkedStack<T>::push(T element) {
    this->list.insertFirst(element);
}

template <typename T> T LinkedStack<T>::pop() {
    return this->list.removeFirst();
}

template <typename T> void LinkedStack<T>::insert(T element) {
    // To "insert" into a stack is to push onto it.  So when we are told to
    // insert, we will push.
    push(element);
}

template <typename T> T LinkedStack<T>::remove() {
    return pop();
}

template <typename T> int LinkedStack<T>::getSize() {
    return this->list.getSize();
}

template <typename T> bool LinkedStack<T>::isEmpty() {
    return this->list.isEmpty();
}

template <typename T> T LinkedStack<T>::peek() {
    return this->list.get(0);
}
