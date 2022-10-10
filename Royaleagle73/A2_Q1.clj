(defn get_distance_index_pairs [home destinations]
  (sort (loop [index 0 distances {}] (if (= index (count destinations))
                                       distances
                                       (recur
                                        (inc index)
                                        (assoc distances (keyword (str (Math/sqrt (+ (Math/pow (- (get home 0) (get (get destinations index) 0)) 2) (Math/pow (- (get home 1) (get (get destinations index) 1)) 2))))) index)))))
  )

(defn compute_dist [home destinations distance_index_pairs] 
  (loop [index 0
         nearest_distances []] (
      if (= index 5)
            nearest_distances
            (recur 
             (inc index) 
             (merge nearest_distances (get destinations (get (get distance_index_pairs index) 1))))
  )))

(defn main [] (
  do
  (def home [0 0])
  (def destinations [[5 5] [1 1] [2 2] [3 3] [4 4] [6 6]])
  (def distance_index_pairs (vec (get_distance_index_pairs home destinations)))
  (compute_dist home destinations distance_index_pairs)             
))

(main)