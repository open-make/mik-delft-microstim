# Hardware setup for the "Microstimulation" experiment 

This repository provides information to set up the "Microstimulation" experiment used in Matthew Larkum's lab, including both *a documentation package of the hardware, the experimental protocol, and the software used for data acquisition* 
We will present here the most recent version which was reworked to use BPOD (Schutte et al. in preparation), we will also refer to the original setup described in (Doron et al., 2020).

In the microstimulation experiment, a *rodent* (usually a mouse) is head fixed. It receives *Intracranial Direct Current stimulation (IDCS or microstimulation)* in the primary somatosensory barrel cortex (S1-BF). The goal of the task is to teach the animal to report the stimulus by licking a water spout during the response window. The animal usually learns to associate the stimulation with a sugar water (4% sucrose) reward and will lick the water tube upon stimulation. Different versions of the setup and the protocol exist. 


## Current state of the project

The hardware can be defined as a prototype, as most self-assembled setups in neurobiology labs. Most components are not open source, and expensive. Note that things like the camera holder, rod-connector or head-bar holder can be found as 3D printable files from the [SimpleScienceSetup](https://github.com/mik-schutte/SimpleScienceSetup) project.

The current version uses [BPOD](https://sanworks.io/shop/products.php?productFamily=bpod) technology and [MATLAB](mathworks.com/campaigns/products/trials.html?gclid=CjwKCAiAmsurBhBvEiwA6e-WPC8ymdKjoKsw-h0QvnPUYUxUiHMEaFBh7Eg0xaEl5rYMuemgdsWKdBoC2_kQAvD_BwE&ef_id=CjwKCAiAmsurBhBvEiwA6e-WPC8ymdKjoKsw-h0QvnPUYUxUiHMEaFBh7Eg0xaEl5rYMuemgdsWKdBoC2_kQAvD_BwE:G:s&s_kwcid=AL!8664!3!462958882966!e!!g!!matlab%20download&s_eid=ppc_10961695282&q=matlab+download&gad_source=1)  scripts, while the original setup used CED 1401 and SPIKE2. 

The goal of this repository is to provide a step-by-step guide for a non-engineer (neuroscientist) to create, build, implement and do experiments on the setup.  The **future** of the project holds implementations for probe recordings, 2P-imaging and widefield imaging..


## Overview of the microstimulation setup

The microstimulation setup can be subdivided into several compartments:

* The [base setup](10_basesetup/base_readme.md) base setup: The components needs to be brought together, everything needs to be grounded and vibration resistant,. The elements should be hooked to the computer with possibly a good time synchronisation.

* The [animal restrains](11_animalrestrains/AR_readme.md): animal restraining and head fixation system.

* The [water reward system](12_water-reward/WR_readme.md): the lick detector, the multitool, the solenoid, the tubing and the water container.
* The [electrical compartment for stimulation and eventually recording](13_stimulation-recoding/stim_rec_readme.md): is comprised of the stimulus isolator, the electrode, the electrode holder and the micromanipulator. Together, they are used to generate an electrical stimulation that's emitted through the electrode.
* The [camera compartment](14_videorecording/vid_r_readme.md) contains the cameras, the camera holders, the lenses, the infra-red and the UV-light. Collectively they allow for the recording of animal behaviour such as pupil dilation and whisker movement.



All compartments put together create a setup that should roughly look like this. 

![Overview of the setup from the side and from above](pictures/microstim-overview.jpg)

*Overview of the setup from the side and from above*

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



## How to contribute 

If you have been reading until here, you can probably help us make this documentation better. Please contact us per email or via an issue in this repository, especially is you are using this documentation, if you have some comments or ideas for improvement, if you want to reuse this hardware for similar or dissimilar experiments or if you just want to say hello. 


## Acknowledgements
The core team members are Mik Schutte and Jelte de Vries. Both of us are employed by the Humboldt University and PhD-students in the Larkum lab and are being supervised by Dr. Robert Sachdev. Primary development was performed by Dr. Guy Doron and transferred by Moritz Druke. Data-management and the supervision concerning open source is done by Dr. Julien Colomb. Lastly, we thank the Delft Open Hardware Academy for its many valuable lessons in designing, project management and hardware documentation.



