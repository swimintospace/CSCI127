//Name: Eliyas Philip
//Email: eliyas.philip84@myhunter.cuny.edu

#include <iostream>
using namespace std;

int main()
{
    int i;
    int number;
    string reminder;

    cout << "Please enter a number: ";
    cin >> number;
    cout << "Please type a word: ";
    cin >> reminder;

    for(i = number; i > 0; i--)
    {
        cout << i << ",\n";
    }

    cout << "Time for " << reminder << "!";
    return 0;
}