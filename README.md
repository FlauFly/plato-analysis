# plato-analysis - Graph/Network theoretic analysis of Stanford Encyclopedia of Philosophy

Project goal is to analyse connection between articles on Stanford Encyclopedia of Philosophy by using graph and network theory tools.

## Table of contents
* [General info](#general-info)
* [Quick Start](#quick-start)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project analises network of connections between articles on Stanford Encyclopedia of Philosophy (SEP), which is widely acknowledged resource in the field of philosophy. Every article at the end of page has "Related Entries" segment which links other articles. This connections were used to create directed graph representing totality of connection between various topics in philosophy as represented by SEP. Various graph and network theoretic tools were used on generated graph to gain insight into SEP representation of philosophy.

## Quick Start
If you want only to see final effect of analysis, head to analysis.ipynb. It is ready notebook file, with outputs already processed and ready to see.

## Technologies
List of technologies:
* Python
* Jupyther Lab
* Pandas
* Networkx

## Setup

This project doesn't require setup, if you want only to see final effect of analysis (look at Quick Start). If you want to reproduce and/or modify project locally, clone repository and then write in terminal:

$ cd plato-analysis
$ conda env create -f environment.yml
$ conda activate plato





