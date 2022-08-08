class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        vector<int> v1;
        int count = 1;
        int n = arr.size();
        if(n==1 || n==2 && arr[0] == arr[1]){
            return true;
        }else if(n==2 && arr[0]!=arr[1]){
            return false;
        }else{
            for(int i=1;i<n;i++){
                if(arr[i] == arr[i-1]){
                    count++;
                }else{
                    v1.push_back(count);
                    count = 1;
                }
                if(i == n-1){
                    v1.push_back(count);
                }
            }
        }
        sort(v1.begin(),v1.end());
        int m = v1.size();
        // for(int i=0;i<m;i++){
        //     cout<<v1[i];
        // }
        for(int i=1;i<m;i++){
            if(v1[i] == v1[i-1]){
                return false;
            }
        }
        return true;
    }
};