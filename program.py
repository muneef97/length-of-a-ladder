import math

def main():
    wall_height = input("Enter the height of the wall in meters.: ")
    ground_distance = input("Enter the distance between wall and ladder base.: ")
    step_1 = int(wall_height)**2 + int(ground_distance)**2
    ladder_length = math.sqrt(step_1)

    print("The length of the ladder is %s", ladder_length)

if __name__ == '__main__':
    main()