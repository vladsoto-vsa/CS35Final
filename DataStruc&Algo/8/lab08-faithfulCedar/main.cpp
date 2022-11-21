/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <bits/stdc++.h>

#include "hashTable.h"
#include "ioUtils.h"
#include "tweet.h"
#include "adts/stlList.h"
#include "adts/stlMaxPriorityQueue.h"

using namespace std;

void printContents(STLMaxPriorityQueue<int, Tweet>* priorityContents) {
  int value = 5;
  if(priorityContents->getSize() < 5) {
    value = priorityContents->getSize();
  }
  for(int i = 0; i < value; i++) {
    Tweet current_tweet = priorityContents->remove();
    cout << "\n@" << current_tweet.username << "  " << "(" << current_tweet.date << ")" << endl;
    cout << current_tweet.contents << endl;              
    cout << "Rpl: " << current_tweet.replies << "  " << "Rtw: " << current_tweet.retweets << "  " <<
    "Lik: " << current_tweet.likes << "  " << "URL: " << current_tweet.url << endl; 
  }  
}

int main(int argc, char** argv) {
    string filename = argv[1];
    cout << "Loading tweets..." << endl;

    List<Tweet>* tweets = readTweetFile(filename);
    cout << "Processing tweets..." << endl;
   
    HashTable<string, STLList<Tweet>*>* userTweets = new HashTable<string, STLList<Tweet>*>(); 
    // dictionary of usernames mapped to tweets
    HashTable<string, STLList<Tweet>*>* dateTweets = new HashTable<string, STLList<Tweet>*>(); 
    // dictionary of dates mapped to tweets       


    int index = 0;
    for(int i = index; i < tweets->getSize(); i++) {
      string username = tweets->get(index).username;
      if (!userTweets->contains(username)){
        STLList<Tweet>* usernameFile = new STLList<Tweet>();
        userTweets->insert(username, usernameFile);
      }
      usernameFile->insertLast(tweets->get(i));
      index += 1;
    }
    delete usernameFile;

    index = 0;
    for(int i = index; i < tweets->getSize(); i++) {
      string date = tweets->get(index).date;
      if (!dateTweets->contains(date)) {
        STLList<Tweet>* dateFile = new STLList<Tweet>();
        dateTweets->insert(date, dateFile);
      }
      dateFile->insertLast(tweets->get(i));
      index += 1;
    }
    delete dateFile;


   /* while(index < tweets->getSize()) {
      STLList<Tweet>* userContents = new STLList<Tweet>();
      string username = tweets->get(index).username;
 
      while(index < tweets->getSize() && tweets->get(index).username == username) {
        if(tweets->get(index).username == username) {
          userContents->insertLast(tweets->get(index));
        }
        index += 1;
      }
      userTweets->insert(username, userContents);
    }

    index = 0;
    while(index < tweets->getSize()) {
      STLList<Tweet>* userContents = new STLList<Tweet>();
      string date = tweets->get(index).date;

      if(!dateTweets->contains(date)) {
        for(int i = index; i < tweets->getSize(); i++) {
          if(tweets->get(i).date == date) {
            userContents->insertLast(tweets->get(i));
          }
        }
        dateTweets->insert(date, userContents);
      }
      index += 1;
    }

    delete tweets;*/

    cout << "File " << filename << " loaded." << endl;
    cout << "Welcome to the tweet database query tool." << endl;

    while(true) {
      bool chosen = false;
      string option = "";
      string username = "";
      string date = "";
      
      while(!chosen) {
        cout << "\nPlease choose from the following options:" << endl;
        cout << "A) Search by username" << endl;
        cout << "B) Search by date" << endl;
        cout << "C) Quit" << endl;
        cout << "? ";
        cin >> option;

        if(option == "A") {
          cout << "Please enter your search username: ";
          cin >> username;
          chosen = true;
        }
        else if(option == "B") {
          cout << "Please enter your search date: ";
          cin >> date;
          chosen = true;
        }
        else if(option == "C") {
          // quitting the program
          cout << "\nGoodbye" << endl;
          vector<pair<string, STLList<Tweet>*>> items = userTweets->getItems();

          for(int i = 0; i < items.size(); i++) {
            delete items[i].second;
          }

          items = dateTweets->getItems();
          for(int i = 0; i < items.size(); i++) {
            delete items[i].second;
          }

          delete userTweets;
          delete dateTweets;
          return 1;
        }
        else {
          cout << "Invalid Selection.\n" << endl;
        }
      }

      if(option == "A" && !userTweets->contains(username)) {
        cout << "No tweets with username " << username << " found." << endl;
      } 
      else if(option == "B" && !dateTweets->contains(date)) {
        cout << "No tweets with date " << date << " found." << endl;
      }
      else {
        string typeCount = "";
        cout << "Search by (r)etweet count or (l)ike count? ";
        cin >> typeCount;
        if(typeCount == "r" || typeCount == "l") {

          if(option == "A") {
            vector<Tweet> contents = userTweets->get(username)->toVector();

            if(typeCount == "r") {
              vector<pair<int, Tweet>> userRetweets;

              for(int i = 0; i < contents.size(); i++) {
                userRetweets.push_back(pair<int, Tweet> (contents[i].retweets, contents[i]));
              }

              STLMaxPriorityQueue<int, Tweet>* priorityContents = new STLMaxPriorityQueue<int, Tweet>(userRetweets);
              printContents(priorityContents);
              delete priorityContents;
              
            }
            else {
              vector<pair<int, Tweet>> userLikeTweets;

              for(int i = 0; i < contents.size(); i++) {
                userLikeTweets.push_back(pair<int, Tweet> (contents[i].likes, contents[i]));
              }

              STLMaxPriorityQueue<int, Tweet>* priorityContents = new STLMaxPriorityQueue<int, Tweet>(userLikeTweets);
              printContents(priorityContents);
              delete priorityContents;
            }
          }
          else {
            // if option == "B"
            vector<Tweet> contents = dateTweets->get(date)->toVector();
            
            if(typeCount == "r") {
              vector<pair<int, Tweet>> dateRetweets;

              for(int i = 0; i < contents.size(); i++) {
                dateRetweets.push_back(pair<int, Tweet> (contents[i].likes, contents[i]));
              }

              STLMaxPriorityQueue<int, Tweet>* priorityContents = new STLMaxPriorityQueue<int, Tweet>(dateRetweets);
              printContents(priorityContents);
              delete priorityContents;
            }
      
            else {
              vector<pair<int, Tweet>> dateLikeTweets;

              for(int i = 0; i < contents.size(); i++) {
                dateLikeTweets.push_back(pair<int, Tweet> (contents[i].likes, contents[i]));
              }

              STLMaxPriorityQueue<int, Tweet>* priorityContents = new STLMaxPriorityQueue<int, Tweet>(dateLikeTweets);
              printContents(priorityContents);
              delete priorityContents;
            }
          }
        }
        else {
          cout << "Invalid count type." << endl;
        }
      }
    }
    return 0;
}
