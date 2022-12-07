# SignToSpeech - Leap Motion Branch
CS-UY 4563 Machine Learning - Fall 2022 - Final Project<br>
By Kora S. Hughes

<br>AUTHOR'S NOTE: since my current operating system isnt compatible with leap motion I wont be able to develop this at the moment however I intend to build upon this in the future... <br>

## Abstract:
SignToSpeech builds on Google's MediaPipe hand tracking software and delivers a machine learning based translation software for American Sign Language (ASL) users.
The purpose is to reduce the need for human sign-langauge interpretors and overall increase the accessibility of communication for the deaf/hard-of-hearing community: a google-translate for sign language.<br>
The purpose of this algorithm is to build on existing sign language processing (SLP) techniques by testing the feasibility of single-hand-centered classification and evaulating which algorithms work the best.

## Methods:
### Data Collection:<ol>
<li>signs collected with 2 different people of different hand shapes, posing with just their hands on a blank background</li>
<li>testers were given an image of the intended sign prior to collection and were told to rotate their sign and relax it over the course of the video </li>
<li>each video was around 10 seconds and 3 snap shots of said video were taken every elapsed second via the data_gatherer file</li>
<li>key landmarks of hand positions were taken from each image as part of preprocessing</li>
</ol>

### Packages: <ol>
<li>MediaPipe Classification: [https://google.github.io/mediapipe/solutions/hands.html, https://www.roadtovr.com/google-hand-tracking-mediapipe/https://ai.googleblog.com/2019/08/on-device-real-time-hand-tracking-with.html ]</li>
</ol>


## Testing:<ol>
<li>Overall Framework: one-hot encoded classification</li>
<li>Started with a logistic binary classification algorithm. Once that worked I used one vs. all multiclassification </li>
<li>The multiclassifier was trained using logistic regression on validation set starting at [A vs. B], then a new sign was added after each successful implementation until the final set was [A vs. B vs. H vs. K vs. W vs. Y] </li>
<li>Once the algorithm prooved it could classify all 6 signs, different strategies and algorithms were tested on the training set (ex: support vector machines, ridge regression, neural network implementaiton)</li>
</ol>


### Phases:<ol>
<li>Find a hand tracking software/device that can collect data (ideally should be able to export it to a usable format at the click of a button)</li>
<li>Define model and test parameters for current [stage]</li>
<li>Set classification structure to word strings</li>
<li>Use text-to-speech to say string out loud</li>
</ol>

### Stages:<ol>
<li>Classify static single-hand position from ASL alphabet</li>
<li>Classify static single-hand position from ASL words</li>
<li>2-hand signs</li>
<li>Dynamic positions</li>
<li>Real-time analysis/classification</li>
<li>Classify sign language</li>
<li>Classify sign dialects</li>
<li>Extrapolate recurring new signs from a conversation and add to database of new terms</li>
<li>Reconstruct single signs from written classification</li>
<li>Reconstruct sentence and conversations from text.</li>
</ol>

>  Note: Due to my own time limitations I only intend to get through stages 1 and maybe 2 before my course ends...
      but the purpose of this is to spark future ideas and implementations



## Results:
### Logistic Regression based Classification:<ol>
<li>[tbd]</li>
</ol>

#### Adding Support Vector Machines:<ol>
<li>[tbd]</li>
</ol>

#### Adding ridge regression:<ol>
<li>[tbd]</li>
</ol>


### Neural Network:<ol>
<li>[tbd]</li>
</ol>

#### changing number of update iterations:<ol>
<li>[tbd]</li>
</ol>

#### changing network structure: initial=[]<ol>
<li>added layers: [tbd]</li>
<li>added neurons: [tbd]</li>
</ol>

#### changing activation functions:<ol>
<li>sigmoid: [tbd]</li>
<li>ReLU: [tbd]</li>
<li>TanH: [tbd]</li>
</ol>

#### Adding ridge regression:<ol>
<li>[tbd]</li>
</ol>
                          
## Future Research:
### Implementations:<ol>
<li>Leap Motion Controller: https://www.ultraleap.com/product/leap-motion-controller/</li>
<li>Haptic Feedback Devices for sign language learning</li>
</ol>

### Additional Attributes:<ol>
<li>pos hand_center, pos finger_tips, pos finger-joints, pos wrist </li>
<li>hand/finger orientation vectors, finger flexion, wrist flextion, hand direction (wrist-relative), max vert/horiz dist between landmarks </li> </ol>

### Strategies to Implement: <ol>
<li> unsuperivsed analysis </li>
<li> landmark distance normalization: relative to wrist </li>
<li> one vs. rest and one vs. all classifcation </li>
<li> larger data set </li>
<li> more, diverse hands, and hand signs </li>
<li> hand signs from regular users ** </li>
<li> more diverse backgrounds </li>
<li> added convolutionary layers based on edge detection and invariant features like medial axis and euler number. </li>
<li> weighted finger values (ex: more significant fingers like pointer, thumb, and ring-finger) </li>
</ol>

### Potential Tools:<ol>
<li>Facial Landmarks</li>
<li>Tone recognition using sign velocity and jitter</li>
<li>Tone recognition using facial sentiment analysis techniques</li>
</ol>

## Inspiration:<ol>
<li>https://iopscience.iop.org/article/10.1088/1741-2552/aba6da/meta</li>
<li>https://github.com/sign-language-processing/sign-language-processing.github.io</li>
<li>https://github.com/google/shuwa</li>
</ol>
