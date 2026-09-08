class Solution {
protected: 
    int date_to_day(string date){
            int M=stoi(date.substr(0,2));
            int D=stoi(date.substr(3,2));
            int total=D;
            for(int m=1;m<M;m++) total+=days_in_month(m);
            return total;
        }
    int days_in_month(int m){
        if(m==1 || m==3 || m==5 || m==7 || m==8 || m==10 || m==12) return 31;
        if(m==2) return 28;
        else return 30;
    }
public:
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        int alicestart=date_to_day(arriveAlice);
        int aliceLeave=date_to_day(leaveAlice);
        int bobstart=date_to_day(arriveBob);
        int bobleave=date_to_day(leaveBob);
        int start=max(alicestart,bobstart);
        int end=min(aliceLeave,bobleave);
        if(start>end) return 0;
        return end-start+1;
    }
};