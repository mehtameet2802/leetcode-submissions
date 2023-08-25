class Solution {
public:
    vector<int> searchRange(vector<int>& arr, int k) {
        int n = arr.size();
        if(n==0 || k>arr[n-1] || k<arr[0])
            return {-1,-1};
        int s = 0;
        int e = n-1;
        int f = -1;
        int l = -1;
        while(s<=e){
            int mid = s+(e-s)/2;
            if(arr[mid]==k){
                f = mid;
                e = mid-1;
            }
            else if(arr[mid]>k)
                e = mid-1;
            else
                s = mid+1;
        }

        if(f==-1) return {-1,-1};

        s=0;
        e=n-1;
        while(s<=e){
            int mid = s+(e-s)/2;
            if(arr[mid]==k){
                l = mid;
                s = mid+1;
            }
            else if(arr[mid]>k)
                e = mid-1;
            else
                s = mid+1;
        }

        return {f,l};
    }
};