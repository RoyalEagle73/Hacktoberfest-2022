(defn maxMod [values] (
                      loop [index 0
                            max_val 0
                            second_max 0] (if (= index (count values))
                                            (mod second_max max_val)
                                            (if (>= (get values index) max_val)
                                              (recur (inc index) (get values index) max_val)
                                              (if (and 
                                                   (< (get values index) max_val)
                                                   (> (get values index) second_max))
                                                (recur (inc index) max_val (get values index))
                                                (recur (inc index) max_val second_max)))
)))

(defn main [] (
               do (def a [1 2 44 3])
               (def b [2, 6, 4])
               (println (maxMod a))
               (println (maxMod b))
))

(main)