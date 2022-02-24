class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        vector<string> v;
        for(int i=0;i<arr.size();i++){
            int count = 0;
            for(int j=0;j<arr.size();j++){
                if(arr[i] == arr[j]){
                    count++;
                }
            }
            if(count<2){
                v.push_back(arr[i]);
            }
        }
        if(v.size()<k){
            return "";
        }
        return v[k-1];
    }
};