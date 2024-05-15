
# Version Control

- All Git Repositories must be on Github Enterprise in their relevant project

- The repository name must follow the naming convention: ProjectName.RepoName
  - i.e : CASM.ResourceCollections
  
- Pre Hooks must be used before commiting code into a repository

- Each development project, that is deployed must have 3 branches:
  - main (production branch)
  - testing (similar to main, but to test everything is ok before merging to production)
  - development (basis for Pull Requests and continious development)

- Each repository that has code must be checked by Github dependend bot. It informs about available updates and mentions security issues  

- each change must have an associated issue / task 
  - Because this way all work is done in isolation on a dedicated branch rather than the main branch. It allows you to submit multiple pull requests without confusion. You can iterate without polluting the master branch with potentially unstable, unfinished code

- branch out from dev/development
  - This way, you can make sure that code in master will almost always build without problems, and can be mostly used directly for releases (this might be overkill for some projects).
  
- do not push to development, testing or main, instead use Pull Requests
  - It notifies team members that they have completed a feature. It also enables easy peer-review of the code and dedicates forum for discussing the proposed feature.

- Update your local development branch and do an interactive rebase before pushing your new code and creating pull requests
  - Rebasing will merge in the requested branch (master or develop) and apply the commits that you have made locally to the top of the history without creating a merge commit (assuming there were no conflicts). Resulting in a nice and clean history.

- Resolve potential conflicts while rebasing and before making a Pull Request.

- Delete local and remote feature branches after merging.
  - It will clutter up your list of branches with dead branches. It ensures you only ever merge the branch back into (development) once. Feature branches should only exist while the work is still in progress.
- for each issue a new pull request (PR) is created

- if more than 1 person develops code, a PR must be voted on by all developers
  - the goal is to keep everyone informed about each code change and keeping the integrity of the code quality

- Before making a Pull Request, make sure your feature branch builds successfully and passes all tests (including code style checks).
  

- a lead / manager, that does not spend more than 50% of their allocated time coding, does not have the right to reject a PR
  - the reason is, they do not know the code base and hence cannot make code related decisions 

- every PR must include unit / integration tests that cover the changes

- unit / integration tests must pass, if a test fails it must be fixed

The workflow looks like this:

```
git checkout -b <branchname>
# Either
git add -p

# for the lazy ones, but this adds everything
git add . 

# more granular
git add file1 file2 file3


git checkout development
git pull

git checkout <branchname>
git rebase -i --autosquash development

git push
```

If you are using the Github Pull Requests extension for VScode, you can use the editor to "start working on an issue" which will create a new branch for you and also help you create a pull request"


For a `README.md` template you can use the one from the [examples folder](./examples/README.md)

Make use of the github templates for issues, such as Bug or Feature Request.




