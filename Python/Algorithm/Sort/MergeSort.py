# マージソート


class MergeSort():
    def sort(self, array):
        """
        @param array: ソートしたい配列
        return: ソートした配列
        """

        mid = len(array)
        if mid > 1:
            left = sort(array[: mid / 2])
            right = sort(array[: mid / 2])
            array = []
            while len(left) != 0 and len(right) != 0:
                if left[0] < right[0]:
                    array.append(left.pop())
