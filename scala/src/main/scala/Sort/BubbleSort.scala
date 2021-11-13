package Sort

import scala.util.control.Breaks._

object BubbleSort {

  // arrayを昇順にソートする
  def bubbleSort(array: Array[Int]): Array[Int] = {
    breakable(
      for (_ <- array.indices) {
        var swap = false

        for (i <- 0 to array.length - 2) {
          if (array(i) > array(i + 1)) {
            val temp = array(i)
            array(i) = array(i + 1)
            array(i + 1) = temp
            swap = true
          }
        }

        if (!swap) {
          break()
        }
      }
    )

    array
  }
}