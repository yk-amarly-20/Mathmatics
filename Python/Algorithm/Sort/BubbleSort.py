# バブルソート


class BubbleSort():

    def sort(self, array):
        """
        @param array: 配列,ソートする配列を渡す
        return: ソートされた配列
        """
        length = len(array)
        for i in range(length - 1, 0, -1):
            for j in range(i):
                if array[j] > array[j + 1]:
                    tmp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = tmp

        return array


if __name__ == "__main__":
    bs = BubbleSort()
    array = [1, 3, 6, 4, 2, 7, 5]
    array_sorted = bs.sort(array)
    print(array_sorted)
