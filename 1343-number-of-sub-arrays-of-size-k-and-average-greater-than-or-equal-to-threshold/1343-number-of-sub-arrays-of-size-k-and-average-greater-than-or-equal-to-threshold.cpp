class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int left=0;
        int right=k-1;
        int cnt=0;
        int sum = 0;

        for(int i = 0; i < k; i++)
        sum += arr[i];

        while(right < arr.size()) {
            if(sum / k >= threshold)
                cnt++;

            sum -= arr[left];
            left++;

            right++;

        if(right < arr.size())
            sum += arr[right];
            }
        return cnt;
    }
};