#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hashmap;
        int need, value;

        for (int i = 0; i < nums.size(); i++) {
            value = nums.at(i);
            need = target - value;
            if (hashmap.find(need) == hashmap.end()) {
                // the value that we need is not present in the hash
                hashmap[value] = i;
            } else {
                return {hashmap.at(need) + 1, i+1};
            }
        }
    }
};

int main() {
    Solution s;
    vector<int> input {3, 2, 4};
    s.twoSum(input, 6);
    //cout << s.twoSum(input, 9) << endl;
}
