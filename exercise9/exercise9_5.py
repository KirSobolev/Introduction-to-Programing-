from functions import box_volume, ball_volume, pipe_volume
check = True

while check:
    operation = int(input("Select the operation (1-3), 0 stops the application:"))
    if operation == 1:
        width = int(input("Give box width:"))
        height = int(input("Give box height"))
        depth = int(input("Give box depth"))
        result = box_volume(width, height, depth)
        print(f"Box volume: {result} m3")
    elif operation == 2:
        ball_radius = int(input("Give ball radius:"))
        result = ball_volume(ball_radius)
        print(f"Ball volume: {result} m3")
    elif operation == 3:
        pipe_radius = int(input("Give pipe radius:"))
        pipe_length = int(input("Give pipe length:"))
        result = pipe_volume(pipe_radius, pipe_length)
        print(f"Pipe volume: {result} m3")
    elif operation == 0:
        check = False
    else:
        print("Wrong operation")
print("Thank you for using our application")
