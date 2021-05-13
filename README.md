# Easy Recipes bot

Just write down your ingredients and this bot instantly finds matching recipes!

This telegram bot recommends easy recipes in Azerbaijani using ingredients you already have in the kitchen.

I have used text similarity method in order to determine how ‘close’ user message and our text. The big idea is that we represent documents as vectors of features, and compare documents by measuring the distance between these features. I have tried a few similarity methods, but after some experiments, I have chosen Cosine similarity method. As a dataset, I have fully scraped __dadli.az__ website (2400 + recip.). You can find whole dataset in data folder.

![Cosine](https://miro.medium.com/max/426/1*5J8YlnfnZlzFobQC9cGk-w.png)


Mathematically speaking, Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. The cosine of 0° is 1, and it is less than 1 for any angle in the interval (0,π] radians. It is thus a judgment of orientation and not magnitude: two vectors with the same orientation have a cosine similarity of 1, two vectors oriented at 90° relative to each other have a similarity of 0, and two vectors diametrically opposed have a similarity of -1, independent of their magnitude.

The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

The dataset's structure is like:

__ad -__ _The name of eating_

__terkibi -__ _Ingredients of eating_

__hazirlanmasi -__ _How to make_

__img_url -__  _The image of eating_

__label -__ _The type of eating_

__yemek_id -__ _unique identifier of each eating_


When user write down ingredients that he/she has, we split it into a list of words by using text to word sequence() function that provided by Keras. By
default, this function automatically does 3 things: 

- [x] Splits words by space.

- [x] Filters out punctuation.

- [x] Converts text to lowercase (lower=True).

You can change any of these defaults by passing arguments to the function.

After splitting user message into a list of words, our similarity function compare it with __terkibi__ feature and determine the most similiar eating. Then our telegram bot sends this eating's name, "how to make", and image to user. The example answer is below:


![](https://github.com/NijatZeynalov/Easy-Recipes-bot/blob/master/example%20answers/example1.jpeg)

.

![](https://github.com/NijatZeynalov/Easy-Recipes-bot/blob/master/example%20answers/example2.jpeg)
