# VR Tracking Data
Please note, this project is under development and the results are constantly being updated.  

Two Franka Emika Panda robots which are following different trajectories. Either human made or computer generated. The human generated trajectories are made using HTC-Vive VR controllers.


<p align="center">
  <img src="./GIFS/demo.gif" title="Hello World!" width="800">
</p>
All the packages to build and run this demo will be available on my github. The code is currently under development and will be released when finished (around June 2020).  
  
The data is generated and collected using the ROS packages:  
* [moveit_vive](https://github.com/Machine-Jonte/moveit_vive), used for controlling and recording data.
* [vive_ros](https://github.com/Machine-Jonte/vive_ros/tree/master), reading controller data and send it as ROS messages (modified version by me).
* [panda_dual_gazebo_moveit_config](https://github.com/Machine-Jonte/panda_dual_gazebo_moveit_config), configuration for MoveIt.
* [panda_dual_gazebo](https://github.com/Machine-Jonte/panda_dual_gazebo), xacro and robot files (modified for working with gazebo). 


# Common Information
To generate 3D trajectory graph run:  
```
cd {where plot_tracking.py is located}
python plot_tracking.py /dir/to/left.csv /dir/to/right.csv
```
To generate 2D graphs run:
```
cd {where plot_graph.py is located}
python plot_graph.py /dir/to/left.csv /dir/to/right.csv
```
## Human Generated
### Handwritten digits
Trying to get the results as close to real performance I decided to only do the digits one time (if possible). The digits are generated with the two arms at the same time. And the digits are hand written (obviously). The first image is left and the second image is right. 

## Computer Generated
### Circle
A circle of different sizes and speed was generated to study the behavior of the system. 
The function used to calculate the circle is:  
<!-- y(t) = r \cdot cos\left(2\pi \frac{1}{T} t\right)-->
<!-- z(t) = r \cdot sin\left(2\pi \frac{1}{T} t\right) -->
<p align="center">
  <img src="./functions/circle/y_function.png" width="200" title="Circle function y.">
</p>
<p align="center">
  <img src="./functions/circle/z_function.png" width="200" title="Circle function z.">
</p>

### Sweep Sine
A computer generated sweep sine wave for controller pose. The sweep sine is following the following function:  
<!-- f(t) = sin(2\pi t \frac{f_1-f_0}{2T} \cdot t^2) -->
<p align="center">
  <img src="./functions/sweepsine/sweep_function.png" width="200" title="Sweep sine function.">
</p>
f0 is starting frequency.  
f1 is ending frequency.  
T is the period time.  
In this test f0 = 0.00001, f1 = 1 and T = 500.  


### Step
The step function increased in size for each period. The function can be described as:  
<!-- g(t) = a(t)\cdot  sign(sin(2\pi ft)) -->
<p align="center">
  <img src="./functions/step/function.png" width="200" title="Step function.">
</p>
<!-- a(t) = int(tf) \cdot c, \text{ where } c = 0.01 -->
<p align="center">
  <img src="./functions/step/a_function.png" width="200" title="a(t) function.">
</p>
The frequency f = 1/10. 

# IKFast
## Handwritten digits

<p align="center">
  <img src="./IKFast/human_generated/numbers/1one/left.png" width="400" title="Show the digit number 1 for tracking.">
  <img src="./IKFast/human_generated/numbers/1one/right.png" width="400" title="Show the digit number 1 for tracking.">
</p>
Elapsed time: ~6.8 seconds
<p align="center">
  <img src="./IKFast/human_generated/numbers/8eight/left.png" width="400" title="Show the digit number 8 for tracking.">
  <img src="./IKFast/human_generated/numbers/8eight/right.png" width="400" title="Show the digit number 8 for tracking.">
</p>
Elapsed time: ~38.5 seconds

## Computer Generated
### Circle
#### T = 20, r = 0.1, publish frequency = 100
<p align="center">
  <img src="./IKFast/computer_generated/circle/tuned_PID/left.png" width="400" title="Small generated circle with period time 20.">
  <img src="./IKFast/computer_generated/circle/tuned_PID/right.png" width="400" title="Small generated circle with period time 20.">
</p>

#### T = 5, r = 0.1, publish frequency = 100
<p align="center">
  <img src="./IKFast/computer_generated/circle/T5r01/left.png" width="400" title="Small generated circle with period time 20.">
  <img src="./IKFast/computer_generated/circle//T5r01/right.png" width="400" title="Small generated circle with period time 20.">
</p>

### Sweep Sine
<p align="center">
  <img src="./GIFS/IKFast/sweepsine.gif" title="Sweeeeeep sine!" width="800">
</p>
<p align="center">
  <img src="./IKFast/computer_generated/sweepsine/left.png" width="800" title="Sweep sine system output left.">
  <img src="./IKFast/computer_generated/sweepsine/right.png" width="800" title="Sweep sine system output right.">
</p>

### Step Wave
<p align="center">
  <img src="./GIFS/IKFast/step.gif" title="Step wave" width="800">
</p>
<p align="center">
  <img src="./IKFast/computer_generated/step/left.png" width="800" title="Step system output left.">
  <img src="./IKFast/computer_generated/step/right.png" width="800" title="Step system output right.">
</p>


# KDL IK Solver and Cartesian Path Planning
## Handwritten digits
### One
<p align="center">
  <img src="./KDL/shapes/numbers/1one/left.png" width="400" title="Show the digit number 1 for tracking.">
  <img src="./KDL/shapes/numbers/1one/right.png" width="400" title="Show the digit number 1 for tracking.">
</p>
Elapsed time: ~9.5 seconds

### Two
<p align="center">
  <img src="./KDL/shapes/numbers/2two/left.png" width="400" title="Show the digit number 2 for tracking.">
  <img src="./KDL/shapes/numbers/2two/right.png" width="400" title="Show the digit number 2 for tracking.">
</p>
Elapsed time: ~16.1 seconds

### Three
<p align="center">
  <img src="./KDL/shapes/numbers/3three/left.png" width="400" title="Show the digit number 3 for tracking.">
  <img src="./KDL/shapes/numbers/3three/right.png" width="400" title="Show the digit number 3 for tracking.">
</p>
Elapsed time: ~20.6 seconds

### Four
<p align="center">
  <img src="./KDL/shapes/numbers/4four/left.png" width="400" title="Show the digit number 4 for tracking.">
  <img src="./KDL/shapes/numbers/4four/right.png" width="400" title="Show the digit number 4 for tracking.">
</p>
Elapsed time: ~16.0 seconds

### Five
<p align="center">
  <img src="./KDL/shapes/numbers/5five/left.png" width="400" title="Show the digit number 5 for tracking.">
  <img src="./KDL/shapes/numbers/5five/right.png" width="400" title="Show the digit number 5 for tracking.">
</p>
Elapsed time: ~15.8 seconds

### Six
<p align="center">
  <img src="./KDL/shapes/numbers/6six/left.png" width="400" title="Show the digit number 6 for tracking.">
  <img src="./KDL/shapes/numbers/6six/right.png" width="400" title="Show the digit number 6 for tracking.">
</p>
Elapsed time: ~30.4 seconds

### Seven
<p align="center">
  <img src="./KDL/shapes/numbers/7seven/left.png" width="400" title="Show the digit number 7 for tracking.">
  <img src="./KDL/shapes/numbers/7seven/right.png" width="400" title="Show the digit number 7 for tracking.">
</p>
Elapsed time: ~10.1 seconds

### Eight
<p align="center">
  <img src="./KDL/shapes/numbers/8eight/left.png" width="400" title="Show the digit number 8 for tracking.">
  <img src="./KDL/shapes/numbers/8eight/right.png" width="400" title="Show the digit number 8 for tracking.">
</p>
Elapsed time: ~29.3 seconds

### Nine
<p align="center">
  <img src="./KDL/shapes/numbers/9nine/left.png" width="400" title="Show the digit number 9 for tracking.">
  <img src="./KDL/shapes/numbers/9nine/right.png" width="400" title="Show the digit number 9 for tracking.">
</p>
Elapsed time: ~18.0 seconds

# Computer Generated
## Circle

### T = 10, r = 0.1, publish frequency = 100
<p align="center">
  <img src="./KDL/computer_generated_paths/circle/10/left_small.png" width="400" title="Small generated circle with period time 10.">
  <img src="./KDL/computer_generated_paths/circle/10/right_small.png" width="400" title="Small generated circle with period time 10.">
</p>

### T = 10, r = 0.2, publish frequency = 100
<p align="center">
  <img src="./KDL/computer_generated_paths/circle/10/left.png" width="400" title="Small generated circle with period time 10.">
  <img src="./KDL/computer_generated_paths/circle/10/right.png" width="400" title="Small generated circle with period time 10.">
</p>

### T = 30, r = 0.2, publish frequency = 100
<p align="center">
  <img src="./KDL/computer_generated_paths/circle/30/left.png" width="400" title="Small generated circle with period time 30.">
  <img src="./KDL/computer_generated_paths/circle/30/right.png" width="400" title="Small generated circle with period time 30.">
</p>

### T = 10, r = 0.2, publish frequency = 2
<p align="center">
  <img src="./KDL/computer_generated_paths/circle/10/pub_freq2/left.png" width="400" title="Small generated circle with period time 10.">
  <img src="./KDL/computer_generated_paths/circle/10/pub_freq2/right.png" width="400" title="Small generated circle with period time 10.">
</p>

### T = 5, r = 0.2, publish frequency = 2
<p align="center">
  <img src="./KDL/computer_generated_paths/circle/5/pub_freq2/left.png" width="400" title="Small generated circle with period time 5.">
  <img src="./KDL/computer_generated_paths/circle/5/pub_freq2/right.png" width="400" title="Small generated circle with period time 5.">
</p>




## Sweep Sine
<p align="center">
  <img src="./KDL/computer_generated_paths/sweepsine/sweep_sine.gif" title="Sweeeeeep sine!" width="800">
</p>
<p align="center">
  <img src="./KDL/computer_generated_paths/sweepsine/left.png" width="800" title="Sweep sine system output left.">
  <img src="./KDL/computer_generated_paths/sweepsine/right.png" width="800" title="Sweep sine system output right.">
</p>


## Step     
<p align="center">
  <img src="./KDL/computer_generated_paths/step/left.png" width="800" title="Step function system output left.">
  <img src="./KDL/computer_generated_paths/step/right.png" width="800" title="Step function system output right.">
</p>



## Transfer Function (Estimate)
Estimating the transfer function one can see that the system only can track low frequencies. That is also possible to see from the sweep sine tests. From which the transfer function is estimated from.
The images was generated with MATLAB. The script is called TFE.m.

<p align="center">
  <img src="./KDL/TFE_valid_region.png" width="400" title="Step function system output left.">
  <img src="./KDL/TFE.png" width="400" title="Step function system output left.">
</p>

Valid region to the right (as sweep sine did not go to 5Hz).
