---
title: Webtoon test
author: thl3f
date: 12/8/20
header-includes:
    - \usepackage{graphicx}
    - \usepackage{amsthm}
    - \usepackage{amssymb}
    - \usepackage{amsmath}
    - \usepackage{amsfonts}
    - \usepackage{mathdots}
    - \usepackage{enumerate}
    - \usepackage{tikz}
    - \usepackage{xcolor}
    - \usepackage{tikz-3dplot}
    - \usepackage{hyperref}
    - \usepackage{ifthen}
    - \usepackage{pgfplots}
    - \usepackage[textwidth=3.2in,textheight=5.3333in]{geometry}
    - \usepackage{fontspec}
    - \setmainfont{Lato}
    - \pagenumbering{gobble}
---

Hello and welcome to this WEBTOON series! This is a test of the Markdown WEBTOON system that I am creating to quickly and easily create \LaTeX-based WEBTOONs, by writing them in Markdown, converting them to PDF, and then converting the PDF to PNGs of size 800 pixels by 1280 pixels.

I'm not sure why WEBTOONs have to be of this size. I think it is because it is somewhat high resolution (technically, I think 720p is considered "HD") but is still low enough resolution to be loaded reasonably quickly on most users' cellphones -- which, of course, are the primary modicum of consumption of WEBTOON content. 

# Markdown Basics

Let's try out some Markdown features. In order to create a heading, we do as follows:

```Markdown
# This is a large heading

## This is a subheading

### This is a subsubheading

#### This is a subsubsubheading

##### This is a subsubsubsubheading

###### This is a subsubsubsubsubheading
```

This, of course, produces the following:

# This is a large heading

## This is a subheading

### This is a subsubheading

#### This is a subsubsubheading

##### This is a subsubsubsubheading

###### This is a subsubsubsubsubheading



Text formatting is easy in Markdown. 

```Markdown
**This text will be bold**

*This text will be italicized*

_This text will also be italicized_

~~This text will be struck through~~

***This text will be both bold and italicized***
```

\verb+`This text will be monospaced`+

This produces:

**This text will be bold**

*This text will be italicized*

_This text will also be italicized_

~~This text will be struck through~~

***This text will be both bold and italicized***

`This text will be monospaced`

# Some issues

## Cropping 

Let me clear up some things. It should be pretty clear that the "\*\*\*This text will be both bold and italicized\*\*\*" is cut off towards the end. This is because code does not have text wrapping in \LaTeX (or in usual Markdown for that matter). Since the code makes the page wider than 800 pixels, it gets cropped out.

For those readers who don't really care about that (since you probably won't be writing much code in a WEBTOON that goes over 48 characters on a line, although who am I to judge), I'll give you a reason to *be concerned*: **The same non-wrapping behavior occurs with displaystyle math**. For people who are writing in Markdown and using \LaTeX syntax, this is obviously much more of an issue. The simple fix for this is just not to write very long mathematical equations in displaystyle; something like the following will just get cut off:

$$\int_{-\infty}^{550} f_{X_1|X_2}(x_1|600)\; dx_1 = \int_{-\infty}^{550} \frac{\frac{1}{2\pi 12000 \sqrt{1-.6^2}} \text{exp} 
\Bigg\{ - \frac{\frac{(600-500)^2}{100^2} - 2(.6) \frac{(600-500)(x_1-500)}
{12000} + \frac{(x_1-500)^2}{120^2}}{2(1-.6^2)} \Bigg\}}
{\frac{1}{120 \sqrt{2\pi}} e^{-\frac{1}{2}(\frac{600-500}{120})^2}}\; dx_1 \approx 0.451966$$

This is of course an extreme example. What are some alternative ways that this could have been displayed?

Consider:

* using the `align` environment
* using `multiline` for a long equation
* using inline math instead of display math
* simplifying the equation rather than leaving it all messy as in the above example
* not having such a long equation in the first place

For example, the following math displays perfectly:

\begin{align*}
\frac{d f}{dx} &= \frac{d}{dx}\Bigg[\frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}\Bigg]\\
\frac{d f}{dx} &= -\frac{d}{dx}\Bigg[\frac{(x-\mu)^2}{2\sigma^2}\Bigg]\times\frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}\\
\frac{d f}{dx} &= -\frac{1}{2\sigma^3\sqrt{2\pi}}\frac{d}{dx}\Big[(x-\mu)^2\Big] e^{-\frac{(x-\mu)^2}{2\sigma^2}}\\
\frac{d f}{dx} &= -\frac{e^{-\frac{(x-\mu)^2}{2\sigma^2}}(x-\mu)}{\sqrt{2\pi}\sigma^3}
\end{align*}

But even with the `align` environment, long equations can still get cut off:

\begin{align*}
g(x) &= -\frac{e^{-\frac{(x-\mu)^2}{2\sigma^2}}(x-\mu)}{\sqrt{2\pi}\sigma^3}\\
\frac{dg}{dx} &= \frac{d}{dx}\Bigg[-\frac{e^{-\frac{(x-\mu)^2}{2\sigma^2}}(x-\mu)}{\sqrt{2\pi}\sigma^3}\Bigg]\\
\frac{dg}{dx} &= -\frac{1}{\sqrt{2\pi}\sigma^3}\frac{d}{dx}\bigg[e^{-\frac{(x-\mu)^2}{2\sigma^2}}(x-\mu)\bigg]\\
\frac{dg}{dx} &= -\frac{1}{\sqrt{2\pi}\sigma^3}\Bigg[\frac{d}{dx}\bigg[e^{-\frac{(x-\mu)^2}{2\sigma^2}}\bigg](x-\mu) + e^{-\frac{(x-\mu)^2}{2\sigma^2}}\frac{d}{dx}(x-\mu)\Bigg]\\
\frac{dg}{dx} &= -\frac{1}{\sqrt{2\pi}\sigma^3}\Bigg[-\frac{(x-\mu)e^{-\frac{(x-\mu)^2}{2\sigma^2}}}{\sigma^2}(x-\mu) + e^{-\frac{(x-\mu)^2}{2\sigma^2}}\Bigg]\\
\frac{dg}{dx} &= -\frac{1}{\sqrt{2\pi}\sigma^3}\Bigg[-\frac{(x-\mu)^2e^{-\frac{(x-\mu)^2}{2\sigma^2}}}{\sigma^2} + e^{-\frac{(x-\mu)^2}{2\sigma^2}}\Bigg]
\end{align*}

## Other issues

Some readers might have noticed that there can sometimes be abnormal spaces in between various blocks of text. This is due to cropping as well -- it is a little complicated but for those interested in the reason this happens, check out the "How It Works" portion.

Evidently, the script should be run multiple times and the user should check the output in order to ensure that it is working correctly. Speaking of which, how does the script work?

# How It Works

The script is written in Python, since Python is easy to write and very readable. Also I know Python well. I could have written it in Bash or something, but Bash as a programming language is carcinogenic and should be banned. Python's `os.system()` function works just fine for scripting. 

## How to run the script

In order to run the script, one simply needs to open up the terminal and execute the following:

```
python /path/to/script.py/ file.md
```

...where `file.md` is the Markdown file to convert, and `/path/to/script.py/` is obviously the path to the script on the user's computer. **Make sure that the version of Python being referenced by `python` is Python 3**. (This will be discussed in the "Dependencies" section as well.)

After the script is done, the user will have a set of numbered PNG images in their current directory ready to be used for a WEBTOON!

## How the script actually works, on the inside

Python as a programming language has been described by many as "functional pseudocode", and for good reason. If you want to see for yourself how the program works, it should be pretty simple to just read each line. But for those who are less interested in Python and more interested in making sure the script doesn't just wipe their hard drive, let's talk about what happens.

The script itself is basically just a collection of commands that could be typed in the terminal, run via the `os.system()` Python module. Here's what it does:

1. Get the filename from user input (the `file` part of `file.md` in the example above)
2. Use `pandoc` to create a PDF from the Markdown file
3. Crop some of the excess whitespace with `pdfcrop`
4. Use ImageMagick's `convert` tool to convert the PDF to a set of 800 pixel by 1320 pixel PNGs, one for each page of the PDF, and stack them vertically together
5. Cut the long image generated in step 4 into PNGs of height 1280 pixels, so that they are usable in a WEBTOON

# Dependencies

Unfortunately, you can't just download the script, run it with a Markdown file as an argument, and expect everything to go swimmingly right off the bat. There are some programs that you need to install first:

* UNIX -- this script will only work on UNIX-based machines. It could probably be made to work on Windows machines as well, but scripting for Windows is best done when one is completely wasted and usually in AutoHotKey, not in a real language like Python
* Python 3 -- many users might have Python 2 preinstalled on their machine. You can check what version of python the command `python` refers to by doing `python --version` in the terminal. If you get some Python 2.X as your output, try `python3 --version`. If that gives you an error, you need to install Python. You can Google your platform-specific instructions (or, if you're on Linux, just install it with your system's package manager)
* `pandoc` -- you can check whether you have this by typing `pandoc` into the terminal. If it says something along the lines of "No such file or directory", you don't have it installed. Either Google it or install it with your system's package manager
* \LaTeX -- the script uses `xelatex` as the compiler, which should come with a full TeXLive installation.
* `pdfcrop` -- generally part of TeXLive's utilities, but can probably be installed separately if necessary
* ImageMagick -- sometimes preinstalled, but always useful. Get it if you don't have it already, even if you don't plan on using the script

So now that you have everything installed, you might wonder where you can get this magical Python script. Well, if you're too lazy to write it yourself (seriously, it's only like 26 lines with comments and breaks, and fewer than 15 lines without) you can find it at the GitHub link in the Author's comments below.

# Writing the Markdown file

I went over some of the Markdown basics before, but now we need to get into the `pandoc`-specific important things that you need to know. To generate a title and author and date like the ones I have at the top of this WEBTOON, you need something called a "YAML" block, which looks like this:

```markdown
---
title: Webtoon test
author: thl3f
date: 12/8/20
---
```

Then, in order to get all the fun packages you want to include for the \LaTeX, you'll need a `header-includes` section in your YAML header, which for this document looks like this (although this is ***definitely*** overkill for what I'm doing here):

```markdown
header-includes:
    - \usepackage{graphicx}
    - \usepackage{amsthm}
    - \usepackage{amssymb}
    - \usepackage{amsmath}
    - \usepackage{amsfonts}
    - \usepackage{mathdots}
    - \usepackage{enumerate}
    - \usepackage{tikz}
    - \usepackage{xcolor}
    - \usepackage{tikz-3dplot}
    - \usepackage{hyperref}
    - \usepackage{ifthen}
    - \usepackage{pgfplots}
    - \usepackage[textwidth=3.2in,textheight=5.3333in]{geometry}
    - \usepackage{fontspec}
    - \setmainfont{Lato}
    - \pagenumbering{gobble}
```

The geometry package's header entry is probably cut off due to the length of the line. Here it is, sliced up:
`\usepackage[textwidth=3.2in,`

`textheight=5.3333in]{geometry}`

All together, the header might look something like this (some packages omitted):

```markdown
---
title: Webtoon test
author: thl3f
date: 12/8/20
header-includes:
    - \usepackage[textwidth=3.2in,textheight=5.3333in]{geometry}
    - \usepackage{fontspec}
    - \setmainfont{Lato}
    - \pagenumbering{gobble}
---
```

The `geometry` package mentioned above is actually **very necessary** because it helps make sure the text fits within a region reasonably close to the WEBTOON horizontal pixel limit of 800. The `fontspec` package is used for setting the font to something other than the default serif font, and the `\setmainfont` command specifies that we want the font to be "Lato". The somewhat weirdly-named `\pagenumbering{gobble}` command removes all page numbering as it's unnecessary for a WEBTOON.

Also, please don't feel compelled to copy everything here down from the images; this header code will all be available at the GitHub link in the Author's comments below.

And that's it! Feel free to like this or comment when it (hopefully but probably not) works for you!




