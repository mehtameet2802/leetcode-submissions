class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        vector<vector<int>> ans;
        int x,y;
        x = nums1.size();
        y = nums2.size();
        int x1 = 0;
        int y1 = 0;
        while(x!=0 && y!=0){
            if(nums1[x1][0] == nums2[y1][0]){
                nums1[x1][1] = nums1[x1][1]+nums2[y1][1];
                ans.push_back(nums1[x1]);
                x1++;
                y1++;
                x--;
                y--;
            }
            else if(nums1[x1][0] < nums2[y1][0]){
                ans.push_back(nums1[x1]);
                x1++;
                x--;
            }
            else{
                ans.push_back(nums2[y1]);
                y1++;
                y--;
            }
        }
        
        while(x!=0){
            ans.push_back(nums1[x1]);
            x1++;
            x--;
        }
        
        while(y!=0){
            ans.push_back(nums2[y1]);
            y1++;
            y--;
        }
        return ans;
    }
};