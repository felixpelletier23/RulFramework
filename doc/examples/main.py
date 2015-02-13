import rule_python as rule
import math


def update(vision_frames, referee_commands):

    print("into Python")
    if vision_frames:
        team = vision_frames[0].teams[0]
        robot = team.robots[0]
        coords = robot.pose.coord
        print("vision_frames[0].teams[0].robots[0].pose.coord.x: "
              + str(coords.x))

    if referee_commands:
        command = referee_commands[0].command
        print("referee_commands[0].command.name: "
              + str(command.name))

    if vision_frames:
        for team in vision_frames[-1].teams:
            for robot in team.robots:
                rc = rule.robot_command()
                rc.is_team_yellow = team.team_id == 1
                rc.dribble = True
                rc.dribble_speed = 1
                rc.kick = True
                rc.kick_speed = 2
                rc.robot_id = robot.robot_id
                rc.stop = False
                x = 1000 - robot.pose.coord.x
                y = 1000 - robot.pose.coord.y
                magnitude = math.sqrt(x*x + y*y)
                rc.pose.coord.x = x / magnitude
                rc.pose.coord.y = y / magnitude
                rc.pose.orientation = 0 - robot.pose.orientation
                rule.send_command(rc)