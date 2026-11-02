class Solution(object):
    def deserialize(self, s):
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ''

        for c in s:
            if c == '[':
                ni = NestedInteger()
                if stack:
                    stack[-1].add(ni)
                stack.append(ni)

            elif c.isdigit() or c == '-':
                num += c

            elif c == ',' or c == ']':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''

                if c == ']':
                    ni = stack.pop()
                    if not stack:
                        return ni