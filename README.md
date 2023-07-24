# AI_Game_Jam_EXPAND
# Convolutional Neural Network from Scratch

This repository contains the implementation of a Convolutional Neural Network (CNN) from scratch using Python and the `numpy` library. The purpose of this project is to build the basic components of a CNN, including convolutional and pooling operations, and implement forward propagation.

## Table of Contents

1. [Introduction](#introduction)
2. [Course Information](#course-information)
3. [Dependencies](#dependencies)
4. [Padding](#padding)
5. [Convolution Step](#convolution-step)
6. [Forward Propagation](#forward-propagation)
7. [Pooling Layer](#pooling-layer)

## Introduction

In this project, we will build a Convolutional Neural Network (CNN) from scratch. CNNs are a type of deep learning model widely used for image recognition and computer vision tasks. They are designed to automatically and adaptively learn spatial hierarchies of features from input images.

## Course Information

This project was done as an exercise in the Coursera course: [Convolutional Neural Networks](https://www.coursera.org/learn/convolutional-neural-networks).

## Dependencies

To run the code, you will need the following dependencies:

- `numpy`: A fundamental package for scientific computing in Python.
- `h5py`: A common package to interact with a dataset stored on an H5 file.
- `matplotlib`: A plotting library for Python.

Make sure to have these packages installed before running the code.

## Padding

In the first part of the project, we implement a helper function for padding. Padding is the process of adding extra border pixels around the input data before applying convolutional operations. It serves several purposes, including avoiding the shrinking problem, controlling the output size, and retaining information from the input borders.

## Convolution Step

In the second part, we implement a single step of the convolution, where a filter is applied to a specific position to obtain a single real-valued output. Convolution is a fundamental operation in CNNs, allowing the network to learn local patterns and features.

## Forward Propagation

The third part focuses on the implementation of the forward propagation for a convolution function. This function convolves the filter over an input activation to produce an output activation.

## Pooling Layer

In the last part, we implement the forward pass of the pooling layer. The pooling layer reduces the spatial dimensions of the input and helps reduce computation while making the network invariant to the position of features.

To get started, you can run the Jupyter notebook provided in this repository to see the code in action and understand how each component of the CNN is built.

Feel free to explore and modify the code according to your needs. Happy learning!

---

You can access the original Jupyter notebook on Google Colab using the following badge:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mohammed-khair/AI_Game_Jam_EXPAND/blob/master/Convolutional_neural_network_from_scratch.ipynb)
