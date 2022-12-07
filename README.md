# SignToSpeech
CS-UY 4563 Machine Learning - Fall 2022 - Final Project<br>
By Kora S. Hughes

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
<li>baseline logistic regression did extremely well, achieving perfect accuracy for most trials with a learning rate of around 0.25</li>
<li>any added ridge regression term made it a decent amount worse so those were avoided</li>
</ol>

#### Adding Support Vector Machines:<ol>
<li>[tbd]</li>
</ol>

#### Adding ridge regression:<ol>
<li>[tbd]</li>
</ol>


### Neural Network:<ol>
<li>Neural Network trained classification tended to bottom out at around 2k-5k iterations</li>
<li>Generally it favored a lower learning rate of around 0.14</li>
</ol>

#### changing network structure: initial=[]<ol>
<li>added layers: added layers did slightly poorly at face value but did a decent amount better with a higher learning rate of around 0.4 and a lower number of neurons per hidden layer resulting in approximately 45% accuracy </li>
<li>added neurons: relative to the 18 neuron hidden layer baseline I set, more neurons (about 25) did much better and less neurons did substantially worse</li>
</ol>

#### changing activation functions:<ol>
<li>sigmoid: did decently well but only after around 3k training examples</li>
<li>ReLU: did as well as sigmoid but with a fewer number of training examples (around 2k)</li>
<li>TanH: took much longer than the other two to train and did worse</li>
</ol>

#### Adding ridge regression:<ol>
<li>Did surprisingly well, even with higher lambda values around 0.01</li>
<li>Combined with a higher learning rate of 0.3, the algorithm achieved a cost of around 0.48 and accuracy of 74%</li>
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
