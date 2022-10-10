(def input [1 2 3 4 5])
(def N 2)

(defn replaceCube [input] 
  (for [value input]
    (if (= (- (/ value N) (int (/ value N))) 0)
      (* value (* value value))
      (* value 1))))

(replaceCube input)