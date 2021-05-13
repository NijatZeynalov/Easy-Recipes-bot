# Easy Recipes bot
This telegram bot recommends easy recipes in Azerbaijani using ingredients you already have in the kitchen.

I have used text similarity method in order to determine how ‘close’ user message and our text. The big idea is that we represent documents as vectors of features, and compare documents by measuring the distance between these features. I have tried a few similarity methods, but after some experiments, I have chosen Cosine similarity method. As a dataset, I have fully scraped __dadli.az__ website (2400 + recip.). You can find whole dataset in data folder.

![Cosine](https://miro.medium.com/max/426/1*5J8YlnfnZlzFobQC9cGk-w.png)


Mathematically speaking, Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. The cosine of 0° is 1, and it is less than 1 for any angle in the interval (0,π] radians. It is thus a judgment of orientation and not magnitude: two vectors with the same orientation have a cosine similarity of 1, two vectors oriented at 90° relative to each other have a similarity of 0, and two vectors diametrically opposed have a similarity of -1, independent of their magnitude.

The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity
