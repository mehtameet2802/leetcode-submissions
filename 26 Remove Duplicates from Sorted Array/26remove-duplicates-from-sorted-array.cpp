class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int cur = nums[0];
        int count = 1;
        int index = 1;
        for(int i=1;i<nums.size();i++){
            if(nums[i]==cur)
                continue;
            else{
                count++;
                cur = nums[i];
                nums[index] = cur;
                index++;
            }
        }
        return count;
    }
};