#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int main() {
	string token;
	vector<double> stock_prices;
	ifstream inputfile("easy-249.txt");
	int buy_day, sell_day, max_buy, max_sell = 0;
	double profit, max_profit = 0;

	if (!inputfile.is_open()) {
		cout << "Could not open easy-249.txt" << endl;
		return -1;
	}

	while (inputfile >> token) {
		stock_prices.push_back(stod(token));
	}
	inputfile.close();

	for (buy_day = 0; buy_day < stock_prices.size(); buy_day++) {
		for (sell_day = buy_day + 2; sell_day < stock_prices.size(); sell_day++) {
			profit = stock_prices[sell_day] - stock_prices[buy_day];
			if (profit > max_profit) {
				max_profit = profit;
				max_buy = buy_day;
				max_sell = sell_day;
			}
		}
	}

	cout << "Max profit " << max_profit << " from buy on day " << max_buy << " at " << stock_prices[max_buy] << " and sell on day " << max_sell << " at " << stock_prices[max_sell] << endl;

	return 0;
}
