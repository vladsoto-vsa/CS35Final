/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include <stdexcept>
using std::pair;
using std::runtime_error;
using std::vector;

template <typename K, typename V> LinearDictionary<K, V>::LinearDictionary() {
}

template <typename K, typename V> LinearDictionary<K, V>::~LinearDictionary() {
}

template <typename K, typename V> int LinearDictionary<K, V>::getSize() {
    return this->items.size();
}

template <typename K, typename V> bool LinearDictionary<K, V>::isEmpty() {
    if(this->items.size() == 0) {
        return true;
    }
    else {
        return false;
    }
}

template <typename K, typename V>
void LinearDictionary<K, V>::insert(K key, V value) {
    if(contains(key)) {
        throw runtime_error("key already exists");
    }
    
    this->items.push_back(pair<K, V> (key, value));
}

template <typename K, typename V>
void LinearDictionary<K, V>::update(K key, V value) {
    bool key_found = false;

    for(int i = 0; i < this->items.size(); i++) {
        if(this->items[i].first == key) {
            this->items[i].second = value;
            key_found = true;
        }
    }

    if(!key_found) {
        throw runtime_error("key not found");
    }
    
}

template <typename K, typename V> V LinearDictionary<K, V>::get(K key) {
    bool key_found = false;
    V value;
    
    for(int i = 0; i < this->items.size(); i++) {
        if(this->items[i].first == key) {
            value = this->items[i].second;
            key_found = true;
        }
    }

    if(!key_found) {
        throw runtime_error("key not found");
    }

    return value;
}

template <typename K, typename V> bool LinearDictionary<K, V>::contains(K key) {
    for(int i = 0; i < this->items.size(); i++) {
        if(this->items[i].first == key) {
            return true;
        }
    }
    return false;
}

template <typename K, typename V> void LinearDictionary<K, V>::remove(K key) {
    bool key_found = false;
    for(int i = 0; i < this->items.size(); i++) {
        if(this->items[i].first == key) {
            this->items.erase(this->items.begin() + i, this->items.begin() + i + 1);
            key_found = true;
        }
    }
    
    if(!key_found) {
        throw runtime_error("key not found");
    }
}

template <typename K, typename V> vector<K> LinearDictionary<K, V>::getKeys() {
    vector<K> itemKeys;
    for(int i = 0; i < this->items.size(); i++) {
        itemKeys.push_back(this->items[i].first);
    }
    return itemKeys;
}

template <typename K, typename V>
vector<pair<K, V>> LinearDictionary<K, V>::getItems() {
    return this->items;
}

template <typename T> void removeFromVector(vector<T> &list, int index){
  if(index < 0 || index >= list.size()){
    throw runtime_error("index out of range in removeFromVector");
  }
  list.erase(list.begin()+index, list.begin()+index+1);
}

