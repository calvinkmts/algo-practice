from typing import List

class Solution:
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        grouped_intervals : List[List[int]] = []

        sorted_intervals = sorted(intervals, key=lambda x: (x[0], -(x[1] - x[0])))

        # print(f"sorted_intervals: {sorted_intervals}")

        grouped_intervals.append(sorted_intervals[0])

        for i in range(1, len(sorted_intervals)):

            # print(grouped_intervals)

            # check first all the grouped_intervals element
            can_append_interval = True
            can_merged_index = -1
            for j in range(0, len(grouped_intervals)):
                if not(sorted_intervals[i][0] > grouped_intervals[j][1] or sorted_intervals[i][1] < grouped_intervals[j][0]):

                    can_merged_index = j # index to add the current_sorted_intervals
                    can_append_interval = False

            if can_append_interval:
                grouped_intervals.append(sorted_intervals[i])
                continue

            # extend left
            if grouped_intervals[can_merged_index][0] > sorted_intervals[i][0] and grouped_intervals[can_merged_index][1] >= sorted_intervals[i][1]:
                grouped_intervals[can_merged_index][0] = sorted_intervals[i][0]
            # extend right
            elif grouped_intervals[can_merged_index][0] <= sorted_intervals[i][0] and grouped_intervals[can_merged_index][1] < sorted_intervals[i][1]:
                grouped_intervals[can_merged_index][1] = sorted_intervals[i][1]
            # extend both
            elif grouped_intervals[can_merged_index][0] > sorted_intervals[i][0] and grouped_intervals[can_merged_index][1] < sorted_intervals[i][1]:
                grouped_intervals[can_merged_index][0] = sorted_intervals[i][0]
                grouped_intervals[can_merged_index][1] = sorted_intervals[i][1]


        return grouped_intervals
    '''

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        grouped_intervals : List[List[int]] = []
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], -(x[1] - x[0])))

        grouped_intervals.append(sorted_intervals[0])
        grouped_intervals_index = 0

        for i in range(1, len(sorted_intervals)):

            # check merge or append
            if sorted_intervals[i][0] <= grouped_intervals[grouped_intervals_index][1]:
                grouped_intervals[grouped_intervals_index][1] = max(grouped_intervals[grouped_intervals_index][1], sorted_intervals[i][1])
            else:
                grouped_intervals.append(sorted_intervals[i])
                grouped_intervals_index += 1

        return grouped_intervals


if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(solution.merge([[1,4],[4,5]]))
    print(solution.merge([[2,3],[4,5],[6,7],[8,9],[1,10],[1,8]]))
    print(solution.merge([[1,4],[0,0]]))
    print(solution.merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))
