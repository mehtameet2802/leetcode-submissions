class Solution {
public:
    int hammingWeight(uint32_t n) {
        int x = 0;
        while(n!=0){
            int y = n&1;
            if(y==1)
                x++;
            n = n>>1;
        }
        return x;
    }
};