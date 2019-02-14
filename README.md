# CSCI-4448-Homework-2-Problem-6

Hongyi Chen (solo team)

This is written in Python 3.7 (I wrote it in Java last time).

Here's a list of changes I made:
 - Previously, the Point class only had a toString method, and there was no way for other classes to access the coordinates of the point except to parse the string. This time, I added getter functions for the x and y coordinates of the point. Since I intended Point objects to be immutable, I did not make setter functions.
 - I also added a rot90deg(c) method to the Point class, which returns a new point which is rotated 90 degrees counterclockwise about a center point c. This is useful for the Square class, since I needed to rotate a point 3 times to generate all 4 vertices of the square. Previously, I had done all the messy arithmetic for rotations inside the Square initializer. My new code is a bit cleaner because of this.
 - I decided to approach the sort problem differently this time. Previously, I made the Shape class implement the Comparable interface in Java. I do not know of an equivalent for this in Python, so instead of using a compareTo function inside Shape to compare the z-values of shapes, I made a getter for the z-value. Then, to sort the array of shapes, I used Python's Array.sort method with the key being the z-value of each shape. 
