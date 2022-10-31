(defn digit [number index] (- (int (get number index)) 48))

(defn increment-at-place [number index] (str (subs number 0 index) (str (+ 1 (digit number index))) (subs number (+ index 1))))

(defn nines [number] (
                      loop [index 0
                            result true] ( if (or
                                               (= index (count number))
                                               (false? result))
                                          result
                                          (recur (inc index) (
                                                              if (not= (get number index) \9)
                                                              false
                                                              true
                                          )))
))

(defn next_smallest_palindrome [number] (if (and  (= (count number) 1)
                                                  (< (digit number 0) 9))
                                 ; If number is single digit and less than 9, return (digit+1)
                                          (str (+ (digit number 0) 1))
                                          (if (true? (nines number))
                                           ; If number only contains 9, return "1{(size-1) times 0}1"
                                            (str "1" (apply str (repeat (- (count number) 1) \0)) "1")
                                            ; For rest of all
                                            ( loop [start 0
                                                    end (- (count number) 1)
                                                    result number] 
                                             (if (>= start end)
                                             result
                                             (recur (inc start) (dec end) (; if character at start is greater than number at end, replace character at end by character at start
                                                                           if (>= (digit result start) (digit result end))
                                                                            (str (subs result 0 end)  (str (digit result start)) (subs result (+ end 1)))
                                                                            (loop [index (- end 1)
                                                                                   output result] (if (not= (digit output index) 9)
                                                                                                    (str (subs output 0 index)
                                                                                                         (str (+ (digit output index) 1))
                                                                                                         (subs output (+ index 1) end)
                                                                                                         (str (digit (str (subs output 0 index)
                                                                                                                          (str (+ (digit output index) 1))
                                                                                                                          (subs output (+ index 1) end)) start))
                                                                                                         (subs output (+ end 1)))
                                                                                                    (recur (dec index) (str (subs output 0 index)  "0" (subs output (+ index 1)))))))))
                                             ))))

(defn main [] (do
                (def number "23545")
                (next_smallest_palindrome number)))

(main)