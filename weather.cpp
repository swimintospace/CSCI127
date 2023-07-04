//Name: Eliyas Philip
//Email: eliyas.philip84@myhunter.cuny.edu

#include <iostream>

using namespace std;

int main()
{
    
    int temperature;

    cout << "Enter the temperature: ";
    cin >> temperature;
    
    if(temperature < 32)
    {
        cout << "It's freezing!";
    }
    else if(temperature < 68 && temperature > 32)
    {
        cout << "It's cold!";
    }
    else if(temperature < 73 && temperature > 68)
    {
        cout << "It's warm!";
    }
    else 
    {
        cout << "It's hot!";
    }

    return 0;
}