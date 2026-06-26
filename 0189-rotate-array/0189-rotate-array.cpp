class Solution {
public:
    void reverseArray(vector<int>& nums,int start,int end){
    if(nums.size()==0 || nums.size()==1){
        return;
    }
    while(start<end){
        swap(nums[start],nums[end]);
        start++;
        end--;
    }
}
    void rotate(vector<int>& nums, int k) {
        int n=nums.size();
        k=k%n;
        reverseArray(nums, 0, n - 1);

        //Reverse first k elements
        reverseArray(nums, 0, k - 1);

        //Reverse remaining n-k elements
        reverseArray(nums, k, n - 1);
        
    }
};

