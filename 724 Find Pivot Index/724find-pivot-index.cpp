class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int prev = 0;
        int total = 0;
        for(int i=0;i<nums.size();i++){
            total=total+nums[i];
        }
        for(int i=0;i<nums.size();i++){
            if(prev == total-nums[i]-prev){
                return i;
            }
            prev = prev+nums[i];
        }
        return -1;
    }
};