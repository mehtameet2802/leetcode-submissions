class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int max = max_element(arr.begin(),arr.end()) - arr.begin();
        int top = -1;
        int st[arr.size()];
        if(max==0 || max==arr.size()-1){
            return 0;
        }
        for(int i = 0;i<arr.size();i++){
            if(top == -1){
                top++;
                st[top] = arr[i];
            }
            else if(st[top] != arr[i] && arr[i]>st[top] && i<=max){
                top++;
                st[top] = arr[i];
            }
            else if(st[top] != arr[i] && arr[i]<st[top] && i>max){
                top++;
                st[top] = arr[i];
            }
            else if(st[top] == arr[i]){
                return 0;
            }
        }
        
        if(top == arr.size()-1){
                return 1;
            }
            
            return 0;
    }
};