class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int n=nums.size();
        if(n==1) return nums[0];
        if(nums[0]!=nums[1]) return nums[0];
        if(nums[n-1]!=nums[n-2]) return nums[n-1];
        int low=1;
        int high=n-2;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(nums[mid]!=nums[mid-1]  && nums[mid]!=nums[mid+1]){
                return nums[mid];
            }
            //we are in left
            else if((mid%2==1 && nums[mid]==nums[mid-1]) || (mid%2==0 && nums[mid]==nums[mid+1])){
                low=mid+1;
            }else{
                high=mid-1;
            }
        }
        return -1;
        
    }
};


//  int n=nums.size();
//         int str=0,end=nums.size()-1;
//         if(n==1) return nums[0];
//         while(str<=end){
//             int mid=str+(end-str)/2;
//             if(mid== 0 && nums[0]!=nums[1]) return nums[mid];//only two elements exist in array
//             if(mid== n-1 && nums[n-1]!=nums[n-2]) return nums[mid];
//             if(nums[mid-1]!=nums[mid] && nums[mid]!=nums[mid+1]){
//                 return nums[mid];
//             }
//             if(mid%2==0){//even spaces
//                 if(nums[mid-1]==nums[mid]){//right search
//                     end=mid-1;
//                 }
//                 else{//left search
//                     str=mid+1;
//                 }
//             }
//             else{//odd spaces
//                 if(nums[mid-1]==nums[mid]){//right search
//                     str=mid+1;
//                 }
//                 else{//left search
//                     end=mid-1;
//                 }
//             }
//         }