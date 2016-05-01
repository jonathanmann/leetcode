class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype List[int]
        """
        range_hash = {}

        r = [0]
        p = 0
        e = 2**p
        previous_place = 0
        current_place = 0
        for i in range(1,num + 1):
            if i == e:
                r.append(1)
                p += 1
                e = 2**p
                previous_place = current_place
                current_place = i
            elif i % 2 == 1:
                r.append(1 + r[-1])
            else:
                r.append(1 + previous_place)
        return r

print Solution().countBits(8)
