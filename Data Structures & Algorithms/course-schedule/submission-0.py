class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i : [] for i in range(numCourses)}
        for crs, req in prerequisites:
            premap[crs].append(req)
        
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if premap[crs] == []:
                return True
            visiting.add(crs)
            for req in premap[crs]:
                if not dfs(req):
                    return False
            visiting.remove(crs)
            premap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True