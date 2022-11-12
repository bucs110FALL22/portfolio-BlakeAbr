# Final Project Milestone #3

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

Complete this document in **your** portfolio (CH 9). 

You should now begin to code your models. 

Define your models in the `FinalProject/src/` folder in your portfolio.

Although you will probably need to alter them further, you should try to write as much of the models as you can. You can always change things later.

## Models Design

You need to make sure you have the following for each Model:

1. for classes that should be sprites:
    * inherit sprite functionality
    * have instance variables image and rect
2. Models should not have any event logic
    * In other words, you should not be inspecting or responding to events in your models
    * Although some is required, such as the Sprite class, try to minimize how much of the pygame library you use in your models

Remember, this is to get you thinking and help me guide you. Nothing is set in stone.

***

Using the example below, list each model class and its interface

1. < Class Name > 
    * __init__
        * < description >
    * < additional methods >

## Class Interface 1
class fish
  __init__ (self, image, move, stop)
  self.image = image
  self.move = move
  self.stop = stop
  
 

## Class Interface 2
class Player
  __init__ (self, image,throwHook, retrieveHook, hookMove, playerMove)
  self.image = image
  self.throwHook = throwHook
  self.retrieve = retrieveHook
  self.hookMove = hookMove
  self.playerMove = playerMove
  
  

## Class Interface 3
class Background
  __init__ (self, image, changeLocation, goToMenu)
  self.image = image
  self.changeLocation = Location
  self.goToMenu = goToMenu
 
  
  
  