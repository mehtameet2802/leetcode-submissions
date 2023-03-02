class CustomStack {
public:
    int j;
    int n;
    int *st;

    CustomStack(int maxSize) {
        st = new int[maxSize];
        j = -1;
        n = maxSize;
    }
    
    void push(int x) {
        if(j<n && j!=n-1){
            j++;
            st[j] = x;
        }
    }
    
    int pop() {
        if(j==-1){
            return -1;
        }
        int x = st[j];
        j--;
        return x;
    }
    
    void increment(int k, int val) {
        if(j<=k-1){
            for(int i=0;i<=j;i++){
                st[i] = st[i]+val;
            }
        }
        else{
            for(int i=0;i<k;i++){
                st[i] = st[i]+val;
            }
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */