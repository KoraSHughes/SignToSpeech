# SignToSpeech
> a personal project combining skills from CS-UY 4563 Machine Learning, CS-UY 3943 Mining Massive Datasets, CS-GY 6313 Information Visualization, and CS-UY 3943 Machine Learning Visualization
By Kora S. Hughes

Paper: https://drive.google.com/file/d/1nJ3Z_PBy9S_16MsACai9DAsWS7SY6e9d/view?usp=sharing <br>
SLAP (Sign Language Abstraction Picture) Visualizations: https://observablehq.com/d/790228ffa9ae0f19 <br>
More Info: https://www.linkedin.com/posts/korashughes_algorithmic-classification-models-for-sign-activity-7007154391946305536-T1fT?utm_source=share&utm_medium=member_desktop <br>

## Abstract:
SignToSpeech builds on Google's MediaPipe hand tracking software and delivers a machine learning based translation software for American Sign Language (ASL) users.
The purpose is to reduce the need for human sign-langauge interpretors and overall increase the accessibility of communication for the deaf/hard-of-hearing community: a google-translate for sign language.<br>
The purpose of this algorithm is to build on existing sign language processing (SLP) techniques by testing the feasibility of single-hand-centered classification and evaulating which algorithms work the best.

## Data Usage:
- Homebrew Data: https://drive.google.com/drive/u/3/folders/10QZHo7gI2Y2C0V5OqWY9i8yvhxj5gkwz
- Kaggle Training Set: https://www.kaggle.com/datasets/ardamavi/27-class-sign-language-dataset

## Results Overview:
- Logistic Regresion: 68.74%
- Support Vector Machines: 82.04%
- Neural Networks: 84.80%


## Project Overview:
- data_gatherer.ipynb converts videos to images for homebrew training/testing data ('testing/images' && 'training/images')
- SignToSpeech.ipynb processes the images into landmarks and applies algorithms to them, outputting various results into '/results/'
  - best_hands contains the images and data of hands that the best algorithm chosen by SignToSpeech.ipynb is most confident in
  - processed_train_data files contain landmark data for training data
  - predicted_matrix contains the results of the algorithms tried with overview files for hyperparameters chosen
  - hand_metadata contains frequency dictionaries of what signs exist in the training/testing data for both the kaggle and homebrew sets
  - homebrew-test/train contains old data and tests run as a proof of concept before I decided to fully pursue this project 
- hand_landmarker.ipynb takes the most confident sign images in ('results/best_hands') and overlays landmarks on top of them ('results/best_hands/with-landmarks')
