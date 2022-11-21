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
#include <vector>

#include "adts/list.h"
#include "adts/queue.h"
#include "adts/stlList.h"
#include "adts/stlQueue.h"

#include "linkedBSTNode.h"

using std::pair;
using std::runtime_error;
using std::vector;

template <typename K, typename V> LinkedBST<K, V>::LinkedBST() {
    this->size = 0;
    this->root = nullptr;
}

template <typename K, typename V> LinkedBST<K, V>::~LinkedBST() {
    while(this->size > 0) {
        remove(this->root->getKey());
    }
}

template <typename K, typename V> int LinkedBST<K, V>::getSize() {
    return this->size;
}

template <typename K, typename V> bool LinkedBST<K, V>::isEmpty() {
    if(this->root == nullptr) {
        return true;
    } else {
        return false;
    }
}

template <typename K, typename V> void LinkedBST<K, V>::insert(K key, V value) {
    this->root = insertInSubtree(this->root, key, value);
    this->size += 1;
}

template <typename K, typename V> void LinkedBST<K, V>::update(K key, V value) {
    updateInSubtree(this->root, key, value);
}

template <typename K, typename V> V LinkedBST<K, V>::get(K key) {
    return findInSubtree(this->root, key);
}

template <typename K, typename V> bool LinkedBST<K, V>::contains(K key) {
    return containsInSubtree(this->root, key);
}

template <typename K, typename V> void LinkedBST<K, V>::remove(K key) {
    this->root = removeFromSubtree(this->root, key);
    this->size -= 1;
}

template <typename K, typename V> vector<K> LinkedBST<K, V>::getKeys() {
    vector<pair<K, V>> list = getItems();
    vector<K> new_list;
    for(int i = 0; i < list.size(); i++) {
        new_list.push_back(list[i].first);
    }
    return new_list;
}

template <typename K, typename V>
vector<pair<K, V>> LinkedBST<K, V>::getItems() {
    vector<pair<K, V>> list = traversePreOrder();
    vector<pair<K, V>> new_list;
    for(int i = 0; i < list.size(); i++) {
        new_list.push_back(list[i]);
    }
    return new_list;
}

template <typename K, typename V> int LinkedBST<K, V>::getHeight() {
    return getHeightInSubtree(this->root);
}

template <typename K, typename V> K LinkedBST<K, V>::getMaxKey() {
    return getMaxInSubtree(this->root).first;
}

template <typename K, typename V> K LinkedBST<K, V>::getMinKey() {
    return getMinInSubtree(this->root).first;
}

template <typename K, typename V>
vector<pair<K, V>> LinkedBST<K, V>::traversePreOrder() {
    List<pair<K, V>>* list = new STLList<pair<K, V>>();
    buildPreOrderTraversal(this->root, list);
    vector<pair<K, V>> new_list; 
    while(!list->isEmpty()) {
        new_list.push_back(list->removeFirst());
    }
    delete list;
    return new_list;
}

template <typename K, typename V>
vector<pair<K, V>> LinkedBST<K, V>::traverseInOrder() {
    List<pair<K, V>>* list = new STLList<pair<K, V>>();
    buildInOrderTraversal(this->root, list);
    vector<pair<K, V>> new_list; 
    while(!list->isEmpty()) {
        new_list.push_back(list->removeFirst());
    }
    delete list;
    return new_list;
}

template <typename K, typename V>
vector<pair<K, V>> LinkedBST<K, V>::traversePostOrder() {
    List<pair<K, V>>* list = new STLList<pair<K, V>>();
    buildPostOrderTraversal(this->root, list);
    vector<pair<K, V>> new_list; 
    while(!list->isEmpty()) {
        new_list.push_back(list->removeFirst());
    }
    delete list;
    return new_list;
}

template <typename K, typename V>
vector<pair<K, V>> LinkedBST<K, V>::traverseLevelOrder() {
    List<LinkedBSTNode<K, V>*>* list = new STLList<LinkedBSTNode<K, V>*>();
    vector<pair<K, V>> new_list; 
    LinkedBSTNode<K, V>* current;
    
    list->insertFirst(this->root);

    while(list->getSize() > 0) {
        current = list->removeFirst();
        
        if(current != nullptr) {
            new_list.push_back(pair<K, V>(current->getKey(), current->getValue()));
        } 
        
        if(current->getLeft() != nullptr && current->getRight() != nullptr) {
            list->insertLast(current->getLeft());
            list->insertLast(current->getRight());
        }
        else if(current->getLeft() != nullptr && current->getRight() == nullptr) {
            list->insertLast(current->getLeft());
        }
        else if(current->getRight() != nullptr && current->getLeft() == nullptr) {
            list->insertLast(current->getRight());
        } 
    }
    delete list;
    return new_list; 
}

template <typename K, typename V> void LinkedBST<K, V>::checkInvariants() {
    if (this->countNodes(this->root) != this->size) {
        throw runtime_error(
            "Problem in BST: Node count doesn't match tree size");
    }
    if (this->root != nullptr) {
        // The bounds provided here are arbitrary because the false arguments
        // indicate that they do not apply.  But we need a value of type K to
        // fill this parameter since we don't have globally min/max K values
        // generically.
        this->verifyKeysBoundedBy(this->root, false, this->root->getKey(),
                                  false, this->root->getKey());
    }
}
