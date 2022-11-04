# SignToSpeech
CS-UY 4563 Machine Learning - Fall 2022 - Final Project<br>
By Kora S. Hughes

## Prompt: ...

## Idea: ASL Sign to Speech
With the implementation of [tbd] hand tracking software, I plan to create a classification algorithm of American Sign Language.
The purpose is to be a sort of google-translate for various sign languages.

### Phases:<ol>
<li>Find a hand tracking software/device that can collect data
            a) ideally should be able to export it to a usable format at the click of a button</li>
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

## Implementations:
Leap Motion Controller: https://www.ultraleap.com/product/leap-motion-controller/
MediaPipe Classification: https://google.github.io/mediapipe/solutions/hands.html
                          https://www.roadtovr.com/google-hand-tracking-mediapipe/
                          https://ai.googleblog.com/2019/08/on-device-real-time-hand-tracking-with.html
### Potential Attributes:
pos hand_center, pos finger_tips, pos finger-joints, pos wrist
### Potential Extrapolation:
hand/finger orientation vectors, finger flexion, wrist flextion, hand direction (wrist-relative)

### Strategies to Implement:
#### Added Tools: ...
#### More Data: ...
#### More Training: ...

## Other Examples:
https://github.com/google/shuwa
