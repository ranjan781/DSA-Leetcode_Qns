class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.size() > s2.size())
            return false;
        vector<int> freq1(26, 0);
        vector<int> freq2(26, 0);    
        for(char ch : s1) {
            freq1[ch - 'a']++;
        }
        int window = s1.size();      
        for(int i = 0; i < window; i++) {
            freq2[s2[i] - 'a']++;
        }
        if(freq1 == freq2)
            return true;        
        for(int i = window; i < s2.size(); i++) {         
            freq2[s2[i] - 'a']++;       
            freq2[s2[i - window] - 'a']--;
            if(freq1 == freq2)
                return true;
        }
        return false;
    }
};