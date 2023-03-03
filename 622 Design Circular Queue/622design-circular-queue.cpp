class MyCircularQueue {
public:
    int *arr;
    int j=-1;
    int k=-1;
    int n;
    MyCircularQueue(int k) {
        arr = new int[k];
        n = k;
    }
    
    bool enQueue(int val) {
        cout<<val;
        if(j==-1 && k==-1){
            j=0;
            k=0;
            arr[k] = val;
            return true;
        }
        else if(k==n-1 && j==0){
            return false;
        }
        else if(k==j-1){
            return false;
        }
        else if(k<n-1){
            k++;
            arr[k] = val;
            return true;
        }
        else if(k==n-1){
            k=0;
            arr[k] = val;
            return true;
        }
        return true;   
    }
    
    bool deQueue() {
        if(j==-1 && k==-1)
            return false;
        else if(j==k){
            j=-1;
            k=-1;
            return true;
        }
        else if(j==n-1){
            j=0;
            return true;
        }
        else if(j<k || j<n-1){
            j++;
            return true;
        }
        return true;
    }
    
    int Front() {
        if(j==-1 && k==-1)
            return -1;
        return arr[j];
    }
    
    int Rear() {
        if(j==-1 && k==-1)
            return -1;
        return arr[k];
    }
    
    bool isEmpty() {
        if(j==-1 && k==-1)
            return true;
        return false;
    }
    
    bool isFull() {
        if(j==-1 && k==-1)
            return false;
        else if(j==0 && k==n-1)
            return true;
        else if(j==0 && k<n-1)
            return false;
        else if(k==j-1)
            return true;
        return false;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */