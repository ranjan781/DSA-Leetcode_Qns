class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int n=gain.size();
        int currentAltitude=0;
        int highestAltitude=currentAltitude;
        for(int altitudegain:gain){
            currentAltitude+=altitudegain;
            highestAltitude=max(highestAltitude,currentAltitude);
        }
        return highestAltitude;
    }
};