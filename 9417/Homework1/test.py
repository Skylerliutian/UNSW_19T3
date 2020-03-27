def lengthOfLongestSubstring(s):
    count = 0
    for i in range(len(s)):
        r = s[i]
        for j in s[i+1:]:
            if j not in r:
                r += j
            else:
                break
        if len(r) > count:
            count = len(r)
            print(r)
    return count


nums1 = [1, 3]
nums2 = [2]
x = sorted(nums1+nums2)
length = len(x)
if length % 2 == 0:
    mid = length // 2
    print(f'the median is {(x[mid] + x[mid - 1]) / 2}')
else:
    mid = length // 2
    print(f'the median is {x[mid]}')
