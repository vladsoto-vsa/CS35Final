/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include <stdexcept>


#include "hashFunctions.h"

using std::pair;
using std::runtime_error;
using std::vector;


template <typename K, typename V> HashTable<K, V>::HashTable() {
    this->capacity = 4;
    this->size = 0;
    this->maxLoadFactor = 0.75;
    this->table = new LinearDictionary<K, V>[this->capacity];
}

template <typename K, typename V>
HashTable<K, V>::HashTable(float maxLoadFactor) {
    this->capacity = 4;
    this->size = 0;
    this->maxLoadFactor = maxLoadFactor;
    this->table = new LinearDictionary<K, V>[this->capacity];
}

template <typename K, typename V> HashTable<K, V>::~HashTable() {
    delete[] this->table;
}

template <typename K, typename V> int HashTable<K, V>::getSize() {
    return this->size;
}

template <typename K, typename V> bool HashTable<K, V>::isEmpty() {
    if(this->size == 0) {
        return true;
    }
    else {
        return false;
    }
}

template <typename K, typename V> void HashTable<K, V>::insert(K key, V value) {
    if((float(this->size)/this->capacity) > this->maxLoadFactor) {
        expandCapacity();
    }

    int index = hash(key, this->capacity);
    this->table[index].insert(key, value);   
    this->size += 1;
}

template <typename K, typename V> void HashTable<K, V>::update(K key, V value) {
    int index = hash(key, this->capacity);
    this->table[index].update(key, value);
}

template <typename K, typename V> V HashTable<K, V>::get(K key) {
    int index = hash(key, this->capacity);
    return this->table[index].get(key);
}

template <typename K, typename V> bool HashTable<K, V>::contains(K key) {
    int index = hash(key, this->capacity);
    if(this->table[index].contains(key)) {
        return true;
    }
    else {
        return false;
    }
}

template <typename K, typename V> void HashTable<K, V>::remove(K key) {
    int index = hash(key, this->capacity);
    this->table[index].remove(key);
    this->size -= 1;
}

template <typename K, typename V> vector<K> HashTable<K, V>::getKeys() {
    vector<K> itemKeys;
    for(int i = 0; i < this->capacity; i++) {
        vector<K> tempKeys = this->table[i].getKeys();
        for(int j = 0; j < tempKeys.size(); j++) {
            itemKeys.push_back(tempKeys[j]);
        }
    }
    return itemKeys;
}

template <typename K, typename V>
vector<pair<K, V>> HashTable<K, V>::getItems() {
    vector<pair<K, V>> items;
    for(int i = 0; i < this->capacity; i++) {
       vector<pair<K, V>> tempItems = this->table[i].getItems();
        for(int j = 0; j < tempItems.size(); j++) {
            items.push_back(tempItems[j]);
        }
    }  
    return items;
}

template <typename K, typename V> void HashTable<K, V>::expandCapacity() {
    LinearDictionary<K, V>* newTable = new LinearDictionary<K, V>[this->capacity*2];
    vector<pair<K, V>> items = getItems();
    this->capacity *= 2;
    for(int i = 0; i < items.size(); i++) {
        int index = hash(items[i].first, this->capacity);
        newTable[index].insert(items[i].first, items[i].second);
    }
    delete[] this->table;
    this->table = newTable;
}

// TODO: put any other definitions here
