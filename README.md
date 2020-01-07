# NLP-Disaster-Tweets
Predict which Tweets are about real disasters and which ones are not

## Machine Learning on Text

Essential preperatory step is to transform our documents into numeric features, a process called vectorization.
Instances are vector (numeric) representations of distinguishable entities. In text analysis, instances are entire
documents, in this case tweets.

### Features
Each property of the vector representation is called a feature, therefore the representation of instances describes a multidimensional
feature space where predictions can be made. Features represent some real world attribute of the instance, a mapping or function applied to a combination of properties.

### Bag of Words

A bag-of-words is a representation of text that describes the occurrence of words within a document.
If we decide to Vectorize a tweet using this method you can imagine we would have a vector full of 0.
You can imagine if we try using this on a book the 

### Feature Extraction Phase
The process of encoding documents in a numeric feature space is called feature
extraction or more simply, vectorization and is an essential first step towards language aware analysis.
In the feature extraction phase, the goal is to analyze, extract, and select a sufficiently
hearty set of features with which to model the data.

### Model Selection
In the second phase, a set of algorithms are selected from a model family, which can then be used, evaluated, and compared
in parallel.

### Model Tuning

Finally, we conduct tuning by adjusting the model hyperparameters
to identify the combination that result in the most predictive fitted model.

## Term Frequency-Inverse Document Frequency

The Goald is to consider the relative frequency or rareness of tokens in
the document against their frequency in other documents