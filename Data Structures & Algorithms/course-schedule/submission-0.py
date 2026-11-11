class Solution:
    
    def dfs(self,course,visitset,store):
        if course in visitset:
            return False
        if store[course] == []:
            return True

        visitset.add(course)
        for pre in store[course]:
            if not self.dfs(pre, visitset, store):
                return False
        visitset.remove(course)
        store[course] = []
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #This most certainly use dictionaries and it take manipulating them with th correct output.
        #[course I want to take, course i need to take before hand]
        # course -> list of pre-req
        # {course -> list of pre-req}
        # {1:[0]}, {0:[1]}
        store = {}
        for value in prerequisites:
            course = value[0]
            prereq = value[1]
            if course not in store:
                store[course] = [prereq]
            else:
                temp = store[course]
                temp.append(prereq)
                store[course] = temp
        
        for course in range(numCourses):
            if course not in store:
                store[course] = []
        visitset = set()

        for course in range(numCourses):
            if not self.dfs(course,visitset,store):
                return False
        return True

    
