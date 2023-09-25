class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int ans = INT_MIN;
        int left = 0;
        int right = 0;
        queue<int> q1;
        int ze = 0;
        for(right;right<nums.size();right++){
            if(nums[right]==0){
                ze++;
                q1.push(right);
            }
            if(ze>k){
                left = max(left,q1.front()+1);
                q1.pop();
                ze--;
            }
            ans = max(ans,right-left+1);
        }
        return ans;
    }
};