class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> mp;
        // int check=0;
        for(int i=0;i<nums.size();i++){
            mp[nums[i]]+=1;
            if(mp[nums[i]]>1){
                return true;
            }
        }
        // if(check==1)
        //     return true;
        return false;
    }
};