#https://leetcode.com/problems/course-schedule/

#BASICALLY DETECTING CYCLES IN DIRECTED GRAPH if yes then not possible

#BRUTE FORCE
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a graph as an adjacency list (dictionary of lists)
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        # Fill the graph with edges (course dependencies)
        for pair in prerequisites:
            course = pair[0]
            prereq = pair[1]
            graph[prereq].append(course)

        # Create visited and path tracking arrays
        visited = [False] * numCourses
        path = [False] * numCourses

        # Helper function to do DFS and detect cycles
        def hasCycle(course):
            if path[course]:  # If we're visiting the same course in the current path, cycle!
                return True
            if visited[course]:  # Already checked and safe
                return False

            visited[course] = True
            path[course] = True

            for neighbor in graph[course]:
                if hasCycle(neighbor):
                    return True

            path[course] = False  # Backtrack
            return False

        # Check every course for a cycle
        for i in range(numCourses):
            if hasCycle(i):
                return False  # Cycle found, can't finish all courses

        return True  # No cycle found, all courses can be finished
