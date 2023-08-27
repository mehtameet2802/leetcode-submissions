class Solution {
public:
    int check(vector<int> arr,int mid){
        int cnt =0;
        int cur =0;
        for(int i=0;i<arr.size();i++){
            if(arr[i]>mid)
                return -1;
            if(cur+arr[i]==mid){
                cnt+=1;
                cur =0;
            }
            else if(cur+arr[i]>mid){
                cnt+=1;
                cur = arr[i];
            }
            else
                cur+=arr[i];
        }
        if(cur>0)
            cnt+=1;
        return cnt;
    }

    int ans = INT_MAX;
    int splitArray(vector<int>& nums, int k) {
        int s = 0;
        int e = accumulate(nums.begin(),nums.end(),0);
        while(s<=e){
            int mid = s+(e-s)/2;
            int a1 = check(nums,mid);
            if(a1 == -1){
                s = mid+1;
                continue;
            }
            if(a1<=k){
                ans = min(ans,mid);
                e = mid-1;
            }
            else
                s = mid+1;
        }
        return ans;
    }
};