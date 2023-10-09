#!/usr/bin/env python
## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import os
import rospy
from std_msgs.msg import Float32
import dearpygui.dearpygui as dpg

def subscribe_cb(data):
    if dpg.get_value("checkbox_sub"):
        dpg.set_value("slider1", data.data)


def main():
    rospy.init_node('dearpy_listener', anonymous=False)
    sub = rospy.Subscriber('slider_value', Float32, subscribe_cb)    # コールバックを一旦設定すれば、トピックは勝手に処理される

    #-------- DearPy GUI ---------------------
    dpg.create_context()
    dpg.create_viewport(title=os.path.basename(__file__), width=810, height=310)
    dpg.set_global_font_scale(2.5)

    with dpg.window(label="window", width=800, height=300 ,pos=[5,5]):
        dpg.add_slider_float(tag="slider1",label="SLIDER",default_value=0, max_value=100,min_value=-100)
        dpg.add_checkbox(label="sub", tag="checkbox_sub", default_value=True)
        dpg.add_text('',tag="Status")

    dpg.setup_dearpygui()
    dpg.show_viewport()
    
    rate = rospy.Rate(10) # 10hz
    #while not rospy.is_shutdown():
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        rate.sleep()
        
    dpg.destroy_context()

if __name__ == '__main__':
    main()
