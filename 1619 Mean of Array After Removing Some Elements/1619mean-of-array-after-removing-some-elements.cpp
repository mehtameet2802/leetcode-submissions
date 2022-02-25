class Solution {
public:
    double trimMean(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        double x = 0.05*arr.size();
        arr.erase(arr.begin(),arr.begin()+x);
        for(int i=0;i<x;i++){
            arr.pop_back();
        }
        double s = accumulate(arr.begin(),arr.end(),0);
        return s/arr.size();
    }
};