class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int n = arr.size();

        int i = 0;
        int j = 0;

        long long currsum = 0;

        vector<int> minBestlenTillidx(n, INT_MAX);

        int bestMinLen = INT_MAX;
        int result = INT_MAX;

        while (j < n) {

            currsum += arr[j];

            while (i <= j && currsum > target) {
                currsum -= arr[i];
                i++;
            }

            if (currsum == target) {

                int len = j - i + 1;

                
                if (i > 0 && minBestlenTillidx[i - 1] != INT_MAX) {
                    result = min(result, 
                                 len + minBestlenTillidx[i - 1]);
                }

                bestMinLen = min(bestMinLen, len);
            }

            minBestlenTillidx[j] = bestMinLen;

            j++;
        }

        return result == INT_MAX ? -1 : result;
    }
};