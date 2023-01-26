class Solution {
public:
    typedef pair<int, int> pi;
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<int> diff;
        vector<int> ans;
        for(int i=0;i<arr.size();i++){
            diff.push_back(abs(x-arr[i]));
        }
        // priority_queue<pi,vector<pi>,greater<pi>> pq;
        // for(int i=0;i<arr.size();i++){
        //     pq.push(make_pair(diff[i],arr[i]));
        // }

        vector<pi> v1;
        for(int i=0;i<arr.size();i++){
            v1.push_back(make_pair(diff[i],arr[i]));
        }

        sort(v1.begin(),v1.end());

        int i=0;
        while(i<k){
            ans.push_back(v1[i].second);
            i++;
        }
        sort(ans.begin(),ans.end());
        return ans;
    }
};