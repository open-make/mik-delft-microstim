# Microstimulation Setup
This file is intended for documenting the process involved in developing the microstimulation setup used in Doron et al., (2020); with some adaptations for video recordings.The goal is to create a step-by-step documentation that provides sufficient information for a non-engineer (neuroscientist) to create, build, implement and do experiments on the setup. 

The current implementation utilizes the intelligent laboratory interface from [Cambridge Electronic Design (CED)](https://ced.co.uk/products/spkovin) paired with their analyzing software SPIKE2. For running experiments.

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

## Current state of the project
The project is in the development/research phase. Nevertheless, the current version should be applicable for building and running the experiment with CED 1401 and SPIKE2. Note that things like the camera holder, rod-connector or headbar holder can be found as 3D printable files from the [SimpleScienceSetup](https://github.com/mik-schutte/SimpleScienceSetup).

The future of the project holds implementations for probe recordings, 2P-imaging and widefield imaging.

## How to contribute 
We are always looking for insightful people that want to help out making the microstimulation setup as efficient and animal-friendly as possible. Especially, implementations for different experiments are welcome. If you want to chip in with your skills send me an email with the things you want to work on together with some details about yourself.

## Acknowledgements
The core team members are Mik Schutte (myself) and Jelte de Vries. Both of us are employed by the Humboldt University and PhD-students in the Larkum lab and are being supervised by Dr. Robert Sachdev. Primary development was performed by Dr. Guy Doron and transferred by Moritz Druke. Data-management and the supervision concerning open source is done by Dr. Julien Colomb. Lastly, we thank the Delft Open Hardware Academy for its many valuable lessons in designing, project management and hardware documentation.
