# Building the Microstimulation Setup

## Preliminary Notes
Please take into account the current status of the project. We're actively working on advancements for the microstimulation setup, which may affect the documentation's completeness. The change from version0 to version1 has transfered the laboratory interface from CED to BPOD. However, the instructions provided below are compatible with both versions. You can find the specific components in the [bill_of_materials](base_setup/base_BoM.csv) 


## Purpose
The base setup serves as the foundation for the entire microstimulation experiment. Its primary functions include: minimize vibrations, ensuring a stable platform for the experiment. This stability is crucial for accurate data collection and the functionality of delicate equipment.

For stability, we employ a vibration table (XXX) with an accompanying xxx plate. Alternatively, tools from the [SimpleScienceSetup](https://github.com/mik-schutte/SimpleScienceSetup) can be utilized. Grounding is achieved by [describe grounding method].


The base setup acts as a platform for integrating and arranging the various compartments necessary for the experiment:

1. **Animal Restraints:** This section includes components for head fixation and animal restraint to facilitate electrode insertion while minimizing discomfort for the subject.

2. **Water Reward System:** Components such as the lick detector, multitool, solenoid, tubing, and water container are situated within this section to ensure precise and reliable delivery of the water reward.

3. **Electrical Compartment:** Components like the arduino pulse configurator, stimulus isolator, electrode, and electrode holder are placed here to generate and emit electrical stimulation through the electrode.

4. **Camera Compartment:** This section houses cameras, camera holders, lenses, infra-red, and UV-light setups, enabling the recording of various behavioral aspects such as pupil dilation and whisker movement.

The base setup's strategic design and placement of these compartments ensure a cohesive and functional microstimulation setup.

## Necessary Tools

To replicate the microstimulation setup, gather the following tools:

- Airtable
- Optical breadboard (6mm)
- Grounding box
- Surgical microscope
- Flat head screwdriver
- 6mm hex screw (x2)
- [Additional tool needed]


## Build instructions
![Animal Restraint Build](pictures/build_animalrestraint.png)