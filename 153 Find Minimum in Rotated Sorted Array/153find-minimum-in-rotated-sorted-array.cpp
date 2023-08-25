class Solution {
public:
    int findMin(vector<int>& arr) {
        int  n =arr.size();
        int s = 0;
        int e = n-1;
        int ans = INT_MAX;
        while(s<=e){
            int mid = s+(e-s)/2;
            if(arr[s]<=arr[mid]){
                ans = min(ans,arr[s]);
                s = mid+1;
            }
            else{
                ans = min(ans,arr[mid]);
                e = mid-1;
            }
        }
        return ans;
    }
};