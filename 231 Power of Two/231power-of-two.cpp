class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n<0)
            return false;
        int one = 0;
        while(n!=0){
            if(n&1)
                one++;
            n = n>>1;
        }
        if(one == 1)
            return true;
        return false;
    }
};