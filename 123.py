'''
1) 设置变量.jump代表	的位置，初始化为0;
2)	设置变量max_index代表从第0位置至第jump位置这个过程中，最远可到达的位置， 初始化为indcx[0]。
3. 利用jump扫描index数组，直到jump达到index数组尾部或jump超过max_index，扫描过程中，
更新max_index。
4. 若最终jump为数组长度	，则返回true,否则返回false。
'''
class Solution:
    def Jump(self, nums, n):
        dp = [0] * n
        for i in range(4):
            dp[i] = str(nums[i])
        for i in range(4,n):
            dp[i] = self.Sumab(self.Sumab(dp[i-4],dp[i-3]),dp[i-1])
        return dp[n-1]
    def Sumab(self,array1, array2):
        array1 = list(map(int,list(array1)))
        len1 = len(array1)
        array2 = list(map(int, list(array2)))
        len2 = len(array2)
        if len1 <= len2:  # 两种情况，第一种：数组1的长度小于数组2的长度，第二种情况反过来。
            minlen = len1  # 较大和较小的数组长度
            maxlen = len2
            ans = [0 for x in range(maxlen)]  # 新建立一个与
            ans = [0 for x in range(maxlen)]  # 新建立一个与较长数组长度一致的全为0的数组
            ans[-minlen:] = array1  # 数组的后一部分保存较短数组的值
            # print ans
            for i in range(1, maxlen + 1):
                i = -i  # 从数组尾部开始算
                temp = ans[i] + array2[i]
                if temp >= 10:  # 如果和大于10，则保留个位数值，并进位
                    temp = temp - 10
                    ans[i] = temp

                    if i == -maxlen:  # 数组的第一位，进位后超出数组范围，用python的insert函数，在数组前插入数值
                        ans.insert(0, 1)
                    else:  # 如果没有超出数组范围，则直接在新建的数组的前一位加1
                        ans[i - 1] = ans[i - 1] + 1
                else:
                    ans[i] = temp
                    # print ans
        else:  # 第二种情况
            minlen = len2
            maxlen = len1
            ans = [0 for x in range(maxlen)]
            ans[-minlen:] = array2
            for i in range(1, maxlen + 1):
                i = -i
                temp = ans[i] + array1[i]
                if temp >= 10:
                    temp = temp - 10
                    ans[i] = temp
                    if i == -maxlen:
                        ans.insert(0, 1)
                    else:
                        ans[i - 1] = ans[i - 1] + 1
                else:
                    ans[i] = temp

        return ans
