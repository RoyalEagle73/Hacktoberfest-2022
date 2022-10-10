(defn increase_price [menu items] (loop [index 0
                                         new_menu menu] (if (= index (count items))
                                                          new_menu
                                                          (recur (inc index) (loop [menu_index 0] (if (or
                                                                                                       (= menu_index (count menu))
                                                                                                       (= (get items index) (get (get menu menu_index) 0)))
                                                                                                    (update new_menu menu_index (fn [n] (update n 1 #(float (with-precision 3 :rounding FLOOR (* % 1.1))))))
                                                                                                    (recur (inc menu_index))))))))

(defn main [] (do
                (def menu [["Sweet_Corn_Soup", 300.0], ["Cream_of_Tomato_Soup", 100.0], ["Bacon_and_Cheese", 150.0], ["Honey_Mustard", 230.0], ["Hot_Coffee", 50.0], ["Cold_Coffee", 50.0], ["Egg_Sandwiches", 130.0], ["Tacos", 400.0]])
                (def items ["Hot_Coffee" "Cold_Coffee" "Tacos"])
                (increase_price menu items)))

(main)