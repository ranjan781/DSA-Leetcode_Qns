class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n=nums.size();
        int num;
        for(int i=0;i<n;i++){
            int count=0;
            num=nums[i];
            for(int j=0;j<n;j++){
                if(nums[j]==num)
                    count++;    
            }
            if(count==1){
            return num;
        }
        }
        return num;
    }
        
};