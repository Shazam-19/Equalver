# Equalver

Equalver is an advanced mathematical equations calculator with a friendly user interface 
and functionality to help the user interact with it easily.

- User Friendly GUI
- Solve complex equations in less than a second!
- ✨Magic ✨

To Download the Application file use this [link](https://drive.google.com/file/d/1DTTqz2lnBarjfwJPsjxdRrSlh4xBJG2Y/view?usp=sharing).

## Features

- Write an equation in a normal way without the need to specify each multiplication (e.g. **2+4x** instead of 2+4*x).
- Solve Bisection, False Position, Simple Fixed Point, Newton, and Secant-Methods. 
- Export the solution to an _csv_ file to easily copy and modify the answer.

Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Tech

Equalver uses a number of open source language and it's libraries to work properly:

- [Python] - High-Level Programming language for anything on your mind!
- [Sympy] - Symbolic mathematics are easier with this masterpiece.
- [Tkinter] - Python's de-facto standard GUI.
- [CSV] - CSV (Comma Separated Values) format, is a type of files to import and export spreadsheets and databases.
- [Matplotlib] - A cross-platform, data visualization and graphical plotting

And of course Equalver itself is open source with a [public repository][dill] on GitHub.

## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```



## Development

Want to contribute? Great!

Make a fork of the repositry and play with it 
as you want, once you are done; let me know to add your work 
to the main project!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```



## License

MIT License

Copyright (c) [2022] [AbdEl-Rahman Sayed Shehata AbdEl-Hamid Semida]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

**Free Software, Hell Yeah!**



