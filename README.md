# logic-gate-generator
An interactive web application that parses complex Boolean logic expressions to automatically generate accurate truth tables and render vector-style circuit gate schematics using SymPy, Graphviz, and Streamlit.
⚡ Logic Gate Truth Table & Schematic Generator

An interactive, Python-powered web application built with Streamlit, SymPy, and Graphviz. This application parses arbitrary boolean logic expressions, constructs complete truth tables, and dynamically generates logic circuit schematic diagrams.

🌟 Features

Boolean Expression Parser: Accepts standard boolean operators (AND, OR, NOT).

Truth Table Computation: Calculates all binary input variations ($2^N$ combinations) and outputs a clean, downloadable evaluation table.

Logic Gate Diagram Generation: Dynamically renders visual circuit gate schematics using Graphviz layout trees.

Interactive UI: Fast, responsive web application interface powered by Streamlit.

📁 Repository Structure

├── app.py              # Main Streamlit web application frontend
├── logic_engine.py     # Backend parser, truth table calculator, & schematic generator
├── requirements.txt    # Python dependencies
├── .gitignore          # Environment and cache exclusion rules
└── README.md           # Project documentation


🚀 Quick Start (Local Setup)

1. Prerequisites

Make sure you have Python 3.8+ installed on your system.

System Dependency: Graphviz

Graphviz system binaries are required to render circuit schematics:

Windows: Download and run the installer from Graphviz Downloads. During setup, check "Add Graphviz to system PATH".

macOS: Run brew install graphviz using Homebrew.

Linux (Ubuntu/Debian): Run sudo apt-get install graphviz.

2. Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/logic-gate-generator.git
cd logic-gate-generator


Install Python dependencies:

pip install -r requirements.txt


3. Running the App

Launch the Streamlit web server:

streamlit run app.py


Or via Python executable module:

python -m streamlit run app.py


Your browser will automatically open  https://logic-gate-generator-tent899osrupqsmcuqsw6o.streamlit.app/.

🌐 Deploying to Streamlit Community Cloud (Free)

Push this repository to your GitHub account.

Sign in to share.streamlit.io.

Click New app, select your repository and branch (main).

Set Main file path to app.py.

Click Deploy!

📝 Accepted Syntax Examples

Syntax

Description

Example

AND

Logical Conjunction

A AND B

OR

Logical Disjunction

A OR B

NOT

Logical Negation

NOT A

Parentheses

Precedence Control

(A AND B) OR (NOT C)

🛠️ Built With

Streamlit - Web UI Framework

SymPy - Symbolic Mathematics & Logic Engine

Graphviz - Diagram Construction Engine

Pandas - Data Structures & Tabular Data
