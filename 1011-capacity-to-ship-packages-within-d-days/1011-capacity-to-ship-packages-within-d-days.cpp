class Solution {
public:
    int sumofelement(vector<int>&weights){
        int sum=0;
        for(int i=0;i<weights.size();i++){
            sum+=weights[i];
        }
        return sum;
    }

    int reqday(vector<int>&weights,int mid){
        int days=1;
        int load=0;
        for(int i=0;i<weights.size();i++){
            if(load+weights[i]>mid){
                days=days+1;
                load=weights[i];
            }else{
                load+=weights[i];
            }
        }
        return days;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int low=*max_element(weights.begin(),weights.end());
        int high=sumofelement(weights);
        while(low<=high){
            int mid=low+(high-low)/2;
            int NoofDays=reqday(weights,mid);
            if(NoofDays<=days){
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return low;
    }
};