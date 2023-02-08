class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        // vector<uint32_t> v;
        // int x = 32;
        // while(x!=0){
        //     v.push_back(n&1);
        //     n=n>>1;
        //     x--;   
        // }
        // for(int i=0;i<v.size();i++){
        //     cout<<v[i];
        // }  
        // cout<<endl;
        // for(int i=0;i<v.size();i++){
        //     cout<<v[i];
        // }  
        // uint32_t ans=0;
        // for(int i=0;i<32;i++){
        //     ans = ans<<1;
        //     ans = ans|v[i];
        //     cout<<"ans = "<<ans;
        // }
        uint32_t  ans= 0;
        for(int i=0; i<32; i++){
		    ans = ans<<1;
			ans  |=  (n&1);
			n >>= 1;
		}
        return ans;
    }
};