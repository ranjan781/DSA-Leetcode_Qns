class Solution {
public:
    int split(vector<int>& nums, int maxSum) {
        int cnt = 1;
        int sum = 0;

        for (int x : nums) {
            if (sum + x <= maxSum) {
                sum += x;
            } else {
                cnt++;
                sum = x;
            }
        }

        return cnt;
    }

    int splitArray(vector<int>& nums, int k) {

        int low = *max_element(nums.begin(), nums.end());
        int high = accumulate(nums.begin(), nums.end(), 0);

        int ans = high;

        while (low <= high) {

            int mid = low + (high - low) / 2;

            if (split(nums, mid) <= k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return ans;
    }
};