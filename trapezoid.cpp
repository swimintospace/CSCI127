//Name: Eliyas Philip
//Email: eliyas.philip84@myhunter.cuny.edu

#include <iostream>
using namespace std;


int main()
{
        int i, h, number;
        char letter;
        cout << "Enter a number: \n";
        cin >> number;
        cout << "Enter a letter: \n";
        cin >> letter;

        
        for(int i = 0; i < number; i++)
        {
            for(int h = i; h <= i; h++)
            {
                cout << letter;
            }
            cout << "\n";
        
        }
        for(int i = 0; i < number; i++)
        {
            for(int h = i; h < number; h++)
            {
                cout << letter;
            }
            cout << "\n";
        }

}