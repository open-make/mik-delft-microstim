# Notes on documenting the microstimulation setup
This file is intended for documenting the (thought) process involved in developing a documentation for the microstimulation setup used in Doron et al., (2020); with some adaptations for video recordings. 

The goal is to create a step-by-step documentation that provides sufficient information for a non-engineer (neuroscientist) to create, build, implement and do experiments on the setup. 

## Description of the microstimulation setup
The microstimulation setup can be subdivided into three compartments: animal, electrical and behavioural. Together, they allow the research of animal behaviour in response to electrical microstimulation.

* The **animal compartment** consists of the headbar holder, the lick detector, the multitool, the solenoid, the tubing and the water container. Collectively, they allow for the restrainment of the animal and the correctly timed distribution of a water reward.
* The **electrical compartment** is comprised of the stimulus isolator, the electrode, the electrode holder and the micromanipulater. Together, they are used to generate an electrical stimulation that's emitted through the electrode.
* The **behavioural compartment** contains the cameras, the camera holders, the lenses, the infra-red and the UV-light. Collectively they allow for the recording of animal behaviour such as pupil dilation and whisker movement.

All compartments put together create a setup that should roughly look like this. 

![](https://i.imgur.com/2MDle4r.jpg)

## Component description
|Component|Description |
|--------|-------|
|Headbar holder| Head restrainer that will keep the head of the animal fixed during the experiment. A simple thumbscrew allows you to release or secure the headbar. *Optional 3D*|
|Lick-detector| Piezo sensor that converts licking to an electrical signal that is amplified and picked up by the multitool. *IR/Piezo*|
|Multitool| Amplifies and thresholds the signal that is detected by the lick-detector. If the threshold is met a block pulse is send to open the solenoid for a set amount of time.|
|Solenoid| Controls the dispensation of a water reward by un-clamping the tubing.|
|Stimulus isolator with charger| Delivers positive, negative or bipolar currents. Pulse duration is controlled by an externally applied voltage.|
|Electrode| Tungsten electrode with heat-treated tapered tip. This is connected to the stimulus isolater and inserted into the brain to inject a current.|
|Electrode holder| Metal rod with an adjustable clamping mechanism for holding the electrode.|
|Micromanipulator| Device that controls the movement of the electrode. Movement can be made in 3 dimensions (x,y,z) on a control pad and is reduced to micrometers.|
|Grayscale camera| Low-light monochromatic camera used for capturing video footage of the face/pupil.|
|RGB camera| Color camera used for capturing video footage of the UV-painted whiskers.|
|Camera holder| Adaptor that can be screwed into the camera. Allows for positioning of the camera to a rod.|
|IR light| Infrared (780nm) LED.|
|UV light| UV (380nm) LED.|

## Intended value of the project
### Pains
- Replicating an experimental setup is difficult. 
- Design of a setup changes constantly.
### Gains
- Understandable guide for building the setup.
- Database for available addons
- Platform for common problems & ideas.


## Current state of the project
The project is still very much in the research phase. As of 05-10-2022 the research involves developing understanding of OpenHardware through the OpenHardware Academy by TU delft and learning the basics of 3D printing.

The future of the project will depend on this knowledge to improve the design of the setup and design 3D holders.

## Next steps
|Priority| Features/ target specs|
|--------|-------|
|Must have| Document, flexible camera's, BPOD|
|Should have| No-noise lick-detector, 3D-printed assecoires.
|Could have| Implant

### Minimum hardware design documentation:
* Bill Of Material
* Written build instructions
* Images of build instructions
* Instructions to verify correct functionality
* Example uses of the product
* Optional: Video of build instructions.

### Project documentation
* Current state of the project
* Future plan of the project
* How to contribute
* Where to find what or ask for help

From OpenHardware Academy