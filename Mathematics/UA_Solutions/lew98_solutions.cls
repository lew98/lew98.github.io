\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{lew98_solutions}[lew98 Solutions Class]

\LoadClass[12pt]{report}

% Disable synctex
\synctex=0

% Packages
\RequirePackage[utf8]{inputenc}

\RequirePackage{amsmath, amsfonts, amsthm, mathtools}
\setcounter{MaxMatrixCols}{12}

\RequirePackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=[RGB]{10, 141, 255},
    urlcolor=[RGB]{10, 141, 255}
}
\RequirePackage[nameinlink]{cleveref}

\RequirePackage{enumitem}
\setlist[enumerate,1]{label={(\alph*)}, parsep=0mm, listparindent=6mm, topsep=2mm}

\RequirePackage{tocloft}
\setlength{\cftbeforetoctitleskip}{6mm}
\setlength{\cftaftertoctitleskip}{2mm}
\renewcommand{\cfttoctitlefont}{\Large\bfseries}

\RequirePackage{geometry}
\geometry{
    headheight=15pt,
    left=60pt,
    right=60pt
}
\linespread{1.2}
\allowdisplaybreaks
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\lhead{\nouppercase{\rightmark}}
\chead{}
\rhead{\thepage}
\fancypagestyle{plain}{
  \fancyhf{}
  \rfoot{\thepage}
  \renewcommand{\headrulewidth}{0mm}
  \renewcommand{\footrulewidth}{0mm}
}

\RequirePackage{chngcntr}
\RequirePackage[justification=centering]{caption}
\RequirePackage{float}

\RequirePackage[dvipsnames]{xcolor}

\RequirePackage{graphicx}
\RequirePackage{subcaption}
\RequirePackage{tikz}
\usetikzlibrary{matrix, patterns, decorations.pathreplacing, calligraphy}
\RequirePackage{tikz-cd}
\RequirePackage[edges]{forest}

\setlength{\emergencystretch}{10mm}

% New commands
\newcommand{\interior}[1]{%
  {\kern0pt#1}^{\mathrm{o}}%
}
\newcommand{\setcomp}[1]{#1^{\mathsf{c}}}

\newcommand{\ts}{\textsuperscript}

\newcommand{\hspaceand}[1][8mm]{\hspace{#1} \text{and} \hspace{#1}}

\newcommand{\N}{\mathbf{N}}
\newcommand{\Z}{\mathbf{Z}}
\newcommand{\Q}{\mathbf{Q}}
\newcommand{\I}{\mathbf{I}}
\newcommand{\R}{\mathbf{R}}
\newcommand{\C}{\mathbf{C}}

% Delimiters
\makeatletter
\newcommand{\DeclarePairedDelimiterSwapped}[3]{%
  \expandafter\DeclarePairedDelimiter\csname RIGHT\string#1\endcsname{#2}{#3}%
  \newcommand#1{%
    \@ifstar{\csname RIGHT\string#1\endcsname}
            {\@ifnextchar[{\csname RIGHT\string#1\endcsname}
                          {\csname RIGHT\string#1\endcsname*}%
            }%
  }%
}
\makeatother

\DeclarePairedDelimiterSwapped\abs{\lvert}{\rvert}
\DeclarePairedDelimiterSwapped\norm{\lVert}{\rVert}
\DeclarePairedDelimiterSwapped\paren{(}{)}
\DeclarePairedDelimiterSwapped\bkt{[}{]}
\DeclarePairedDelimiterSwapped\set{\{}{\}}

% Environments
%% Exercise environment
\newtheoremstyle{exercise}
  {}
  {}
  {}
  {}
  {\bfseries}
  {.}
  { }
  {\thmname{#1} \thmnumber{#2}\thmnote{ (#3)}}
\theoremstyle{exercise}
\newtheorem{exercise}{Exercise}[section]

\crefname{exercise}{exercise}{exercises}

%% Solution environment
\newtheoremstyle{solution}
  {}
  {}
  {}
  {}
  {\bfseries}
  {.}
  { }
  {\thmname{#1}\thmnote{ #3}}
\theoremstyle{solution}
\newtheorem*{solution}{Solution}

%% Lemma environment
\newtheoremstyle{lemma}
  {}
  {}
  {}
  {}
  {\bfseries}
  {.}
  { }
  {\thmname{#1} L.\thmnumber{#2}\thmnote{ (#3)}}
\theoremstyle{lemma}
\newtheorem{lemma}{Lemma}

\Crefformat{lemma}{#2Lemma L.#1#3}

%% Figure environment
\renewcommand{\figurename}{Figure F.}

\makeatletter
\def\fnum@figure{\figurename\thefigure}
\makeatother

\counterwithout{figure}{chapter}

\Crefformat{figure}{#2Figure F.#1#3}