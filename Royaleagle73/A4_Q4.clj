(defn is-prefix? [string pattern] (if (> (count pattern) (count string))
                                    false
                                    (= pattern (subs string 0 (count pattern)))))

(defn prefix_matching [string_list pattern from_start] (
                                             loop [index (if (true? from_start) 0 (- (count string_list) 1))
                                                   result -1] (if (or (and (true? from_start) (= index (count string_list)))
                                                                      (and (false? from_start) (= index -1))
                                                                      (not= result -1))
                                                                result
                                                                (recur (if (true? from_start) (inc index) (dec index))
                                                                       (if (is-prefix? (get string_list index) pattern) index -1)))
))

(defn prefix [string_list pattern] [(prefix_matching string_list pattern true)
                 (prefix_matching string_list pattern false)])

(defn main [] (do (def string_list ["a" "b"])
                  (def pattern "c")
                  (prefix string_list pattern)))

(main)