(defn check_equal [string_1 string_2] (
                      loop [index 0
                            result "Not Same"
                            string_new string_2] (if (or
                                                      (= index (count string_1))
                                                      (= result "Same"))
                                                   result
                                                   (recur (inc index)
                                                          (if (= string_new string_1)
                                                            "Same"
                                                            "Not Same")
                                                          (str (subs string_new 1 (count string_new)) (subs string_new 0 1))))
))

(defn main [] (do (def string_1 "abcde")
                  (def string_2 "cdeab")
                  (if (= (count string_1) (count string_2))
                    (check_equal string_1 string_2) 
                    "Not Same")))

(main)
