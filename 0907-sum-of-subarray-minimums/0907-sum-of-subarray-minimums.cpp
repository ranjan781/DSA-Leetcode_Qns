class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {

        int n = arr.size();
        const int MOD = 1e9 + 7;

        vector<int> left(n), right(n);

        stack<int> st;

        // Previous Smaller
        for(int i = 0; i < n; i++) {

            while(!st.empty() && arr[st.top()] > arr[i])
                st.pop();

            if(st.empty())
                left[i] = i + 1;
            else
                left[i] = i - st.top();

            st.push(i);
        }

        while(!st.empty())
            st.pop();

        // Next Smaller
        for(int i = n-1; i >=0; i--) {

            while(!st.empty() && arr[st.top()] >= arr[i])
                st.pop();

            if(st.empty())
                right[i] = n - i;
            else
                right[i] = st.top() - i;

            st.push(i);
        }

        long long ans = 0;

        for(int i=0;i<n;i++){

            ans = (ans + (1LL * arr[i] * left[i] * right[i]) % MOD) % MOD;
        }

        return ans;
    }
};
// class Solution {
// public:
//     int sumSubarrayMins(vector<int>& arr) {
//         long long sum=0;
//         const int MOD = 1e9 + 7;
//         for(int i=0;i<arr.size();i++){
//             int mini=arr[i];
//             for(int j=i;j<arr.size();j++){
//                 mini=min(mini,arr[j]);
//                 sum=(sum+mini)%MOD;
//             }
//         }
//         return sum%MOD;
//     }
// };