     total_R = 0
     reward = R
     
-    for _ in range(1000):
+    epsilon = 0.00001
+    while abs(reward) > epsilon:
         total_R += reward
         reward *= gamma
