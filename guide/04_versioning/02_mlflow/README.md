Contents
==
- [Contents](#contents)
- [Experiment tracking](#experiment-tracking)
- [Using MLFLow](#using-mlflow)

<!--intro-start-->
# Experiment tracking
Experiment tracking is important as it enables us to:
- Monitor and track experiments (hyper-parameters and model performance metrics)
- Package artifacts to reproduce an experiment (training data)
- Store and provision models in a central registry (model file)

MLFLow is a popular open-source experiment tracking tool.

Within MLFLow there is the concept of experiments and runs.

An experiment in MLflow is a container of runs/trials for a machine learning project.

A run in MLflow represents a single iteration of model training/evaluation, it contains a collection of trackable produced in the iteration. A run can include as many secondary runs as we want to form nested runs, which is particularly useful for tracking information during tuning.

# Using MLFLow
The notebook in this folder illustrates how to use MLFlow.

Once you have run the noteboook, run the following command to view the results of the experiment in the UI:
`mlflow ui`

<!--intro-end-->
