#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include "states-and-capitals-arrays.cpp"
using namespace std;

// quiz on capital cities for US states
// display states in mixed-up order
// ask either-or question, keep score

int main() {
    int index, temp, swapPosition, count=0, correct=0;
    int userAnswer, correctAnswer;
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
//    for(index=0;index<MAX_STATES;index++) {
//        cout << displayOrder[index] << ",";
//    }
    cout << "State Capital Quiz!\nHow many questions?"; cin >> count;
    if (count < 0 || count > 50) return(-1);
    for(index=0;index<count;index++) {
        cout << "For the state of " << state[displayOrder[index]]
            << ", is the capital ";
        if (rand() % 2 == 0) {
            correctAnswer = 1;
            cout << capital[displayOrder[index]] << " or "
            << another[displayOrder[index]] << " (1 or 2)?";
        } else {
            correctAnswer = 2;
            cout << another[displayOrder[index]] << " or "
            << capital[displayOrder[index]] << " (1 or 2)?";
        }
        cin >> userAnswer;
        if (userAnswer == correctAnswer) {
            cout << "Correct! ";
            correct++;
        } else {
            cout << "Incorrect. ";
        }
        cout << "The captial of " << state[displayOrder[index]]
        << " is " << capital[displayOrder[index]] << "." << endl;
    }
    cout << "You got " << correct << " out of " << count << " correct!\n";
    return 0;
}
