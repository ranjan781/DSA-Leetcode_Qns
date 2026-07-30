class Solution {
public:
    string addStrings(string num1, string num2) {
        string s;
        int i=num1.length()-1;
        int j=num2.length()-1;
        int carry=0;
        while(i>=0||j>=0||carry!=0){
            int sum=carry;
            if(i>=0){
                sum+=num1[i]-'0';
                i--;
            }
            if(j>=0){
                sum+=num2[j]-'0';
                j--;
            }
            s.push_back(sum%10+'0');
            carry=sum/10;
        }
        reverse(s.begin(),s.end());
        return s;
    }
};