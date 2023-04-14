class Solution {
public:
    int minimizeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int a1 = nums[n-1]-nums[2];
        int a2 = nums[n-2]-nums[1];
        int a3 = nums[n-3]-nums[0];
        return min(a1,min(a2,a3));
    }
};