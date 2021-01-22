# job_scrappy -- A script to pull facts from specific job pages

Ok the reason for this to exist is that I am tired of copy pasting stuff from job web pages and I would like a machine to do it for me.

# Feature set to implement

- [ ] Command line interface to allow:
  - [ ] Take an url and which file to save to.
  - [ ] Take a file with a list of urls and tell it which file to save to.
  - [ ] Take a document name and a recently scrapped data file to create a document with a specific format.
- [ ] Having ability to parse web content:
  - [ ] Having a specific parser to parse a specific website (that has specific structure of course).
- [ ] Content saving capability as well as persistence:
  - [ ] Use json format files to store the content.
  - [ ] Implement the logic:
    - [ ] to check file's existence
    - [ ] getting it as a JSON (i.e. dict data structure)
    - [ ] merging **new** content into **existing** one and saving it back.
- [ ] Implement a capability to create a Word document to present the data:

# Fixing some weird bugs
- Use the link below to fix ipython bug where it crashes when you don't see any auto completion.
  - [here](https://github.com/ipython/ipython/issues/12745#issuecomment-752777081)
