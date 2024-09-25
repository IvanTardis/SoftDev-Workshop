## K11: Some Things Never Change
### Due: 2024-09-26r before class

Your Trio Mission:

1. In a new directory in your workshop, save a copy of the demo for using flask to serve static files.
1. As a team...
  - Familiarize yourself with the app directory structure and the files' content.
  - Note anything notable.
  - Predict expected behaviors.
  - Spin up your website on localhost and reconcile behavior with prediction.
  - Record your notes in `readme` in app's root directory.
1. Once your team has done this, compose and store another html file named `fixie.html` (containing some html to render your team name and roster) so that flask can serve it staticly.

<br>

DELIVERABLES:
* Save to workshop as indicated.
* Each teammate should submit matching sourcecode.

```
path/to/myworkshop$ tree 11_flask-static
.
├── app.py
├── readme
└── static
    ├── foo
    ├── foo.html
    └── fixie.html
```

<br>

Notes:
- "foo" is just a plaintext file, no HTML or any code, based on the wiki, this is just a file where code is broken down into only readable materials
- foo.html has some actual html tags, and a proper "header" on top
- there are 2 routes and 2 functions

Predictions:
- I think accessing foo will cause just the text of the file to be shown, since there is no route to change the output, and no code in the file to format or anything
- Similar to my prediction for foo, I think the file will be accessed, and since there is actual html code, the text inside the html tags, "Is this plaintext, though?" will be printed on the webpage
- EXTRA ABOUT THE COMMMENTED OUT CODE: I think accessing foo.html, with the code block uncommented, will cause a random decimal between 0.0 and 1.0 to be printed, since Mr.Mykolyk said that the route will execute the function when the file path is accessed, so when you go to static/foo.html, it triggers the function, which will print "the __name__ of this module is... __main__" in the terminal, and will print the random decimal on the webpage

Actual behavior:
- I was wrong, it actually downloads the foo file to my downloads folder when I go to that link
- I was right.
- EXTRA ABOUT THE COMMMENTED OUT CODE: I was correct in the prediction of the behavior



[related](https://ukulelemagazine.com/lessons/uke-lesson-3-chords-and-the-truth-country-songwriting-legend-harlan-howard)  
[related](https://en.wikipedia.org/wiki/Plain_text)  
