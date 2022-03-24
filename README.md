# Generating Music from Brainwaves using BCIs
***Feel free to check out [this article](https://bagavanmm.medium.com/generating-music-with-my-brain-829d1c168ef8), which goes more in-depth into how the code for this project works!***

![BrainMusic](https://github.com/BagavanMM/BrainwaveMusic-OpenBCI/blob/main/logo.png)
<!-- ABOUT THE PROJECT -->
## About The Project
In this project, I created a program that allows me to convert my brainwaves into music. **In order to capture these brain signals, we use something known as a brain-computer interface.** 
Whenever you’re doing anything, from talking, playing video games, to even reading this article, billions of neurons in our brain are constantly firing. **A brain-computer interface is that’s used to capture these brain signals, analyze them and translate them into a specific output or command** (in our case, it’s music). Now, a lot of methods used for capturing our brain signals using BCIs are generally invasive/semi-invasive, meaning you’d have to undergo some kind of surgery to implant electrodes into your brain. However, that isn’t going to be practical for this project, and scaling any project/product. That’s why one of the most common ways of collecting this data is through a **non-invasive method known as electroencephalography (EEG).**

**Electroencephalography (or EEG for short)** is what’s used to collect electrical activity from the brain, by placing electrodes (small metal discs with thin wires) onto the scalp/surface of your head. These electrodes are what are used to detect different changes in electrical charge due to activity from your brain waves.



### What I Used to Build This Project
**Hardware:**
The BCI that I used was OpenBCI’s Ganglion Board. This is a biosensing device that’s mainly used for collecting different types of electrical signals from not only the brain but anywhere (which can come in handy for other projects). As for the electrodes, I also used OpenBCI’s headband kit. OpenBCI has great documentation for how to set up this kit, so I would recommend checking that out [here](https://docs.openbci.com/AddOns/Headwear/HeadBand/)

**Software:**
This project was built in python and the main libraries I used are the following:
* [Brainflow](https://brainflow.readthedocs.io/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Midiutil](https://midiutil.readthedocs.io/en/1.2.1/)



<!-- GETTING STARTED -->
## Getting Started

If you want to test this project out for yourself, make sure you first install the necessary libraries to run the code (which was mentioned previously).
After that, all you have to do is cloe the repo!
   ```sh
   git clone https://github.com/BagavanMM/BrainwaveMusic-OpenBCI.git
   ```


<!-- USAGE EXAMPLES -->
## Usage
### Running `EEGMusic-Ganglion.py`
**In order to run this code, you would need to have access to an OpenBCI Ganlgion Board as well as EEG electrodes/thier headband kit**

In line 17, make sure that ```params.serial_port``` is changed to the right serial port address (Currently it's "COM5" however this may be different depending on where you are running this code on).

> If you don't have access to an OpenBCI ganglion board, you can also test out this project by running [`EEGMusic-SyntheticBoard.py`](https://github.com/BagavanMM/BrainwaveMusic-OpenBCI/blob/main/EEGMusic-SyntheticBoard.py). 


The music that is outputted will be stored in a MIDI file called `le-music.mid` - located in the same place as where the script is. 


## Contact

Bagavan Marakathalingasivam - [@BagavanMM](https://twitter.com/BagavanMM) - bagavan.sivam@gmail.com

Project Link: [https://github.com/BagavanMM/BrainwaveMusic-OpenBCI](https://github.com/BagavanMM/BrainwaveMusic-OpenBCI)
