#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include "states-and-capitals-arrays.cpp"
using namespace std;

// quiz on capital cities for US states
// display states in mixed-up order
// ask matching question, keep score

int main() {
    int index, temp, swapPosition, count=0, correct=0;
    string userAnswer;
    int correctAnswer;
    // scramble order of states to ask
    srand(time(NULL));  // initialize random number generator
    int displayOrder[MAX_STATES] = {};
    for(index=0;index<MAX_STATES;index++) {
        displayOrder[index] = index;
    } // [0,1,2,3,4,5,...,48,49]
    for(index=0;index<MAX_STATES;index++) {
        swapPosition = rand() % MAX_STATES;
        temp = displayOrder[index];
        displayOrder[index] = displayOrder[swapPosition];
        displayOrder[swapPosition] = temp;
    }
    cout << "State Capital Quiz!\nHow many questions?"; cin >> count;
    if (count < 0 || count > 50) return(-1);

    int matching_states[count];
    int matching_capitals[count];
    for(index=0;index<count;index++) {
        matching_states[index] = displayOrder[index];
        matching_capitals[index] = displayOrder[index];
    }
    // scramble capitals
    for(index=0;index<count;index++) {
        swapPosition = rand() % count;
        temp =  matching_capitals[index];
        matching_capitals[index] = matching_capitals[swapPosition];
        matching_capitals[swapPosition] = temp;
    }
    for(index=0;index<count;index++) {
        cout << (index + 1) << ". " << state[matching_states[index]]
            << "\t\t" << char(65+index) << ". " << capital[matching_capitals[index]]
            << endl;
    }
    for(index=0;index<count;index++) {
        cout << (index + 1) << ". " << state[matching_states[index]] << "?";
        cin >> userAnswer;
        int capital_index = int(userAnswer[0])-65;
        if (capital_index >=0 && capital_index <= count && matching_states[index] == matching_capitals[capital_index]) {
            cout << "Correct! ";
            correct++;
        } else {
            cout << "Incorrect. ";
        }
        cout << "The captial of " << state[matching_states[index]]
        << " is " << capital[matching_states[index]] << "." << endl;
    }
    cout << "You got " << correct << " out of " << count << " correct!\n";
    return 0;
}

