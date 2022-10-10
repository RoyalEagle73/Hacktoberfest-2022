(defn prime_factorization [num] 
  (loop [index 2
         result []
         number num] (if (> index (Math/sqrt num))
                       result
                       (recur (if (= (mod number index) 0) index (inc index)) (if (= (mod number index) 0) (merge result index) result)
                              (if (= (mod number index) 0) (int (/ number index)) number)))))

(defn main [] (
               do (def num 56)
               (if (< num 2) [] (prime_factorization num))
))

(main)