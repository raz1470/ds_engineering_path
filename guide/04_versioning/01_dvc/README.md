Contents
==
- [Contents](#contents)
- [Data versioning](#data-versioning)
- [Using DVC](#using-dvc)
- [Testing DVC locally](#testing-dvc-locally)

<!--intro-start-->
# Data versioning
Data versioning is important as it enables:
- Collaboration
- Reproduceability
- Traceability

**DVC allows you to have large file associated to your git repository, but not physical stored on 
on remote repository.**

# Using DVC
1)  **Initialization**: A git cloned project should contain .dvc folder. From the project root folder execute the below command to create a .dvc folder:

    `dvc init`

2) **Setting up a repository to store files**: This could be a remote location that multiple people can access

    `dvc remote add -d myremote {location}`

3) **Adding files**:

    `dvc add {folder_name}/{file_name}`

    `git add {folder_name}/{file_name}.dvc {folder_name}\.gitignore`

    `git commit -m "pushing dvc files"`

    `git push`

    `dvc push`

4) **Pulling a file**:

    `dvc pull {folder_name}/{file_name}`

# Testing DVC locally

You can test pulling the DVC files using the following command in the terminal:

`dvc pull`

You can use the following as a guide to push your own file using the following command in the terminal:

`dvc init`

`dvc remote add -d myremote {location to save files}`

`dvc add guide/04_versioning/01_dvc/big_file.csv`

`git add guide/04_versioning/01_dvc/big_file.csv.dvc guide/04_versioning/01_dvc/.gitignore`

`git commit -m "pushing dvc files"`

`git push`

`dvc push`

<!--intro-end-->
