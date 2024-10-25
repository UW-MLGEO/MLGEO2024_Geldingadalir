# Tremor Clustering in Iceland's 2021 Geldingadalir Eruption

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to our project repository for the analysis of seismic tremor signals from the 2021 Geldingadalir eruption in Iceland. Using unsupervised machine learning, we aim to uncover hidden patterns in continuous seismic data to enhance understanding of volcanic activity.

## Project Overview ##

In this project, we replicate and expand upon the findings from the paper <a href="https://www.nature.com/articles/s43247-023-01166-w">Tremor clustering reveals pre-eruptive signals and evolution of the 2021 Geldingadalir eruption of the Fagradalsfjall Fires, Iceland</a>. The paper demonstrates the use of machine learning to analyze tremor signals and detect pre-eruptive activity.

We apply Deep Embedded Clustering (DEC), an unsupervised machine learning technique, to seismic data collected during the eruption. DEC allows us to automatically detect various eruption phases by clustering the continuous tremor signals. Notably, this analysis led to the identification of a previously unknown eruption phase by the authors, highlighting the potential for unsupervised learning in volcanic monitoring.

<figure>
    <img src = "images/fagradalsfjall_eruption.png" alt="Lava Flows From Fagradalsfjall" width="80%">
    <figcaption> Lava Flows From Fagradalsfjall. Photo credit: NASA Earth Observatory
</figure>

## Project Objectives ##

- Understand and reproduce the results from our analysis of the 2021 Geldingadalir eruption.
- Expand the application of DEC to new seismic datasets from different volcanic events.
- Explore the potential for real-time monitoring of volcanic activity using similar techniques.

## Our Process

- Step through the code: We will carefully review the workflow to ensure full comprehension of the methods and results.
- Reproduce results: We will run the provided code to verify that the clustering and phase identification techniques produce consistent results.
- Apply to new data: Once verified, we will test DEC on new seismic datasets to uncover additional insights.
- Investigate real-time potential: Ultimately, we hope to explore the possibility of implementing these methods for real-time seismic event monitoring, using insights from the original paper.

## Environment Setup ##

These instructions are for a *nix system.

```python
git clone https://github.com/UW-MLGEO/MLGEO2024_Geldingadalir
conda env create -f geldingadalir.yml
conda activate ml
pip install -r requirements.txt
```

## Repository Structure ##
```python
.
├── ClusTremor-main                     # Original model
├── LICENSE                             # MIT License information
├── README.md
├── docs                                # Supporting documentation
│   └── test.txt
├── notebooks
│   ├── Data_Cleaning.ipynb             # Data Cleaning notebook - Alaska
│   ├── Dimensionality_Reduction.ipynb  # Dimensionality Reduction notebook - Alaska
│   ├── Download_Data.ipynb             # Data Download notebook - Alaska
│   ├── EDA.ipynb                       # EDA notebook - Alaska
│   ├── Prepare_AI_Ready_Data.ipynb     # Data Preparation notebook - Alaska
│   └── data                            # Data - Alaska
│       ├── ai_ready
│       ├── clean
│       └── raw
├── tests                               # Staging for future test modules
│   └── test_modules.py
└── 
```

## Subproject Branches ## 
```python
9F_HOPS_analysis        # Data processing results from 9F.HOPS of the Iceland Reykjanes experiment 2021
StHelens_analysis       # Data processing results from CC.STD of the Cascade Chain Volcano Monitoring network
```

## Pronounciaion
Geldingadlir:  [ˈkɛltiŋaˌdalɪr̥]

<a href="https://en.wikipedia.org/wiki/File:Fagradalsfjall.ogg">Fagradalsfjall</a>: [ˈfaɣraˌtalsˌfjatl̥]
