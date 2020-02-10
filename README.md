# This repository is Archived

### This repository is archived because I want to make another repository containing only the files in the 'core' folder and publish it in the form of a python package.

### The reason for this is that once I discovered openrefine by google, this repository lost its purpose. So, I'm removing the GUI and only keeping the 'core' part as a separate repository

# datakit

1. Obtain --> csv

2. clean --> dtypes,
   duplocates,
   outliers,
   fillna(mean, median, mode),
   remove hierarchies

3. Visualize | Analyze --> corrplot,
   { for each col:
   if numeric : density plot
   if categorical : bar plot},
   { for each col:
   if numeric : scatter(col, label)
   if categorical: bar(col, label)},

4. Feature Engineering --> use ID for aggregations of sum, mean, std to create new features,
   feature selection,
   dummy variables,
   splitting,
   scaling,
   log(x) | x\*\*(1/3) to normalize skewness,
