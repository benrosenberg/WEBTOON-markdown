# WEBTOON-markdown
Convert a Markdown file into a series of WEBTOON-sized PNGs with pandoc, pdfcrop, and ImageMagick!

To see the results of this Python script, check out the WEBTOON generated with it [here](https://www.webtoons.com/en/challenge/webtoons-with-markdown-and-latex/list?title_no=561496).

Here's the header used for that WEBTOON:

```markdown
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
```