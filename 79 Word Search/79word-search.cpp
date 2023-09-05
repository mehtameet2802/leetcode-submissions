class Solution {
public:

    bool solve(vector<vector<char>> &boa,string word,int ind,int i,int j,int m,int n,string s1){
        // cout<<s1<<ind<<endl;
        if(s1==word)
            return true;
        if(ind>=word.size())
            return false;
        char cur = boa[i][j];
        bool ans = false;
        boa[i][j] = '1';
        if(i+1>=0 && i+1<m && j>=0 && j<n && boa[i+1][j]!='1' && boa[i+1][j]==word[ind+1])
            ans = solve(boa,word,ind+1,i+1,j,m,n,s1+boa[i+1][j]);
        
        if(ans)
            return ans;
        
        if(i-1>=0 && i-1<m && j>=0 && j<n && boa[i-1][j]!='1' && boa[i-1][j]==word[ind+1])
            ans = solve(boa,word,ind+1,i-1,j,m,n,s1+boa[i-1][j]);
        
        if(ans)
            return ans;
        
        if(i>=0 && i<m && j+1>=0 && j+1<n && boa[i][j+1]!='1' && boa[i][j+1]==word[ind+1])
            ans = solve(boa,word,ind+1,i,j+1,m,n,s1+boa[i][j+1]);
        
        if(ans)
            return ans;
        
        if(i>=0 && i<m && j-1>=0 && j-1<n && boa[i][j-1]!='1' && boa[i][j-1]==word[ind+1])
            ans = solve(boa,word,ind+1,i,j-1,m,n,s1+boa[i][j-1]);
        
        if(ans)
            return ans;

        boa[i][j] = cur;
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        for(int i=0;i<board.size();i++){
            for(int j=0;j<board[0].size();j++){
                if(board[i][j]==word[0]){
                    string s1 = "";
                    s1+=word[0];
                    bool ans = solve(board,word,0,i,j,board.size(),board[0].size(),s1);
                    if(ans)
                        return ans;
                }
            }
        } 

        return false;  
    }
};