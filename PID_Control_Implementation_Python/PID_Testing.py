from turtle import color, setpos
import matplotlib

matplotlib.use('Agg')



import PID_Control
import time
import matplotlib.pyplot as plt
import numpy as np
import scipy

from scipy.interpolate import BSpline, make_interp_spline


P = 1.2
I = 1
D = 0.001


def test_pid(P=0.2, I = 0.0, D =0.0, L =100):

    """
    PID Testing test cases
    """

    pid = PID_Control.PID(P,I,D)


    pid.Set_Point = 0.0
    pid.setSampleTime(0.01)



    total_sampling = 100

    feedback = 0

    feedback_list = []
    time_list = []
    setpoint_list = []


    print("simulating...")


    for i in range(1, total_sampling):

        pid.update(feedback)

        output = pid.output

        if pid.Set_Point > 0:

            feedback += (output - (1/i))

        if 20 < i < 60:

            pid.Set_Point = 1

        if 60 <= i < 80:

            pid.Set_Point = 0.5

        if i >= 80:

            pid.setkd = 1.3

        time.sleep(0.02)


        feedback_list.append(feedback)
        setpoint_list.append(pid.Set_Point)
        time_list.append(i)



    time_sm = np.array(time_list)
    time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)
    helper_x = make_interp_spline(time_list, feedback_list)
    feedback_smooth = helper_x(time_smooth)


    fig1 = plt.gcf()
    fig1.subplots_adjust(bottom=0.15)

    plt.plot(time_smooth, feedback_smooth, color='red')
    plt.plot(time_list, setpoint_list, color='blue')
    #plt.plot(time_list, feedback_list, color='red')

    plt.xlim((0, total_sampling))

    plt.ylim((min(feedback_list) - 0.5, max(feedback_list) + 0.5))

    plt.xlabel('time (s)')
    plt.ylabel('PID (PV)')

    plt.grid(True) 
    plt.show()
    print("saving...") 
    fig1.savefig('result.png', dpi=100) 

if __name__ == "__main__":
    test_pid(1.2, 1, 0.001, L=50)