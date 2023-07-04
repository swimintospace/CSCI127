//Name: Eliyas Philip
//Email: eliyas.philip84@myhunter.cuny.edu

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    double input;
    int btc;
    int eth;
    int doge;

    cout << "Enter amount in cryptocurrency: ";
    cin >> input;
    cout << fixed << setprecision(2);
    cout << input << " BTC in USD: $" << input * 31901.19 << " USD\n";
    cout << input << " ETH in USD: $" << input * 1901.54 << " USD\n";
    cout << input << " DOGE in USD: $" << input * 0.179733 << " USD\n";

    return 0;
}