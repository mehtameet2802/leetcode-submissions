class Solution {
public:
    long long int x1 = pow(10,9)+7;

    int cal(int x,long long int n){
        int ans = 1;
        while(n!=0){
            if(n%2==0){
                x = x%x1*x%x1;
                n = n/2;
            }
            else{
                ans = ans%x1*x%x1;
                n--;
            }
        }
        return ans%x1;
    }

    int countGoodNumbers(long long n) {
        long long n1 = n/2;
        int c1 = 1;
        int c2 = 1;
        if(n%2==0){
            long long n1 = n/2;
            c1 = cal(5,n1);
            c2 = cal(4,n1);
        }
        else{
            long long n1 = n/2;
            long long n2 = n1+1;
            c1 = cal(4,n1);
            c2 = cal(5,n2);
        }
        return c1%x1*c2%x1;
    }
};