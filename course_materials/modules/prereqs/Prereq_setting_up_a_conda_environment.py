# %% [markdown]
# # Conda Environment Setup for Neurogenomics
# This notebook will guide you through the steps to set up a Conda environment for the fall 2025 Neurogenomics course.
# Make sure you have Conda installed on your system. You can download it from the [Miniforge github repository](https://github.com/conda-forge/miniforge). 
#
# You can find the specific installation instructions [here](https://github.com/conda-forge/miniforge?tab=readme-ov-file#install).


#%% [markdown]
# ## What is conda/mamba/anaconda?
# Conda is an open-source _package management system_ and environment management system that runs on Windows, macOS, and Linux. It is used to install, run, and update packages and their dependencies which means that it allows you to 'compartmentalize' your projects and have multiple different working environments for different applications or workflows. 
# 
# Mamba is a reimplementation of the conda package manager in C++, which makes it faster and more efficient. Anaconda is a distribution of Python and R and other scientific computing and data science tools as well as many other useful packages.
#
# For all intents and purposes, you can consider conda, mamba, and anaconda to be interchangeable in the context of this course.

# %% [markdown]
# ## Why conda?
# Conda is widely used in the scientific computing and data science communities because it simplifies package management and deployment. It allows users to create isolated environments for different projects, ensuring that dependencies do not conflict with each other. This is particularly useful in fields like genomics and bioinformatics, where different projects may require different versions of libraries and tools.

#%% [markdown]
# ## Create a conda environment from an existing environment definition file

#%% [markdown]
# To get up and running with the course materials, we will create a new conda environment using a predefined YAML file with the necessary packages required for the first modules of this course.  You can use this environment throughout the course if you like, or create your own as needed for your project(s).
#
# The file we will use is located in the course github repository [https://github.com/gofflab/quant_mol_neuro](https://github.com/gofflab/quant_mol_neuro), in the `environment` folder and is named `environment.yml`.  
#
# To download the file directly click [here](https://raw.githubusercontent.com/gofflab/quant_mol_neuro/refs/heads/main/environment/environment.yml).

# %% [markdown]
# Now that we have our environment file, we can create a new conda environment using the following command in the terminal:
#
# ```bash
# conda env create -f environment.yml
# ```
#
# This command will create a new conda environment with all the packages specified in the `environment.yml` file. Once the environment is created, we need to activate it using:
#
# ```bash
# conda activate neurogenomics
# ```
#

#%% [markdown]
# Activating a conda environment is like 'stepping inside' that environment to execute commands or tools contained within. You must be careful throughout the course to ensure that you are working inside the correct enviroment (especially if you create multiple working environments).
#
# Documentation for how to use mamba/conda can be found here: [mamba](https://mamba.readthedocs.io/en/latest/index.html)
#
# A comprehensive video introduction to conda for scientific computing can be found here: [Video Introduction to Conda](https://www.youtube.com/watch?v=qn5zfdJtcYc)
