class Solution {
public:
    void solve(string output, int index, string digit, vector<string>& ans, string mapping[]) {
        if(index == digit.size()){
            ans.push_back(output);
            return;
        }
        
        int number = digit[index] - '0'; 
        string value = mapping[number];
        
        for(int i = 0; i < value.size(); i++){
            output.push_back(value[i]);
            solve(output, index + 1, digit, ans, mapping); 
            output.pop_back(); 
        }
    }

    vector<string> letterCombinations(string digits) {
        vector<string> ans;
        if(digits.length() == 0) {
            return ans;
        }
        
        string output = "";
        int index = 0;
        string mapping[10] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        
        solve(output, index, digits, ans, mapping);
        return ans;
    }
};