#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string longestPalindrom(string s){
        int n = s.size();
        if (n < 2) {
            return s;
        }
        int maxLen = 1;
        int begin = 0;
        vector<vector<int>> dp(n, vector<int>(n));

        for (int i=0; i<n; i++) {
            dp[i][i] = true;
        }

        
    }
}