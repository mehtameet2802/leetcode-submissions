class Solution {
public:
    int splitNum(int num) {
        vector<int> v;
        while(num!=0){
            v.push_back(num%10);
            num = num/10;
        }
        sort(v.begin(),v.end());
        int a1 = 0;
        int a2 = 0;
        int n = v.size();
        for(int i=0;i<n;i++){
            a1 = a1*10 + v[i];
            if(i+1<n){
                i++;
                a2 = a2*10+v[i];
            }
        }
        return a1+a2;
    }
};