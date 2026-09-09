#define ll long long
class Solution {
public:
    long long countCommas(long long n) { //tc-O(logn) with base 1000
        ll result=0;
        ll l_bound=1000;
        ll comma=1;
        while(l_bound<=n){
            ll u_bound=(l_bound*1000)-1;
            if(u_bound>n) u_bound=n;
            ll count=u_bound-l_bound+1;
            result+=count*comma;
            l_bound*=1000;
            comma++;
        }
        return result;
    }
};