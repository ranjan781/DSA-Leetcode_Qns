class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int low=0;
        int high=arr.size()-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            int missing=arr[mid]-(mid+1); //how much missing no. is happening yet
            if(missing<k){
                low=mid+1;
            }else{
                high=mid-1;
            }
        }
        return k+low;
    }
};


// for(int i=0;i<arr.size();i++){
//             if(arr[i]<=k){
//                 k++;
//             }else{
//                 break;
//             }
//         }
//         return k;