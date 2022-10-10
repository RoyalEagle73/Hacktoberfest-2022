(defn get_matched_count [actual_labels predicted_labels]
  (loop [index 0 cnt 0]
    (if (= index (count actual_labels))
      cnt
      (recur (inc index) (if (= (get actual_labels index) (get predicted_labels index)) (inc cnt) cnt)))))

(defn get_accuracy [actual_labels predicted_labels]
  (* 100 (/ (get_matched_count actual_labels predicted_labels) (count actual_labels))))

(defn main [] (
               do (def actual_labels ['Dog','Dog','Cat','Cat','Cat'])
                  (def predicted_labels ['Cat','Dog','Cat','Dog','Cat'])
                  (int (get_accuracy actual_labels predicted_labels))))

(main)