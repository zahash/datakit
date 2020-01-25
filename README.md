# datakit

1. Obtain               --> csv

2. clean                --> dtypes,
                            duplocates,
                            outliers,
                            fillna(mean, median, mode),
                            remove hierarchies

3. Visualize | Analyze  --> corrplot,
                            { for each col:
                                if numeric : density plot
                                if categorical : bar plot},
                            { for each col:
                                if numeric : scatter(col, label)
                                if categorical: bar(col, label)},

4. Feature Engineering  --> use ID for aggregations of sum, mean, std to create new features,
                            feature selection,
                            dummy variables,
                            splitting,
                            scaling,
                            log(x) | x**(1/3) to normalize skewness,

5. Model                --> Best model selection,
                            hyperparameter tuning,
                            Flask deployment
