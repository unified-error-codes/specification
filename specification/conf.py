# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'Unified Error Codes'
copyright = '2026, CharIN e.V. and Contributors'
author = 'CharIN e.V. and Contributors'
version = '0.1'
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Enable figure, table, and code-block numbering
numfig = True
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section %s',
}

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for LaTeX / PDF output ------------------------------------------

latex_engine = 'pdflatex'

latex_documents = [
    (
        'index',                          # startdocname
        'unifiederrorcodes.tex',          # targetname
        'Unified Error Codes',            # title
        'CharIN e.V. and Contributors',   # author
        'manual',                         # theme (manual = book-like)
        False,                            # toctree_only
    ),
]

latex_elements = {
    # -- Paper and basic geometry -------------------------------------------
    'papersize': 'a4paper',
    'pointsize': '11pt',

    # -- Font configuration ------------------------------------------------
    'fontpkg': r'''
\usepackage[T1]{fontenc}
\usepackage{lmodern}            % Latin Modern — clean, professional serif
\usepackage[scaled=0.85]{beramono}  % Bera Mono for code (compact, readable)
\usepackage{microtype}          % Subtle typographic refinements
''',

    # -- Preamble: colours, headers/footers, styling -----------------------
    'preamble': r'''
% ── Colours ────────────────────────────────────────────────────────────
\usepackage{xcolor}
\definecolor{ChapterColor}{RGB}{0, 63, 114}      % Deep navy
\definecolor{SectionColor}{RGB}{0, 63, 114}
\definecolor{LinkColor}{RGB}{0, 83, 155}
\definecolor{CodeBg}{RGB}{246, 248, 250}
\definecolor{CodeFrame}{RGB}{208, 215, 222}
\definecolor{TableHeader}{RGB}{0, 63, 114}
\definecolor{TableHeaderText}{RGB}{255, 255, 255}
\definecolor{TableRowAlt}{RGB}{245, 247, 250}
\definecolor{CaptionColor}{RGB}{80, 80, 80}

% ── Hyperlink styling ─────────────────────────────────────────────────
\hypersetup{
    colorlinks=true,
    linkcolor=LinkColor,
    urlcolor=LinkColor,
    citecolor=LinkColor,
}

% ── Header / Footer ───────────────────────────────────────────────────
\usepackage{fancyhdr}

% Main page style
\fancypagestyle{normal}{
    \fancyhf{}
    \fancyhead[LE]{\small\textcolor{gray}{\leftmark}}
    \fancyhead[RO]{\small\textcolor{gray}{\rightmark}}
    \fancyfoot[C]{\small\thepage}
    \fancyfoot[LE,RO]{\small\textcolor{gray}{Unified Error Codes — v''' + release + r'''}}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.2pt}
}
\pagestyle{normal}

% Plain page style (chapter openers, TOC, etc.)
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[C]{\small\thepage}
    \fancyfoot[LE,RO]{\small\textcolor{gray}{Unified Error Codes — v''' + release + r'''}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0.2pt}
}

% ── Heading styles ────────────────────────────────────────────────────
\usepackage{titlesec}

\titleformat{\chapter}[display]
    {\normalfont\Huge\bfseries\color{ChapterColor}}
    {\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titlespacing*{\chapter}{0pt}{-20pt}{30pt}

\titleformat{\section}
    {\normalfont\Large\bfseries\color{SectionColor}}
    {\thesection}{1em}{}

\titleformat{\subsection}
    {\normalfont\large\bfseries\color{SectionColor}}
    {\thesubsection}{1em}{}

\titleformat{\subsubsection}
    {\normalfont\normalsize\bfseries\color{SectionColor}}
    {\thesubsubsection}{1em}{}

% ── Table styling ─────────────────────────────────────────────────────
\usepackage{colortbl}
\setlength{\arrayrulewidth}{0.3pt}

% ── Tight list spacing ───────────────────────────────────────────────
\usepackage{enumitem}
\setlist{nosep, left=0pt .. 1.5em}

% ── TOC depth ─────────────────────────────────────────────────────────
\setcounter{tocdepth}{3}

% ── Draft / confidential watermark (uncomment if desired) ─────────────
% \usepackage{draftwatermark}
% \SetWatermarkText{DRAFT}
% \SetWatermarkScale{1}
% \SetWatermarkColor[gray]{0.92}
''',

    # -- Custom title page -------------------------------------------------
    'maketitle': r'''
\begin{titlepage}
    \centering
    \vspace*{2cm}

    {\color{ChapterColor}\rule{\textwidth}{2pt}}

    \vspace{1.5cm}

    {\fontsize{36}{42}\selectfont\bfseries\color{ChapterColor} Unified Error Codes\par}

    \vspace{0.8cm}

    {\Large\color{gray} Technical Specification\par}

    \vspace{0.6cm}

    {\color{ChapterColor}\rule{0.5\textwidth}{1pt}}

    \vspace{2cm}

    {\large
    \begin{tabular}{rl}
        \textbf{Version:}  & ''' + release + r''' \\[4pt]
        \textbf{Date:}     & \today \\[4pt]
        \textbf{Authors:}  & CharIN e.V. and Contributors \\[4pt]
        \textbf{Status:}   & Draft \\
    \end{tabular}
    \par}

    \vfill

    {\small\color{gray}%
    \textcopyright\ 2026 CharIN e.V. and Contributors.\\[4pt]
    Licensed under CC-BY-4.0. Code samples under Apache-2.0.}

    \vspace{1cm}
    {\color{ChapterColor}\rule{\textwidth}{2pt}}
\end{titlepage}
''',

    # -- Disable fncychap (conflicts with titlesec) -----------------------
    'fncychap': '',

    # -- Geometry (margins) ------------------------------------------------
    'geometry': r'\usepackage[a4paper, top=30mm, bottom=30mm, left=28mm, right=28mm, headheight=14pt]{geometry}',

    # -- Better code highlighting ------------------------------------------
    'sphinxsetup': (
        'verbatimwithframe=true, '
        'VerbatimColor={RGB}{246,248,250}, '
        'VerbatimBorderColor={RGB}{208,215,222}, '
        'VerbatimHighlightColor={RGB}{255,255,204}, '
        'InnerLinkColor={RGB}{0,83,155}, '
        'OuterLinkColor={RGB}{0,83,155}, '
        'TitleColor={RGB}{0,63,114}, '
        'noteBorderColor={RGB}{0,83,155}, '
        'noteBgColor={RGB}{232,240,254}, '
        'warningBorderColor={RGB}{200,100,0}, '
        'warningBgColor={RGB}{255,243,224}, '
        'dangerBorderColor={RGB}{180,30,30}, '
        'dangerBgColor={RGB}{255,235,235}'
    ),

    # -- Disable default Sphinx list-of-figures/tables at end ----
    'printindex': r'\footnotesize\raggedright\printindex',
}

# -- LaTeX additional files (logo, etc.) -----------------------------------
# latex_additional_files = ['_static/logo.pdf']

# -- PDF metadata -----------------------------------------------------------
latex_show_urls = 'footnote'
latex_show_pagerefs = True
