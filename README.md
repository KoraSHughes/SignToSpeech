# SignToSpeech
CS-UY 4563 Machine Learning - Fall 2022 - Final Project
By Kora S. Hughes

Prompt: ...

Idea: ASL Sign to Speech
With the implementation of [tbd] hand tracking software,
I plan to create a classification algorithm of American Sign Language.
The purpose is to be a sort of google-translate for  


Phase 1) Find a hand tracking software/device that can collect data
            a) ideally should be able to export it to a usable format at the click of a button
Phase 2) Define model and test parameters for current [stage]
Phase 3) Set classification structure to word strings
Phsae 4) Use text-to-speech to say string out loud

Stage 1) Classify static single-hand position from ASL alphabet
Stage 2) Classify static single-hand position from ASL words
Stage 3) 2-hand signs
Stage 4) Dynamic positions
Stage 5) Real-time analysis/classification
Stage 6) Classify sign language
Stage 7) Classify sign dialects
Stage 8) Extrapolate recurring new signs from a conversation and add to database of new terms
Stage 9) Reconstruct single signs from written classification
Stage 10) Reconstruct sentence and conversations from text.
Note: Due to my own time limitations I only intend to get through stages 1 and maybe 2 before my course ends...
      but the purpose of this is to spark future ideas and implementations


Potential Attributes: pos hand_center, pos finger_tips, pos finger-joints, pos wrist
Potential Extrapolation: hand/finger orientation vectors, finger flexion, wrist flextion, hand direction (wrist-relative)


Added Tools:
More Data:
More Training:

Implementations:
Leap Motion Controller: https://www.ultraleap.com/product/leap-motion-controller/
MediaPipe Classification: https://google.github.io/mediapipe/solutions/hands.html
                          https://www.roadtovr.com/google-hand-tracking-mediapipe/
                          https://ai.googleblog.com/2019/08/on-device-real-time-hand-tracking-with.html

Other Examples:
https://github.com/google/shuwa