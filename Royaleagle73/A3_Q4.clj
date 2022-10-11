(def N 2000)

(defn soe [] (
             loop [index 2
                   sieve (vec (repeat N true))] (if (> index (Math/sqrt N))
                                          (vec (keep-indexed #(if (and (true? %2) (> %1 1)) %1) sieve))
                                          (recur (inc index) (if (= (get sieve index) true) (loop [jindex 2
                                                                                                   updated_sieve sieve] (if (> (* jindex index) N)
                                                                                                                          updated_sieve
                                                                                                                          (do
                                                                                                                            (recur (inc jindex) (assoc updated_sieve (* jindex index) false))))) sieve)))
))

(defn get_primes [N, sieve] (filter #(if (<= %1 N) %1) sieve))

(defn main [] (do (def n1 5)
                  (def n2 10)
                  (def sieve (soe))
                  (println (get_primes n1, sieve))
                  (println (get_primes n2, sieve))
                  ))

(main) 
