class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> ans;
        for(int i=0;i<nums.size();i++){
            vector<int> v1;
            int x = nums[i];
            while(x!=0){
                v1.push_back(x%10);
                x = x/10;
            }
            for(int i=v1.size()-1;i>=0;i--){
                ans.push_back(v1[i]);
            }
        }
        return ans;
    }
};