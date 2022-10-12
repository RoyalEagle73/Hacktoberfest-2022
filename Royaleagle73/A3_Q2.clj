(defn sum_of_n [n] (if (= n 1)
                     1
                     (/ (* n (+ n 1)) 2)))

(defn get_appearance_matrix [values] (loop [index 0
                          result []] (
                                     if(= index (int (Math/ceil (/ (count values) 2))))
                                          (if (= 0 (mod (count values) 2)) (vec (concat result (reverse result))) (vec (concat result (reverse (subvec result 0 (- (count result) 1))))))
                                          (recur (inc index) (
                                                             merge result (+ 
                                                                           (* 
                                                                            (- 
                                                                             (+ (count values) 2) 
                                                                             (* 2 (+ index 1))) 
                                                                            (+ 1 index)) 
                                                                             (* 2 
                                                                              (sum_of_n index)))
                                          )))
                          ))

(defn xor [values appearance_matrix] (
                   loop [index 0
                         result 0] (
                                     if( = index (count appearance_matrix))
                                    result
                                    (recur (inc index) ( if (= 0 (mod (get appearance_matrix index) 2)) result (bit-xor result (get values index))))
                         ) 
))

(defn main [] (
               do (def A [1 2 3])
               (def B [4 5 7 5])
               (def C [3 4 5])
               (println (xor A (get_appearance_matrix A)))
               (println (xor B (get_appearance_matrix B)))
               (println (xor C (get_appearance_matrix C)))
))

(main)

