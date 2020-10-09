class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        all_fav_list = list(set(list1).intersection(set(list2)))
        fav_list = []
        min_fav_index_sum = len(list1) + len(list2)
        # print(all_fav_list)
        for f in all_fav_list:
            s = list1.index(f) + list2.index(f)
            if s < min_fav_index_sum:
                fav_list = []
                fav_list.append(f)
                min_fav_index_sum = s
            elif s == min_fav_index_sum:
                fav_list.append(f)
        return fav_list
