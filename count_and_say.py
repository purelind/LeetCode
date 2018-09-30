class Solution:

    def countAndSay(self, n):
        """

        :param n:
        :return:
        """
        def say_term(term_str):
            resp_term = ''
            count = 1
            for i in range(len(term_str)):
                if i == len(term_str) - 1:
                    resp_term += str(count) + term_str[i]
                elif term_str[i + 1] == term_str[i]:
                    count += 1
                else:
                    resp_term += str(count) + term_str[i]
                    count = 1
            return resp_term

        initial_term = '1'
        term_collection = []
        term_collection.append(initial_term)

        for i in range(n-1):
            term_collection.append(say_term(term_collection[i]))

        return term_collection[-1]

    def say(self, s):
        i = j = 0
        count = 1
        ans = ''
        while i < len(s):
            j += 1
            if j == len(s):
                ans += str(count) + s[i]
                break
            if s[i] == s[j]:
                count += 1
                i += 1
            else:
                ans += str(count) + s[i]
                count = 1
                i += 1
        return ans

    def count_and_say_2(self, n):
        if 1 == n:
            return '1'
        if 2 == n:
            return '11'
        return self.say(self.count_and_say_2(n-1))


if __name__ == '__main__':
    ins = Solution()
    print(ins.count_and_say_2(5))
