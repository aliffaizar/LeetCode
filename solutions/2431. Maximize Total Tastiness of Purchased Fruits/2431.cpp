class Solution {
 public:
  int maxTastiness(vector<int>& price, vector<int>& tastiness, int maxAmount,
                   int maxCoupons) {
    vector<vector<int>> dp(maxAmount + 1, vector<int>(maxCoupons + 1));

    for (int i = 0; i < price.size(); ++i) {
      for (int j = maxAmount; j >= price[i] / 2; --j) {
        for (int k = maxCoupons; k >= 0; --k) {
          const int buyWithCoupon =
              k == 0 ? 0 : dp[j - price[i] / 2][k - 1] + tastiness[i];
          const int buyWithoutCoupon =
              j < price[i] ? 0 : dp[j - price[i]][k] + tastiness[i];
          dp[j][k] = max({buyWithCoupon, buyWithoutCoupon, dp[j][k]});
        }
      }
    }

    return dp[maxAmount][maxCoupons];
  }
};
