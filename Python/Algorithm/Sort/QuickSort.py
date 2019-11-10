# クイックソート


class QuickSort():
    def sort(self, array):
        """
        @param array: ソートする配列
        return : ソートした配列
        """

        left = []
        right = []
        if len(array) <= 1:
            return array

        ref = array[0]
        ref_count = 0

        for ele in array:
            if ele < ref:
                left.append(ele)
            elif ele > ref:
                right.append(ele)
            else:
                ref_count += 1

        left = self.sort(left)
        right = self.sort(right)

        return left + [ref] * ref_count + right


if __name__ == '__main__':
    array = [2, 3, 1, 6, 8, 7, 5, 4]
    qs = QuickSort()
    array_sorted = qs.sort(array)
    print(array_sorted)
