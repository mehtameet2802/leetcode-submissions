class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<int> a;
        vector<string> s;
        int c1 = 0; int c2=0;
        int i=1;
        while(target!=a){
            a.push_back(i);
            s.push_back("Push");
            if(a[c1] == target[c2]){
                c1++;c2++;
            }
            else{
                s.push_back("Pop");
                a.pop_back();
            }
            i++;
        }
        return s;
    }
};