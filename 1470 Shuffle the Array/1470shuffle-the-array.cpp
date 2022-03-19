class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> v2;
        int i=0;
        while(i!=(nums.size()/2)){
            v2.push_back(nums[i]);
            v2.push_back(nums[i+n]);
            i++;
        }
        return v2;
    }
};