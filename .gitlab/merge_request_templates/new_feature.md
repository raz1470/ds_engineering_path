# Merge request template - New feature
This merge request template should be used for new features in new or existing projects:

- New script
- New function

**It is the authors responsibility to fill out this merge request template.**
 
## Background

### What are the changes?
*insert-description-here*

### Why are they needed?
*insert-description-here*

### Is there any particular parts which you want reviewing?
*insert-description-here*

### Is there anything you want the reviewer to be aware of?
*insert-description-here*

## Important links
[Link to Jira ticket](insert-link-here)

[Link to documentation](insert-link-here)

## Relevant files to review

- File 1:
  - File name: *insert-filename-here*
  - Description: *insert-description-here*
  - Link: *insert-link-here*
  
- File 2:
  - File name: *insert-filename-here*
  - Description: *insert-description-here*
  - Link: *insert-link-here*

## Author checklist
**In this section we ask the author to confirm that best practices have been followed:**
- Have you created a peer review sub-task in Jira and assigned the reviewer?
  - [ ] Not relevant
  - [ ] Yes
- Does the feature branch follow the [naming convention](https://confluence.corp.entaingroup.com/display/ANA/Git+and+repository+template%2C+cookiecutter)?
  - [ ] Not relevant
  - [ ] Yes
- Has documentation been updated to include new feature?
  - [ ] Not relevant
  - [ ] Yes  
- Have [SQL coding standards](https://confluence.corp.entaingroup.com/display/ANA/SQL+Best+Practices) been followed?
  - [ ] Not relevant
  - [ ] Yes
- Have [Python coding standards](https://confluence.corp.entaingroup.com/display/ANA/Clean+Code+in+Python+and+Code+Standards) been followed?
  - [ ] Not relevant
  - [ ] Yes
- Has the change been tested successfully?
  - [ ] Not relevant
  - [ ] Yes
- Have test results been supplied as part of the MR / Can test results be reproduced by the reviewer?
  - [ ] Not relevant
  - [ ] Yes
- Have pre-commit checks passed locally (refer to [docs](http://marketing-data-science.vie.pages.bwinparty.corp/pngr) for setup)?
  - [ ] Not relevant
  - [ ] Yes
- Have all stages in CI-CD pipeline passed (all green)?
  - [ ] Not relevant
  - [ ] Yes
- Has the MR been tagged with appropriate labels?
  - [ ] Not relevant
  - [ ] Yes
- Have any merge conflicts have been resolved?
  - [ ] Not relevant
  - [ ] Yes
- Is the MR less than 500 lines of code?
  - [ ] Not relevant
  - [ ] Yes
- Is the feature branch being merged into develop rather than main?
  - [ ] Not relevant
  - [ ] Yes

**If the reviewer believes some of the best practices haven't been followed, it is their responsibility to raise this on the MR.**