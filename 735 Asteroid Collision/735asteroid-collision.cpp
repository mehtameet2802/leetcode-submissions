class Solution {
public:
    vector<int> asteroidCollision(vector<int>& ast) {
        stack<int> st;
        for(int i=0;i<ast.size();i++){
            int x = ast[i];
            if(x>0){
                st.push(x);
            }
            else{
                if(st.empty() || st.top()<0)
                    st.push(x);
                else{
                    while(!st.empty() && st.top()>0 && x<0){
                        int y = st.top();
                        st.pop();
                        if(abs(x)<y)
                            x = y;
                        else if(abs(x)==y){
                            x = 0;
                            break;
                        }
                    }
                    if(x!=0)
                        st.push(x);
                }
            }
        }

        vector<int> ans(st.size(),1);
        int n = st.size()-1;
        while(!st.empty()){
            ans[n] = st.top();
            n--;
            st.pop();
        }
        return ans;
    }
};