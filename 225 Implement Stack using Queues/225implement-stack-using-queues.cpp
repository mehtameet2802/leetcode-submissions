class MyStack {
public:
    int first1 = -1;
    int first2 = -1;
    int last1 = -1;
    int last2 = -1;
    int q1[100];
    int q2[100];
    MyStack() {
        
    }
    
    void push(int x) {
        if(first1==-1 &&last1 ==-1){
            first1 = 0;
            last1 = 0;
            q1[last1] = x;
        }
        else{
            first2++;
            while(first1<=last1){
                last2++;
                q2[last2] = q1[first1];
                first1++;
            }
            first1 = 0; last1 = 0;
            q1[last1] = x;
            while(first2<=last2){
                last1++;
                q1[last1] = q2[first2];
                first2++;
            }
            first2 = -1; last2 = -1;
        }
    }
    
    int pop() {
        int z = q1[first1];
        q1[first1] = 0;
        if(first1 == last1){
            first1 = -1;
            last1 = -1;
        }
        else{
            first1++;
        }
        return z;
    }
    
    int top() {
        return q1[first1];
    }
    
    bool empty() {
        if(first1 == -1 && last1==-1){
            return 1;
        }
        return 0;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */