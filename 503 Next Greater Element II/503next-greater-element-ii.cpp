class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& a) {
        int n = a.size();
    vector<int> fin(n,-1);
    vector<int> v1(2*n,-1);
    for(int i=0;i<n;i++){
        v1[i] = a[i];
        v1[i+a.size()] = a[i];
    }
    n = v1.size();
    vector<int> ans(n,-1);
    stack<int> st;
	for(int i=n-1;i>=0;i--){
		if(st.empty())
			ans[i] = -1;
		else{
			while(!st.empty() && st.top()<=v1[i])
				st.pop();
			if(st.empty())
				ans[i] = -1;
			else
				ans[i] = st.top();
		}
		st.push(v1[i]);
	}
    for(int i=0;i<a.size();i++){
        fin[i] = ans[i];
    }
	return fin;
    }
};