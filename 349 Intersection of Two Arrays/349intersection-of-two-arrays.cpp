class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> s;
        vector<int> v1;
        
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        
        int n = nums1.size();
        int m = nums2.size();
        int i=0;
        int j=0;
        while(i<n && j<m){
            if(nums1[i]<nums2[j]) i++;
            else if(nums2[j]<nums1[i]) j++;
            else{
                s.insert(nums1[i]);
                i++;
                j++;
            }
        }
        
        
        for(auto & s1:s){
            v1.push_back(s1);
        }
        return v1;
    }
};