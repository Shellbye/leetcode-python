class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        start_pos = 0
        for start in range(len(gas)):
            gas_index_list = range(start, len(gas)) + range(0, start + 1)
            # print(start, gas_index_list)
            car = 0
            ok = True
            for i in gas_index_list:
                car += gas[i]
                car -= cost[i]
                # print(car)
                if car < 0:
                    # print("not ok")
                    ok = False
                    break
                # else:
                    # print("ok")
            if ok:
                return start
        return -1
