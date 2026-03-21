from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

camera = robot.getDevice('camera')
camera.enable(timestep)

while robot.step(timestep) != -1:
    image = camera.getImage()   # gets the current frame
    camera.saveImage('webots_capture.png', 100)
    print('saved webots_capture.png')
    # you can save/process one frame here
    break