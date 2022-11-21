/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include <stdexcept>
#include <utility>

#include "adts/list.h"
#include "adts/stlList.h"

using std::runtime_error;

template <typename K, typename V>
V LinkedBST<K, V>::findInSubtree(LinkedBSTNode<K, V>* current, K key) {
    if(current == nullptr) { 
        throw runtime_error("No elements in the tree");
    }
    else if(current->getKey() == key) {
        return current->getValue();
    }
    else if(key < current->getKey()) {
        return findInSubtree(current->getLeft(), key);
    } 
    else {
        return findInSubtree(current->getRight(), key);
    } 
}

template <typename K, typename V>
bool LinkedBST<K, V>::containsInSubtree(LinkedBSTNode<K, V>* current, K key) {
    if(current == nullptr) { 
        return false;
    }
    else if(current->getKey() == key) {
        return true;
    }
    else if(key < current->getKey()) {
        return containsInSubtree(current->getLeft(), key);
    } 
    else {
        return containsInSubtree(current->getRight(), key);
    } 
}

template <typename K, typename V>
void LinkedBST<K, V>::updateInSubtree(LinkedBSTNode<K, V>* current, K key,
                                      V value) {
    if(current == nullptr) { 
        throw runtime_error("No elements in the tree");
    }
    else if(current->getKey() == key) {
        current->setValue(value); 
    }
    else if(key < current->getKey()) {
        updateInSubtree(current->getLeft(), key, value);
    } 
    else {
        updateInSubtree(current->getRight(), key, value);
    } 
}


template <typename K, typename V>
int LinkedBST<K, V>::getHeightInSubtree(LinkedBSTNode<K, V>* current) {
    if(current == nullptr) {
        return -1;
    } 
    else if(getHeightInSubtree(current->getLeft()) > getHeightInSubtree(current->getRight())) {
        return getHeightInSubtree(current->getLeft()) + 1; 
    }
    else{
        return getHeightInSubtree(current->getRight()) + 1;
    }
}

template <typename K, typename V>
pair<K, V> LinkedBST<K, V>::getMinInSubtree(LinkedBSTNode<K, V>* current) {
    if(current == nullptr) {
        throw runtime_error("No elements in the tree");
    }
    else if(current->getLeft() != nullptr) {
        return getMinInSubtree(current->getLeft());
    } 
    else {
        return pair<K, V>(current->getKey(), current->getValue());
    }
}

template <typename K, typename V>
pair<K, V> LinkedBST<K, V>::getMaxInSubtree(LinkedBSTNode<K, V>* current) {
    if(current == nullptr) {
        throw runtime_error("No elements in the tree");
    }
    else if(current->getRight() != nullptr) {
        return getMaxInSubtree(current->getRight());
    }
    else {
        return pair<K, V>(current->getKey(), current->getValue());
    }
}

template <typename K, typename V>
LinkedBSTNode<K, V>*
LinkedBST<K, V>::insertInSubtree(LinkedBSTNode<K, V>* current, K key, V value) {
    if(current == nullptr) {
       current = new LinkedBSTNode<K, V>(key, value);
       return current;
    }
    else if(current->getKey() == key) {
        throw runtime_error("Key has already been created");
    }
    else if(key < current->getKey()) {
        current->setLeft(insertInSubtree(current->getLeft(),key,value));
        return current;
    }
    else {
        current->setRight(insertInSubtree(current->getRight(),key,value));
        return current;
    }
}

template <typename K, typename V>
LinkedBSTNode<K, V>*
LinkedBST<K, V>::removeFromSubtree(LinkedBSTNode<K, V>* current, K key) {
    if(current == nullptr){
        throw runtime_error("There are no elements to remove");
    }
    else if (key < current->getKey()){
        current->setLeft(removeFromSubtree(current->getLeft(), key));
        return current; 
    } 
    else if(key > current->getKey()) {
        current->setRight(removeFromSubtree(current->getRight(), key));
        return current; 
    } 
    else {
        if(current->getLeft() == nullptr && current->getRight() == nullptr) {
            delete current;
            return nullptr; 
        } 
        else if(current->getLeft() != nullptr && current->getRight() == nullptr){
            LinkedBSTNode<K, V>* current_left = current->getLeft();
            delete current;
            return current_left;
        }
        else if(current->getLeft() == nullptr && current->getRight() != nullptr){
            LinkedBSTNode<K, V>* current_right = current->getRight();
            delete current;
            return current_right;
        }
        else {
            pair<K, V> big_pair = getMinInSubtree(current->getRight());
            current->setRight(removeFromSubtree(current->getRight(), big_pair.first));
            current->setKey(big_pair.first);
            current->setValue(big_pair.second);
            return current;
        }
    }
}

template <typename K, typename V>
void LinkedBST<K, V>::deleteSubtree(LinkedBSTNode<K, V>* current) {
    if(current == nullptr){
        return;
    }
    else {
        deleteSubtree(current->getLeft());
        deleteSubtree(current->getRight());
        current = nullptr;
    }
}

template <typename K, typename V>
void LinkedBST<K, V>::buildPreOrderTraversal(LinkedBSTNode<K, V>* current,
                                             List<pair<K, V>>* list) {
    if(current == nullptr) {
        return; 
    } 
    else {
        list->insertLast(pair<K, V>(current->getKey(), current->getValue()));
        buildPreOrderTraversal(current->getLeft(),list);
        buildPreOrderTraversal(current->getRight(), list);
    }
}

template <typename K, typename V>
void LinkedBST<K, V>::buildInOrderTraversal(LinkedBSTNode<K, V>* current,
                                            List<pair<K, V>>* list) {
    if(current == nullptr) {
        return;
    }
    else {
        buildInOrderTraversal(current->getLeft(),list);
        list->insertLast(pair<K, V>(current->getKey(), current->getValue()));
        buildInOrderTraversal(current->getRight(), list);
    }
   
}

template <typename K, typename V>
void LinkedBST<K, V>::buildPostOrderTraversal(LinkedBSTNode<K, V>* current,
                                              List<pair<K, V>>* list) {

    if(current == nullptr) {
        return;
    }
    else {
        buildPostOrderTraversal(current->getLeft(),list);
        buildPostOrderTraversal(current->getRight(),list);
        list->insertLast(pair<K, V>(current->getKey(), current->getValue()));
    }
    
}

template <typename K, typename V>
int LinkedBST<K, V>::countNodes(LinkedBSTNode<K, V>* current) {
    if (current == nullptr) {
        return 0;
    } 
    else {
        return this->countNodes(current->getLeft()) +
               this->countNodes(current->getRight()) + 1;
    }
}

template <typename K, typename V>
void LinkedBST<K, V>::verifyKeysBoundedBy(LinkedBSTNode<K, V>* current,
                                          bool minApplies, K minBound,
                                          bool maxApplies, K maxBound) {
    if (minApplies && current->getKey() < minBound) {
        throw runtime_error("LinkedBST::verifyKeysBoundedBy: a node has a "
                            "right descendent with lesser key");
    }
    if (maxApplies && current->getKey() > maxBound) {
        throw runtime_error("LinkedBST::verifyKeysBoundedBy: a node has a left "
                            "descendent with greater key");
    }
    if (current->getLeft() != nullptr) {
        verifyKeysBoundedBy(current->getLeft(), minApplies, minBound, true,
                            current->getKey());
    }
    if (current->getRight() != nullptr) {
        verifyKeysBoundedBy(current->getRight(), true, current->getKey(),
                            maxApplies, maxBound);
    }
}
