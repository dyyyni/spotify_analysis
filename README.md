# Spotify Stream History Analysis

## Overview
This project is a data analysis project using Python, analyzing my Spotify streaming data and creating visualizations.

## Getting Started

### Prerequisites

Before you can get started with this project, you need to have Conda installed on your machine. If you don't have Conda installed, you can download and install it from the official Conda website: https://docs.conda.io/en/latest/miniconda.html

### Installing
To get started with this project, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone git@github.com:dyyyni/spotify_analysis.git
```

2. Navigate to the project directory:

```bash
cd spotify_analysis
```

3. Create a new Conda environment for the project:

```bash
conda env create -f environment.yml
```
4. Activate the new Conda environment:

```bash
conda activate dans-spotify-analysis
```
### Get your Spotify fully wrapped

1. Go to https://www.spotify.com/us/account/privacy/ and download your extended
   streaming history. This might take up to 30 days.

2. You will receive your streaming history in email by one or many .json files.

3. Add these .json files to data/raw folder of this project.

4. Run the following command

```bash
python main.py
```
5. Your data is now processed. You'll have an overview of your listens in the
   command line. Figures can be found at ./reports/figures

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Thanks EU and GDPR for making the tech giants bow to us for once.
