# NormalCrafter

## Overview

[NormalCrafter](https://github.com/Binyr/NormalCrafter) allows you to create temporally stable normal maps from live action video footage. 

In this case, temporally stable means the features are consistent over time and there is a minimal amount of flicker in a video sequence output.

## Installing NormalCrafter

The following webpages have useful resources for NormalCrafter usage:

- [https://github.com/Binyr/NormalCrafter](https://github.com/Binyr/NormalCrafter)
- [https://normalcrafter.github.io/](https://normalcrafter.github.io/)
- [https://arxiv.org/abs/2504.11427](https://arxiv.org/abs/2504.11427)

Lets following along and continue to use the same virtual environment setup created in the earlier Comfy UI + MatAnyone post.


You can download the content from the NormalCrafter repo using:

```bash
cd %USERPROFILE%
conda activate Kartaverse
python.exe -m pip install --upgrade pip
git clone https://github.com/Binyr/NormalCrafter.git
cd %USERPROFILE%/normalcrafter
pip install -r requirements.txt
```

## Troubleshooting

If you try installing the requirements.txt content you will get back the following error message:

    ERROR: Ignored the following yanked versions: 8.9.4.19
    ERROR: Ignored the following versions that require a different python version: 1.21.2 Requires-Python >=3.7,<3.11; 1.21.3 Requires-Python >=3.7,<3.11; 1.21.4 Requires-Python >=3.7,<3.11; 1.21.5 Requires-Python >=3.7,<3.11; 1.21.6 Requires-Python >=3.7,<3.11
    ERROR: Could not find a version that satisfies the requirement nvidia-cudnn-cu11==8.5.0.96 (from versions: 0.0.1.dev5, 8.9.4.25, 8.9.5.29, 9.0.0.312, 9.1.0.70, 9.1.1.17, 9.2.0.82, 9.2.1.18, 9.3.0.75, 9.4.0.58, 9.5.0.50, 9.5.1.17, 9.6.0.74, 9.7.0.66, 9.7.1.26, 9.8.0.87, 9.9.0.52)
    ERROR: No matching distribution found for nvidia-cudnn-cu11==8.5.0.96
    

Solution:

TBD.
