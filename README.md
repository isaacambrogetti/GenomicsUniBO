# GenomicsUniBO 🧬🌴
Repository of UniBo's Genomics course material. 

> It's not an official page of the University of Bologna.

This repository contains notes, resumes, mock exams and common exam questions of the bachelor Genomics Bachelor's degree.  

Help is very welcome! Feel free to download and add your own material to contribute to this public repository 💙  

### Here's a quick guide

Rules to upload files:
- When adding a file, its name should be: [course] _ [module] _ [resume/notes] _ [author name and surname initial / unknown]
- Add files to the corresponding folder, the structure is the following:  
    ```
    academic_year > course_name (> subcourse) (> module) > year > file_types (if lab matherial, slides, resumes, etc) > the file  
    ```
- If the folder is not already present you can make it yourself.  
There are some few exeptions to the folder structure, if you have doubt ask or just create the pull request and we can modify it together.


DO NOT! 💢 🚯
- DO NOT SHARE EXAM ANSWERS (mock exams are fine)
- DO NOT SHARE Bioinformatics homeworks
- DO NOT SHARE lab reports

_____

## How to upload files

### The dumb way :fishing_pole_and_fish:

- Open the repository on GitHub
- Navigate to the folder were you want to place the files
- click on the add file button > upload files
- add your files
- describe what you uploaded in "Sign off and commit changes"
- choose select a new branch for this git commit and start a pull request

your request will be checked and approved.

:warning: **Issue with this method:**
- you will be able to add all the files you want in a single pull request only if they're located in the same folder, otherwise you'll need to open a new pull request for each folder which can be annoying both for you and for who has to check.

### The nerd way :broccoli:
1. clone the repository on your pc or sync the changes if you've already cloned it before
2. create a new branch ```git branch -c your_branch_name```
3. get into your new branch ```git checkout your_branch_name```
4. navigate through the folders of the repository and add your files
5. tell git which files to commit ```git add your_file``` or use ```git add .``` to all of them at once
6. check with ```git status``` if everything is all right. You should see 

    ```
    On branch your_branch_name
    Your branch is up to date with 'origin/main'.

    Changes added to commit:
    ... your files added to the commit ...
    ```
    If you don't see this in stdout, check the previous steps.

7. create the git commit with its description: ```git commit -m "your commit description"```

8. push the commit ```git push origin head```

9. go to the github page under [pulls](https://github.com/isaacambrogetti/GenomicsUniBO/pulls), select your branch and choose pull request.

___

It might seem scary at the beginning but don't worry, if you get anything wrong you're not going to brake the github page.

Have fun and be kind <3
