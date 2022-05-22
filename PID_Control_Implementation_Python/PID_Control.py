import math
import time


class PID:

    """PID Controller
    """


    def __init__(self, P=0.2, I=0.0, D=0.0):


        self.kp = P
        self.ki = I
        self.kd = D


        self.sample_time = 0.00
        self.current_time = time.time()
        self.last_time = self.current_time

        self.clear()

    def clear(self):
        """ The Clear method will clear the PID Computations and Coefficients"""



        self.Set_Point = 0.0

        self.PValue = 0.0
        self.IValue = 0.0
        self.DValue = 0.0
        self.last_error = 0.0



        #windup Guard
        self.int_error = 0.0
        self.windup_guard = 20.0

        self.output = 0.0


    def update(self, feedback_value):

        """This method will compute the PID Control Value for the reference feedback provided


        .. math::
        u(t) = K_p e(t) + K_i*int_{0}^{t} + K_d {de}/{dt}

        .. figure:: images/PID.png
           :align:   center


           Test PID with kp = 1.2, ki =1, kd=0.001 with an additional script

        """


        error = self.Set_Point - feedback_value


        self.current_time = time.time()

        delta_time = self.current_time - self.last_time

        delta_error = error - self.last_error



        if (delta_time >= self.sample_time):

            self.PValue = self.kp * error

            self.IValue += error * delta_time

            if (self.IValue < -self.windup_guard):
                self.IValue = -self.windup_guard

            elif (self.IValue > self.windup_guard):
                self.IValue = self.windup_guard



            self.DValue = 0.0

            if delta_time > 0:

                self.DValue = delta_error / delta_time


                #Memorizes the last time and last error for next calculation

                self.last_time = self.current_time

                self.last_error = error


                self.output = self.PValue + (self.ki * self.IValue) + (self.kd * self.DValue)

    def setkp(self, proportional_gain):

        """"Proportional gain determines how fast the system responds, if we increase the kp gain constant it will impact the speed of the control system response"""
        self.kp = proportional_gain

    def setki(self, integral_gain):

        """Integral gain determines how we can correct the errors over time"""

        self.ki = integral_gain

    def setkd(self, derivative_gain):

        """Derivative gain helps in reducing the overshoot of the steady state response of the system"""

        self.kd = derivative_gain

    
    def setWindup(self, windup):

        """Integral windup, also known as integrator windup or reset windup, 
       refers to the situation in a PID feedback controller where 
        a large change in setpoint occurs (say a positive change) and the integral terms accumulates a significant error 
        during the rise (windup), thus overshooting and continuing 
        to increase as this accumulated error is unwound 
        (offset by errors in the other direction). 
        The specific problem is the excess overshooting. """ 


        self.windup_guard = windup

    def setSampleTime(self, sample_time):

        """PID that should be updated at a regular interval. 
        Based on a pre-determined sample time, the PID decides if it should compute or return immediately."""



        self.sample_time = sample_time








    




