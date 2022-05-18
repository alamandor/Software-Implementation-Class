class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_of_ints = x ^ y

        xor_string = "{0:b}".format(xor_of_ints)

        print(xor_string)
        # Need to count where the bits are 1 now
        cnt = 0
        for bit in xor_string:
            if bit == '1':
                cnt += 1

        return cnt
