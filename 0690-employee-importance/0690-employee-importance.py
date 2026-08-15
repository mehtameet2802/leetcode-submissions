"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        '''
        TC = O(V + E)
        SC = O(V + H)
        '''
        graph = {}

        for employee in employees:
            graph[employee.id] = employee
        
        def helper(employee):
            
            total = employee.importance
            for sub in employee.subordinates:
                total += helper(graph[sub])
            
            return total
        
        return helper(graph[id])

        
        
        