(defn eligible [record] (
                        or (and 
                            (> (/ (get record 1) (get record 3)) 4)
                            (> (get record 2) 2))
                         (and
                          (< (/ (get record 1) (get record 3)) 4)
                          (> (get record 2) 4))
))

(defn man_of_the_match [records] (loop [index 0
                                        man_of_the_match_final "None"
                                        final_records {}] (
                                                              if (= index (count records))
                                                              [final_records man_of_the_match_final]
                                                                    (recur (inc index) (
                                                                                       if(= (eligible (get records index)) true)
                                                                                        (get (get records index) 0)
                                                                                        man_of_the_match_final
                                                                    )
                                                                           (assoc final_records (keyword (get (get records index) 0)) [(get (get records index) 1)
                                                                                                                                       (get (get records index) 2)
                                                                                                                                       (get (get records index) 3)]))
                                        )))

(defn main [] (do (def records [["Arun" 25 3 7]
                                ["Nihal" 50 5 12]
                                ["Sanjay" 10 4 3]])
                  (man_of_the_match records)))
(main)
