class Solution {
public:
    int ans = INT_MAX;

    int check(vector<int> arr,int mid,int k){
        int cnt=0;
        int cur=0;
        for(int i=0;i<arr.size();i++){
            if(arr[i]<=mid){
                cur+=1;
                if(cur==k){
                    cnt++;
                    cur=0;
                }
            }
            else{
                cur = 0;
            }
        }
        return cnt;
    }

    int minDays(vector<int>& bloomDay, int m, int k) {
        int s = *min_element(bloomDay.begin(),bloomDay.end());
        int e = *max_element(bloomDay.begin(),bloomDay.end());
        while(s<=e){
            int mid = s+(e-s)/2;
            int a1 = check(bloomDay,mid,k);
            if(a1<m){
                s = mid+1;
            }
            else if(a1>=m){
                ans = min(ans,mid);
                e = mid-1;
            }
        }
        if(ans == INT_MAX)
            return -1;
        return ans;
    }
};