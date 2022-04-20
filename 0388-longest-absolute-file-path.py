class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        ans, i, n = 0, 0, len(input)
        while i < n:
            # 统计当前文件的深度，连续的\t代表深度++
            depth = 1
            while i < n and input[i] == '\t':
                depth += 1
                i += 1

            # print('depth = ', depth)

            # 统计当前文件名的长度
            length = 0
            isFile = False
            while i < n and input[i] != '\n':
                if input[i] == '.':
                    isFile = True

                length += 1
                i += 1

            i += 1  # 跳过换行符
            # print('stack = ', stack)
            while len(stack) >= depth:
                stack.pop()

            if stack:
                length += stack[-1] + 1

            if isFile:
                ans = max(ans, length)
            else:
                stack.append(length)

        return ans


if __name__ == '__main__':
    s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    # s = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print(s)
    sol = Solution()
    print(sol.lengthLongestPath(s))
