class Solution {
public:
    int ans = INT_MAX;

    int check(vector<int> arr,int c){
        int d = 0;
        int cur = 0;
        for(int i=0;i<arr.size();i++){
            if(c<arr[i])
                return -1;
            cur+=arr[i];
            if(cur==c){
                d+=1;
                cur=0;
            }
            else if(cur>c){
                d+=1;
                cur = arr[i];
            }   
        }
        if(cur>0 && cur<=c)
            d+=1;
        else if(cur>c)
            return -1;
        return d;
    }
    
    void bin(int s,int e,int h,vector<int> arr,int c,int mc){
        while(s<=e){
            int mid = s+(e-s)/2;
            if(mid<mc){
                s=mid+1;
                continue;
            }  
            int val = check(arr,mid);
            if(val==-1 || val>h)
                s=mid+1;
            else if(val<=h){
                ans = min(ans,mid);
                e = mid-1;
            }
        }
    }

    int shipWithinDays(vector<int>& weights, int days) {
        int cap = 0;
        int mc = INT_MIN;
        for(int i=0;i<weights.size();i++){
            cap+=weights[i];
            mc = max(mc,weights[i]);
        }
        int n = weights.size();
        int s = 1;
        int e = cap;
        bin(s,e,days,weights,cap,mc);
        return ans;
    }
};