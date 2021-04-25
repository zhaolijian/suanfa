# 并查集
# 一个数组【A,B,C,D,E】，依赖关系是【【A,B】【B,C】【D,E】】,根据依赖关系可以分为两堆【A,B,C】【D,E】
class Solution:
    # 文件名、文件依赖关系
    def split_package(self , filenames , relations ):
        def find(filename):
            if init[filename] == filename:
                return filename
            init[filename] = find(init[filename])
            return init[filename]

        # 文件名及它的依赖根节点
        init = {filename: filename for filename in filenames}
        res = set()
        for i, j in relations:
            init[i] = j
        for file in filenames:
            res.add(find(file))
        return len(list(res))


if __name__ == '__main__':
    s = Solution()
    filenames = ["fileA", "fileB", "fileC", "fileD", "fileE"]
    relations = [ ["fileA", "fileB"],  ["fileD", "fileE"]]
    print(s.split_package(filenames, relations))

