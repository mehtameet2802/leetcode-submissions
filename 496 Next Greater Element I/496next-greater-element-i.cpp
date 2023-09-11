class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& arr) {
      stack<int> st;
			int n = arr.size();
			map<int,int> mp;
	    vector<int> ans(nums1.size(),-1);
	    for(int i=n-1;i>=0;i--){
		    if(st.empty())
			    mp[arr[i]] = -1;
		    else{
			    while(!st.empty() && st.top()<=arr[i])
				    st.pop();
			    if(st.empty())
				    mp[arr[i]] = -1;
			    else
				    mp[arr[i]] = st.top();
		    }
		    st.push(arr[i]);
	    }
			for(int i=0;i<nums1.size();i++){
				ans[i] = mp[nums1[i]];
			}
	    return ans;
    }
};