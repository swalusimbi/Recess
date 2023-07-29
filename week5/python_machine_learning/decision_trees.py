"""
A decision tree is a type of supervised machine learning used to categorize 
or make predictions based on how a previous set of questions were answered.
The model is a form of supervised learning, 
meaning that the model is trained and tested on a set of data that contains the desired categorization. 

The decision tree may not always provide a clear-cut answer or decision. 
Instead, it may present options so the data scientist can make an informed decision on their own.
Decision trees imitate human thinking, so it's generally easy for data scientists to understand and interpret the results.

Key terms of a decision tree.

Root node: The base of the decision tree.
Splitting: The process of dividing a node into multiple sub-nodes.
Decision node: When a sub-node is further split into additional sub-nodes.
Leaf node: When a sub-node does not further split into additional sub-nodes; represents possible outcomes.
Pruning: The process of removing sub-nodes of a decision tree.
Branch: A subsection of the decision tree consisting of multiple nodes.

A decision tree resembles, well, a tree. 
The base of the tree is the root node. From the root node flows a series of decision nodes that depict decisions to be made. 
From the decision nodes are leaf nodes that represent the consequences of those decisions. 
Each decision node represents a question or split point, and the leaf nodes that stem from a decision node represent the possible answers. 
Leaf nodes sprout from decision nodes similar to how a leaf sprouts on a tree branch.
This is why we call each subsection of a decision tree a “branch.”

Types of Decision Trees.

Categorical Variable Decision Tree
    In a categorical variable decision tree, the answer neatly fits into one category or another. 
    Was the coin toss heads or tails? Is the animal a reptile or mammal? In this type of decision tree, 
    data is placed into a single category based on the decisions at the nodes throughout the tree.    

Continuous Variable Decision Tree
    A continuous variable decision tree is one where there is not a simple yes or no answer. 
    It's also known as a regression tree because the decision or outcome variable depends on other decisions farther up the tree 
    or the type of choice involved in the decision. 

The benefit of a continuous variable decision tree is that the outcome can be predicted based on multiple variables 
rather than on a single variable as in a categorical variable decision tree. 

Continuous variable decision trees are used to create predictions. 
The system can be used for both linear and non-linear relationships if the correct algorithm is selected.






Decision Trees (DTs) are a non-parametric supervised learning method used for classification and regression.
The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.

Classification.
DecisionTreeClassifier is a class capable of performing multi-class classification on a dataset.
As with other classifiers, DecisionTreeClassifier takes as input two arrays: 
    an array X, sparse or dense, of shape (n_samples, n_features) holding the training samples, 
    and an array Y of integer values, shape (n_samples,), holding the class labels for the training samples:

    from sklearn import tree
    X = [[0, 0], [1, 1]]
    Y = [0, 1]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)

After being fitted, the model can then be used to predict the class of samples:

    clf.predict([[2., 2.]])
    array([1])

In case that there are multiple classes with the same and highest probability,
the classifier will predict the class with the lowest index amongst those classes.

As an alternative to outputting a specific class, the probability of each class can be predicted,
which is the fraction of training samples of the class in a leaf:

    clf.predict_proba([[2., 2.]])
    array([[0., 1.]])

DecisionTreeClassifier is capable of both binary (where the labels are [-1, 1]) classification and multiclass (where the labels are [0, …, K-1]) classification.





Pros 
- can handle both regression and classification problems
- captures non-linear relationships
- can handle missing values or outliers


Cons 
- prone to overfitting
- sensitivity to small changes
- maynot perform well on noisy data


"""