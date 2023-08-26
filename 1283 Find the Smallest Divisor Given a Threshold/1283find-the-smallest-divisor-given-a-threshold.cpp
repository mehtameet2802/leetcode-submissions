class Solution {
public:
    int ans = INT_MAX;
    
    void bin(int s,int e,int h,vector<int> arr){
        while(s<=e){
            int mid = s+(e-s)/2;
            long long int a1 = 0;
            for(int i=0;i<arr.size();i++){  
                a1+=((arr[i]+mid-1)/mid);
            }
            if(a1<=h){
                ans = min(ans,mid);
                e = mid-1;
            }
            else if(a1>h)
                s = mid+1;
        }
    }

    int smallestDivisor(vector<int>& nums, int threshold) {
        sort(nums.begin(),nums.end());
        int s = 1;
        int e = nums[nums.size()-1];
        bin(s,e,threshold,nums);
        return ans;
    }
};