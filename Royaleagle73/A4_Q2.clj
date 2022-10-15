(defn digit [number index] (- (int (get number index)) 48) )

(defn strip-zero [number] (if (= (digit number 0) 0)
                            (subs number 1)
                            number))

(defn is-power-of-two? [number] (if (and (odd? (digit number (- (count number) 1)))
                                         (not= (strip-zero number) "1"))
                                  0
                                  (if (and (= (count (strip-zero number)) 1)
                                           (or (= (digit (strip-zero number) 0) 2)
                                               (= (digit (strip-zero number) 0) 1)))
                                    1
                                    (is-power-of-two? (loop [index 0
                                                             carry 0
                                                             result (strip-zero number)] (if (= index (count result))
                                                                                           result
                                                                                           (recur
                                                                                            (inc index)
                                                                                            (if (odd? (digit result index)) 1 0)
                                                                                            (str (subs result 0 index)
                                                                                                 (str (int (/ (+ (* 10 carry) (digit result index)) 2)))
                                                                                                 (subs result (+ 1 index))))))))))

(defn main [] (do (def n "36893488147419103232") ; 2^65 = 36893488147419103232
                  (is-power-of-two? n) 
                  ))

(main)
