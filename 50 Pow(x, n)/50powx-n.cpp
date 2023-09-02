class Solution {
public:
    double myPow(double x, int n) {
        long long int c1 = abs(n);
        double ans=1;
        if(n==0 || x==1)
            return 1.0;
        if(x==-1){
            if(n%2==0)
                return 1.0;
            return -1.0;
        }
        while(c1!=0){
            if(c1%2==0){
                x = x*x;
                c1 = c1/2;
            }
            else{
                ans=ans*x;
                c1--;
            }
        }
        if(n<0){
            return 1/ans;
        }
        return ans;
    }
};