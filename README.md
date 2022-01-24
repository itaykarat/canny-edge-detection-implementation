# canny-edge-detection-implementation

Implementation of the canny edge detection algorithm.

{different classes to support applications S.A webcam, tello drone and manual image edge detection}


![image](https://user-images.githubusercontent.com/60778119/150652706-af7bc78a-247d-4438-983b-5230b410d66a.png)



the first step- noise reduction:

![image](https://user-images.githubusercontent.com/60778119/150652776-15290b96-227f-45c3-a9e6-9b86b2a05828.png)

explanation of gaussian blur:
![image](https://user-images.githubusercontent.com/60778119/150760588-57edef39-f942-4412-a382-49206eb16792.png)



second step - gradient calculation

![image](https://user-images.githubusercontent.com/60778119/150652794-8deb60d4-b472-46a3-8a65-16d8408f9f2a.png)

Case study:

![image](https://user-images.githubusercontent.com/60778119/150760057-fc65706c-98f8-4af5-9808-40c4abd7d1a7.png)
![image](https://user-images.githubusercontent.com/60778119/150759777-9156bf49-096a-4585-8c7f-c25e0a738e49.png)
![image](https://user-images.githubusercontent.com/60778119/150759897-d17fcce0-60f2-4c69-9d83-0600039d2685.png)


example of result of gradients calculation on the image:
![image](https://user-images.githubusercontent.com/60778119/150760309-280151c0-6e5e-436f-8514-5e866f21b74e.png)





third step - Non-Maximum Suppression

![image](https://user-images.githubusercontent.com/60778119/150652811-16506589-455f-42db-a5c4-314f9f12c0f2.png)


fourth step - Double threshold

![image](https://user-images.githubusercontent.com/60778119/150652842-8beabae2-f9ae-44de-8600-d93db11b2730.png)


fifth step - Edge Tracking by Hysteresis

![image](https://user-images.githubusercontent.com/60778119/150652862-5560e84b-f8d7-471d-a664-fd5f5cdcca87.png)
