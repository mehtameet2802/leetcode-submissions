class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        '''
        TC - O(N*L*4) , L is 8 so O(N)
        SC - O(N)
        N is number of strings in bank
        '''

        bank = set(bank)
        
        if endGene not in bank:
            return -1
        
        if startGene == endGene:
            return 0
        
        opt = ['A','C','G','T']
        queue = deque([(startGene,0)])

        while queue:
            string, mutations = queue.popleft()

            if string == endGene:
                return mutations

            for i, ch in enumerate(string):
                for gene in opt:
                    if ch != gene:
                        cur_string = list(string)
                        cur_string[i] = gene
                        cur_string = "".join(cur_string)

                        if cur_string == endGene:
                            return mutations + 1
                        
                        if cur_string in bank:
                            bank.remove(cur_string)
                            queue.append((cur_string, mutations+1))

        return -1     


        