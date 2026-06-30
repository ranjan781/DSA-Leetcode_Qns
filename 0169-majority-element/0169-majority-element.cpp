class Solution {
public:
    int majorityElement(vector<int>& nums) {
    //    int n=nums.size();
    //     for(int val:nums){
    //         int freq=0;
    //         for(int ele:nums){
    //             if(ele==val){
    //                 freq++;
    //             }
    //          if(freq>n/2){
    //             return ans;
    //         }
    //     }
    //     return();
            
    // }
         int n=nums.size();
         int freq=0,ans=0;
         for(int i=0;i<n;i++){
             if(freq==0){
                 ans=nums[i];
           }
             if(ans==nums[i]){
                freq++;
             }
             else{
                 freq--;
             }
     }
     return ans;
       }
};
    

// int main(){
//     vector<int>nums;
//     int n=nums.size();
//     for(int i=0;i<n;i++){
//         cin>>nums[i];
//     }
//     cout<<majorityElement(vector<int>nums);
//     return 0;
// }