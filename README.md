# VR Tracking Data
Two Franka Emika Panda robots which are following different trajectories. Either human made or computer generated. The human generated trajectories are made using HTC-Vive VR controllers.

## Handwritten digits
Trying to get the results as close to real performance I decided to only do the digits one time. The digits are generated with the two arms at the same time. And the digits are hand written (obviously).

### One
<p align="center">
  <img src="./tracking/shapes/numbers/1one/left.png" width="400" title="Show the digit number 1 for tracking.">
  <img src="./tracking/shapes/numbers/1one/right.png" width="400" title="Show the digit number 1 for tracking.">
</p>
Elapsed time: ~9.5 seconds

### Two
<p align="center">
  <img src="./tracking/shapes/numbers/2two/left.png" width="400" title="Show the digit number 2 for tracking.">
  <img src="./tracking/shapes/numbers/2two/right.png" width="400" title="Show the digit number 2 for tracking.">
</p>
Elapsed time: ~16.1 seconds

### Three
<p align="center">
  <img src="./tracking/shapes/numbers/3three/left.png" width="400" title="Show the digit number 3 for tracking.">
  <img src="./tracking/shapes/numbers/3three/right.png" width="400" title="Show the digit number 3 for tracking.">
</p>
Elapsed time: ~20.6 seconds

### Four
<p align="center">
  <img src="./tracking/shapes/numbers/4four/left.png" width="400" title="Show the digit number 4 for tracking.">
  <img src="./tracking/shapes/numbers/4four/right.png" width="400" title="Show the digit number 4 for tracking.">
</p>
Elapsed time: ~16.0 seconds

### Five
<p align="center">
  <img src="./tracking/shapes/numbers/5five/left.png" width="400" title="Show the digit number 5 for tracking.">
  <img src="./tracking/shapes/numbers/5five/right.png" width="400" title="Show the digit number 5 for tracking.">
</p>
Elapsed time: ~15.8 seconds

### Six
<p align="center">
  <img src="./tracking/shapes/numbers/6six/left.png" width="400" title="Show the digit number 6 for tracking.">
  <img src="./tracking/shapes/numbers/6six/right.png" width="400" title="Show the digit number 6 for tracking.">
</p>
Elapsed time: ~30.4 seconds

### Seven
<p align="center">
  <img src="./tracking/shapes/numbers/7seven/left.png" width="400" title="Show the digit number 7 for tracking.">
  <img src="./tracking/shapes/numbers/7seven/right.png" width="400" title="Show the digit number 7 for tracking.">
</p>
Elapsed time: ~10.1 seconds

### Eight
<p align="center">
  <img src="./tracking/shapes/numbers/8eight/left.png" width="400" title="Show the digit number 8 for tracking.">
  <img src="./tracking/shapes/numbers/8eight/right.png" width="400" title="Show the digit number 8 for tracking.">
</p>
Elapsed time: ~29.3 seconds

### Nine
<p align="center">
  <img src="./tracking/shapes/numbers/9nine/left.png" width="400" title="Show the digit number 9 for tracking.">
  <img src="./tracking/shapes/numbers/9nine/right.png" width="400" title="Show the digit number 9 for tracking.">
</p>
Elapsed time: ~18.0 seconds

## Sweep Sine
A computer generated sweep sine wave for controller pose. The sweep sine is following the following function:  
<!-- f(t) = sin(2\pi t \frac{f_1-f_0}{2T} \cdot t^2) -->
<p align="center">
  <img src="./tracking/computer_generated_paths/sweepsine/sweep_function.png" width="200" title="Sweep sine function.">
</p>

The output is:  
<p align="center">
  <img src="./tracking/computer_generated_paths/sweepsine/left.png" width="800" title="Sweep sine system output left.">
  <img src="./tracking/computer_generated_paths/sweepsine/right.png" width="800" title="Sweep sine system output right.">
</p>