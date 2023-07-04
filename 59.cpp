#include <iostream>
using namespace std;

int main()

{
float budget;
cout << "Enter your monthly budget for food and coffee: ";
cin >> budget;

float cost;
cout << "How much are you spending in a week for coffee? ";
cin >> cost;

    {
        cout << "Budget left after week 1 " << (budget - cost) << "\n";
        cout << "Budget left after week 2 " << (budget - 2cost) << "\n";
        cout << "Budget left after week 3 " << (budget - 3cost) << "\n";
        cout << "Budget left after week 4 " << (budget - 4*cost) << "\n";
    }

return 0;
}