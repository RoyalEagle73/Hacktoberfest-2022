(defn merge-two-sorted [vec_1 vec_2] (
                          loop [index_1 0
                                index_2 0
                                result []] (
                                            if (or (= index_1 (count vec_1))
                                                   (= index_2 (count vec_2)))
                                            (
                                             if (= index_1 (count vec_1))
                                             (apply conj result (subvec vec_2 index_2))
                                             ( if (= index_1 (count vec_1))
                                              (apply conj result (subvec vec_1 index_1))
                                              result)
                                            )
                                            (if (< (get vec_1 index_1) (get vec_2 index_2))
                                              (recur (inc index_1) index_2 (conj result (get vec_1 index_1)))
                                              (recur index_1 (inc index_2) (conj result (get vec_2 index_2))))
                                )
))

(defn main [] (do (def A [-1 2 4])
                  (def B [-1 -1 1 3 5])
                  (merge-two-sorted A B)))

(main)