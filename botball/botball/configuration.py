import os
import sys

class RobotConfiguration(object):
    '''
    Stores the configuration for robot-related tasks, such as `choose_game`.
    '''

    @classmethod
    def robot_name(cls):
        '''
        The name of the robot as set by the `BOTBALL_ROBOT_NAME` environment
        variable.
        '''

        robot_name = os.getenv('BOTBALL_ROBOT_NAME')

        if not robot_name and '--ignore-no-config-env' not in sys.argv:
            print('WARNING: Could not find the BOTBALL_ROBOT_NAME environment variable. Defaulting to "demobot".')

        return robot_name or 'demobot'


class ServoConfiguration(object):
    '''
    Stores the configuration for servos.
    '''

    min_raw_position = 98
    '''
    The lowest raw position the servo can travel without potentially causing
    damage.
    '''

    max_raw_position = 1947
    '''
    The highest raw position the servo can travel without potentially causing
    damage.
    '''

    @classmethod
    def raw_position_range(cls):
        '''
        The range starting at `min_raw_position` and ending at `max_raw_position`.
        '''

        return range(cls.min_raw_position, cls.max_raw_position)

    sleep_amount = 0.75
    '''
    The amount of time (in seconds) to wait in between servo movements.

    For simplicity, the `Servo` implementation sleeps for the same amount of
    time, no matter how far the servo traveled. In the future we might make this
    adjust to that amount, but a constant value works for us.
    '''


class MotorConfiguration(object):
    '''
    Stores the configuration for motors.
    '''

    pwm_ticks = 1500
    '''
    The number of PWM ticks that occur per second. Used to control the speed of
    the motor.
    '''

    travel_time_1_cm = 0.04
    '''
    The amount of time (in seconds) it takes to travel 1 cm at full speed. Used
    to calculate how long to block while the motor is traveling.
    '''


class WheelsConfiguration(object):
    '''
    Stores the configuration for wheel controllers.
    '''

    @staticmethod
    def turn_amount(degrees):
        '''
        The distance (in cm) forward the left wheel and backward the right wheel
        should travel when a wheel group is performing a clockwise turn, and
        vice versa.

        This function has been generated using regression for the following turn
        amounts:

        - 45 degrees = 45 * 1.175
        - 90 degrees = 90 * 1.2425
        - 180 degrees = 180 * 1.35
        - 360 degrees = 360 * 1.425
        '''

        if degrees == 45:
            multiplier = 1.175
        elif degrees == 90:
            multiplier = 1.2425
        elif degrees == 180:
            multiplier = 1.35
        elif degrees == 360:
            multiplier = 1.425
        else:
            multiplier = (-2.781096509 * (10 ** -6) * (degrees ** 2) + 1.922759857 * (10 ** -3) * degrees + 1.093333333)

        return degrees * multiplier / 10


class CameraConfiguration(object):
    '''
    Stores the configuration for the camera.
    '''

    channel = 0
    '''
    The channel on which the camera should check for objects. This shouldn't
    need to be changed if you use the provided configuration files.
    '''

    refresh_frames = 20
    '''
    The number of frames the camera should fetch during a refresh before
    tracking objects. The higher the number, the more accurate object tracking
    will be, but the longer it will take for refreshes to occur.
    '''

    confidence_threshold = 0.42
    '''
    The minimum value returned by `get_object_confidence` for an object to be
    recognized by the camera.
    '''

    height_offset = 15
    '''
    The number of pixels to offset the camera boundaries to make object tracking
    more accurate.
    '''


class CreateConfiguration(object):
    '''
    Stores the configuration for the iRobot Create.
    '''

    max_velocity = 500
    '''
    The maximum speed the Create can travel when driving straight, in mm/sec.
    '''

    travel_time_1_cm = 0.02
    '''
    The amount of time (in seconds) it takes to travel 1 cm at max velocity.
    '''
