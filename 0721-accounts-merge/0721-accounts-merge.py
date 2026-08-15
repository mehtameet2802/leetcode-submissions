class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        dsu = DSU(len(accounts))

        email_to_account = {}

        for i, account in enumerate(accounts):
            
            for email in account[1:]:
                if email in email_to_account:
                    dsu.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i
        
        groups = defaultdict(list)

        for email, root in email_to_account.items():
            root = dsu.find(root)
            groups[root].append(email)
        
        ans = []
        for root, emails in groups.items():
            emails.sort()

            ans.append(
                [accounts[root][0]] + emails
            ) 
        


        return ans