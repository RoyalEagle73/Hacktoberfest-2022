(defn hcf [num_1 num_2] (
                         if (= num_2 0)
                         num_1
                         (hcf num_2 (mod num_1 num_2))
 ))

(defn main [] (do (def num_1 56)
                  (def num_2 98)
                  (hcf (max num_1 num_2) (min num_1 num_2))))
(main)