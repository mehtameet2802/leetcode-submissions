class StockSpanner {
public:
    int index;
    stack<pair<int,int>> st;
    StockSpanner() {
        index = -1;
    }
        
    int next(int price) {
        index++;
        while(!st.empty() && st.top().first<=price)
            st.pop();
        
        if(!st.empty()){
            pair<int,int> p = st.top();
            st.push(make_pair(price,index));
            return index-p.second;
        }
        st.push(make_pair(price,index));
        return index+1;
        
    }

    
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */