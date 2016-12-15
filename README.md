# Cognitive Services Apps
Congitive Services App in Python that integrates with Microsoft Cognitive Services API. 

This is a web application that is built using [Flask](http://flask.pocoo.org/) framework to build web apps in Python. 
The web application uses Ninja2 for rendering templates and binding elements in python code.

The Computer Vision API provides state-of-the-art algorithms to process images and return information. 
For example, it can be used to determine if an image contains mature content, or it can be used to find all the faces in an image. 

It also has other features like estimating dominant and accent colors, categorizing the content of images, and describing an image with complete English sentences. 

Additionally, it can also intelligently generate images thumbnails for displaying large images effectively.


## Application Input

1. Image Url: you can pass the image url while the app is running or in the application settings as an argument.

2. Computer Vision API Key: you need to set the subscription key in the app.config file.


![Application Output](/Output.PNG)


## Application Output

1. Image Tags: Capture tags associated with the provided image. This provides an analysis to what type of image has been given to the application.

2. Image Captions: Capture closest captions with confidence ratio to the given image.



References:
+ Read more about Cognitive Services [here](https://www.microsoft.com/cognitive-services/)

+ Read more about Computer Vision API [here](https://www.microsoft.com/cognitive-services/en-us/computer-vision-api)

+ This Application uses Describe Image API [here](https://www.microsoft.com/cognitive-services/en-us/Computer-Vision-API/documentation/DescribingImages)
