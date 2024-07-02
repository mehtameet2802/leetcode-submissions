class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ans = 0;
        int cur = 0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==1)
                cur++;
            else{
                ans = max(cur,ans);
                cur = 0;
            }
        }
        return max(ans,cur);
    }
};