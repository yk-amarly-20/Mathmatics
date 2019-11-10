# 選択ソート


class SelectionSort():

    def sort(self, array):
        """
        @param array: ソートする配列
        return: ソートされた配列
        """

        length = len(array)

        for ind, ele in enumerate(array):
            min_ind = min(range(ind, length), key=array.__getitem__)
            array[ind], array[min_ind] = array[min_ind], array[ind]
        return array


if __name__ == '__main__':
    array = [1, 6, 4, 2, 7, 5, 3]
    ss = SelectionSort()
    array = ss.sort(array)
    print(array)
