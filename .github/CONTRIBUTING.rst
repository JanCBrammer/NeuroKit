Contributing
============


**All people are very much welcome to contribute to code, documentation, testing and suggestions.**

This package aims at being beginner-friendly. Even if you're new to this open-source way of life, new to coding and github stuff, we encourage you to try submitting pull requests (PRs). 

- *"I'd like to help, but I'm not good enough with programming yet"*

It's alright, don't worry! You can always dig in the code, in the documentation or tests. There are always some typos to fix, some docs to improve, some details to add, some code lines to document, some tests to add... Just explore the code structure, find where functions are located, where documentation is written, where tests are made, and see what you can fix. **Even the smaller PRs are appreciated**.

- *"I don't know how to code at all :("*

You can still contribute to the `documentation <https://github.com/neuropsychology/NeuroKit/tree/master/docs>`_ by creating tutorials, help and info!

- *"I'd like to help, but I don't know where to start"*

You can look around the **issue section** to find some features / ideas / bugs to start working on. You can also open a new issue **just to say that you're there, interested in helping out**. We might have some ideas adapted to your skills.

- *"I'm not sure if my suggestion or idea is worthwile"*

Enough with the impostor syndrom! All suggestions and opinions are good, and even if it's just a thought or so, it's always good to receive feedback.

- *"Why should I waste my time with this? Do I get any credit?"*

Software contributions are getting more and more valued in the academic world, so it is a good time to collaborate with us! All contributors will be added within the `**authors list** <https://neurokit2.readthedocs.io/en/latest/credits.html>`_. We're also very keen on including them to eventual academic publications.


**Anyway, starting is the most important! You will then enter a *whole new world, a new fantastic point of view*... So fork this repo, do some changes and submit them. We will then work together to make the best out of it :)**


How to push changes
-------------------

- NeuroKit has two main branches, *master* and the *dev*. The typical workflow is to first PR your changes to the dev branch. And every now and then, the dev branch is merged into master (and the version is incremented).
- In other words, you should never directly make changes on the *master* branch, because *master* is usually behind *dev* (maybe the the things you are changing on *master* have already been changed on *dev*?) and because it should be a stable, tested branch. Whereas on *dev* is the place to experiment.


The typical workflow is the following:


1. Download `GitHub Desktop <https://desktop.github.com/>`_ and follow the small tutorial that it proposes
2. *Fork* the NeuroKit repository (can be done on the GitHub website page), and clone it using GitHub Desktop to your local computer (it will copy over the whole repo from GitHub to your local machine)
3. In GitHub Desktop, switch to the *dev* branch. You are now on the *dev* branch (of your own fork)
4. From there, create a new branch, called for example "bugfix-functionX" or "feature-readEEG" or "typofix"
5. Push some changes
6. Create a pull request (PR) from your fork to the "origin" (the original repo) dev branch
7. Wait for it to be merged into dev, and see it being merged into master






Structure and code
-------------------

- NeuroKit is currently organized into submodules, such as *ecg*, *signal*, *statistics*, etc.
- The API (the functions) should be consistent, with functions starting with a prefix (`plot_`, `ecg_`, `eda_`, etc.) so that the user can easily find them by typing the "intuitive" prefix.
- Authors of code contribution are invited to follow the `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ style sheet to write some nice (and readable) python.
- That being said, *human readability* should always be favoured over anything else. Ideally, we would like the code in NeuroKit to be understandable even by non-programmers.
- Contrary to Python recommandations, we prefer some nicely nested loops, rather than complex one-liners `["that" for s if h in i for t in range("don't") if "understand" is False]`.
- Please *document and comment* your code, so that the purpose of each step (or code line) is stated in a clear and understandable way.
- Don't forget to add tests and documentation to your functions.


Useful reads
------------

*For instance, one way of starting to contribute could be to improve this file, fix typos, clarify things, add ressources links etc :)*

- `Understanding the GitHub flow <https://guides.github.com/introduction/flow/>`_
- `How to create a Pull Request <https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/github-collaboration/how-to-submit-pull-requests-on-github/>`_

