class Solution {
public:
    int minMaxDifference(int num) {
        map<int,int> mp;
        vector<int> v1;
        int x = num;
        int a = 0;
        while(x!=0){
            mp[x%10]++;
            v1.push_back(x%10);
            x = x/10;
        }
        reverse(v1.begin(),v1.end());
        int a1 = INT_MIN;
        int a2 = INT_MAX;
        for(int i=0;i<=9;i++){
            if(mp.find(i)!=mp.end()){
                int n1 = 0;
                int n2 = 0;
                for(int j=0;j<v1.size();j++){
                    n1 = n1*10;
                    n2 = n2*10;
                    if(v1[j] == i)
                        n1+=9;
                    else{
                        n1+=v1[j];
                        n2+=v1[j];
                    }
                        
                }
                a1 = max(a1,n1);
                a2 = min(a2,n2);
            }
        }
        return a1-a2;
    }
};