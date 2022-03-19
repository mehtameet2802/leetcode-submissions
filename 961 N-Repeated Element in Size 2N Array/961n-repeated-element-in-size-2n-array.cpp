class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int x;
        for(int i=0;i<nums.size()-1;i++){
            int count = 0;
            if((nums[i] == nums[i+1]) && x!=nums[i]){
                x = nums[i];
                count++;
            }
            if(x == nums[i]){
                count++;
            }
            if(2*count == nums.size()){
                break;
            }
        }
        return x;
    }
};