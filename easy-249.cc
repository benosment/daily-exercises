#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;


int main() {
  string raw_input;
  string token;
  vector<string> stock_prices;
  cout << "Enter stock prices: ";
  getline(cin, raw_input);
  cout << "Raw input:" << raw_input << endl;
  istringstream iss(raw_input);

  do {
    iss >> token;
    if (!token.empty()) {
      cout << "Token: " << token << endl;
      // TODO -- cast token to float
      // TODO -- add to vector
      // TODO -- how to does vector compare to others?
    }
  } while(iss);

  //while(getline(
  // while(getline(cin, raw_input, ' ')) {
  //   stock_prices.push_back(raw_input);
  //   cout << "Pushing " << raw_input << endl;

  // }
  //cout << "Stock prices: " << stock_prices << endl;

  return 0;
}
