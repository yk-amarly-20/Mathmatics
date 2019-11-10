# 二分探索木


class Node():
    """
    ノードクラス
    各ノードを作成
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST():
    def __init__(self, number_list):
        """
        コンストラクタ
        @param nmuber_list: 追加するノード
        """
        self.root = None
        for node in number_list:
            self.insert(node)

    def insert(self, data):
        """
        @param data: 挿入するdata
        """
        n = self.root

        if n == None:
            self.root = Node(data)
            return
        else:
            while True:
                entry = n.data

                if entry < data:
                    if n.right == None:
                        n.right = Node(data)
                        return
                    n = n.right
                elif entry > data:
                    if n.left == None:
                        n.left = Node(data)
                        return
                    n = n.left
                else:
                    n.data = data
                    return

    def search(self, search):
        searcher = self._search_bool(search)
        if searcher == None:
            print("存在しません")
        elif searcher == True:
            print(str(search) + " は見つかりました!")
        elif searcher == False:
            print(str(search) + " は見つかりませんでした...")

    def _search_bool(self, search):
        n = self.root
        if n == None:
            return None
        else:
            lst = []
            lst.append(n)
            while len(lst) > 0:
                node = lst.pop()
                if node.data == search:
                    return True
                if node.right != None:
                    lst.append(node.right)
                if node.left != None:
                    lst.append(node.left)
            return False


if __name__ == '__main__':
    bst = BST([1, 5, 6, 3, 7, 8, 10, 11, 56])
    bst.search(29)
