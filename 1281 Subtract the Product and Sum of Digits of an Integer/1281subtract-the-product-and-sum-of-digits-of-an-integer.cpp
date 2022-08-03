class Solution {
public:
    int subtractProductAndSum(int n) {
        int t;
        int sum = 0;
        int pro = 1;
        for(int i=0;n>0;i++){
            t= n%10;
            n= (n-t)/10;
            sum = sum+t;
            pro = pro*t;
        }
        return pro-sum;
    }
};