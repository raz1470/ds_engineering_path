# Merge request template - New model
This merge request template should be used for new models.

**It is the authors responsibility to fill out this merge request template.**
 
## Background

### What is the aim of the solution?
*insert-description-here*

**Please note the background is going to be brief as the documentation should be used my the reviewer to understand the solution.**

## Important links
[Link to Jira ticket](insert-link-here)

[Link to confluence documentation](insert-link-here)

[Link to additional documentation 1 (e.g. EDA)](insert-link-here)

[Link to additional documentation 1 (e.g Experimentation)](insert-link-here)

## Checklist
**In this section we ask the author to confirm that best practices have been followed:**

- [ ] Have you created a peer review sub-task in Jira and assigned the reviewer?
- [ ] Has the confluence documentation be completed using the template? (see pngr21 [example](https://confluence.corp.entaingroup.com/display/ANA/pNGR21d))
- [ ] Has a link to the documentation been added to this merge request?

### EDA
- What of the following was covered in the EDA:
  - [ ] Target flag design:
    - [ ] Comparison of potential target flag metrics
    - [ ] Comparison of potential target flag outcome window
    - [ ] Longitundinal analysis
  - [ ] [Univariate analysis](https://docs.datarobot.com/en/docs/data/analyze-data/analyze-histogram.html)
  - [ ] [Bivariate analysis](https://docs.datarobot.com/en/docs/data/analyze-data/feature-assoc.html)


- Have the EDA been summarised (authors choice where the summary best fits):
  - [ ] In the confluence documention
  - [ ] In a markdown file in the git repo
  - [ ] In a powerpoint presentation
  - [ ] In a Jupyter notebook

### Model experimentation
- What type of experiments have been run:
  - [ ] It was agreed not to experiment
  - [ ] Hyper-parameter tuning
  - [ ] Using different ML techniques
  - [ ] Different model segmentations (e.g. split models by brand)
  - [ ] Different target flag definitions
  - [ ] Different sampling methods/sizes
  - [ ] Different feature sets

- Have the experiments been tracked using MLFLow following the [best practices](https://vie.git.bwinparty.com/marketing-data-science/mlflow-guide-demo):
  - [ ] Yes
  - [ ] It was agreed not to experiment

- Have the experiments been summarised (authors choice where the summary best fits):
  - [ ] In the confluence documention
  - [ ] In a markdown file in the git repo
  - [ ] In a powerpoint presentation
  - [ ] In a Jupyter notebook

### Model training & evaluation
- [ ] Has the model training & evaluation been summarised in the confluence documentation?

- Where was the model trained?
  - [ ] Local machine
  - [ ] Cloud
  - [ ] Data Robot

- Where was following aspects of the model evaluated?
  - [ ] [Lift chart (for classification and regression)](https://docs.datarobot.com/en/docs/modeling/analyze-models/evaluate/lift-chart.html)
  - [ ] [Residuals (for regression)](https://docs.datarobot.com/en/docs/modeling/analyze-models/evaluate/residuals.html)
  - [ ] [Feature importance](https://docs.datarobot.com/en/docs/modeling/analyze-models/understand/feature-impact.html)
  - [ ] [Feature effects](https://docs.datarobot.com/en/docs/modeling/analyze-models/understand/feature-effects.html#:~:text=feature%20impact%20score.-,Feature%20Effects%20explained,features%20sorted%20by%20Feature%20Impact.)

- [ ] Have the experiments been tracked using MLFLow following the [best practices](https://vie.git.bwinparty.com/marketing-data-science/mlflow-guide-demo):

- Is (semi) auto-retraining setup for:
  - [ ] The data preparation 
  - [ ] The data preparation and model training
  - [ ] It was agreed not to setup auto-retraining

### Model reproducibility
- Is there a training DAG pipeline containing the following:
  - [ ] Markdown file with instructions of how to run the training DAG
  - [ ] Requirements file
  - [ ] Data preparation (SQL)
  - [ ] Model experimentation (Python)
  - [ ] Model training & evaluation (Python)
