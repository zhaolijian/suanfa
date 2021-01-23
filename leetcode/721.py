# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。
# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，
# 因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。

from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        def find(account):
            if parents[account] != account:
                parents[account] = find(parents[account])
            return parents[account]

        def union(account1, account2):
            root = find(account2)
            parents[find(account1)] = root
            while account1 != root:
                parents[account1] = root
                account1 = parents[account1]

        # 邮箱:用户键值对
        account_dict = {}
        parents = {}
        for account in accounts:
            for i in range(1, len(account)):
                if account[i] not in parents:
                    parents[account[i]] = account[i]
                    account_dict[account[i]] = account[0]
            for i in range(2, len(account)):
                union(account[i], account[1])

        emails = defaultdict(set)
        for key in account_dict.keys():
            root = find(key)
            if root in emails:
                emails[root].add(key)
            else:
                emails[root] = {key}
        res = []
        for email in emails:
            temp = [account_dict[email]]
            temp += sorted(list(emails[email]))
            res.append(temp)
        return res


if __name__ == '__main__':
    s = Solution()
    accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],
                ["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
    print(s.accountsMerge(accounts))