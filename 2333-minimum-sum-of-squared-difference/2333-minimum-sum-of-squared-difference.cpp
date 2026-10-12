class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        int n=nums1.size();
        vector<int>countdiff(1e5+1,0);
        for(int i=0;i<n;i++){
            int d=abs(nums1[i]-nums2[i]);
            countdiff[d]++;
        }
        int K=k1+k2;
        for(int currdiff=1e5;currdiff>0 && K>0;currdiff--){
            int countOps=min(countdiff[currdiff],K);
            countdiff[currdiff]-=countOps;
            countdiff[currdiff-1]+=countOps;
            K-=countOps;
        }
        long long result=0;
        for(long long d=1;d<=1e5;d++){
            result+=(countdiff[d]*d*d);
        }
        return result;
    }
};