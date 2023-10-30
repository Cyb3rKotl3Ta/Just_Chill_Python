def bouncingBall(h, bounce, window):
    if 0 < h > 0 and 0 < bounce < 1 and window < h:
        passes = 1
        while h * bounce > window:
            h *= bounce
            passes += 2  # Counting both the fall and the bounce back up
        return passes
    else:
        return -1
    
result = bouncingBall(6, 0.66, 1.5)
print(result)  