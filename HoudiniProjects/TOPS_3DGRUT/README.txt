Use NVIDIA 3DGRUT's library to train a 3D Gaussian Raytracing model from the command-line

This HIP file requires you to have launched Houdini/HQueue from inside a virtual environment session that has CUDA Toolkit, Python 3.11, and several other python packages pre-installed:

conda activate Kartaverse
cd $HOME/3dgrut/
houdini

For more information check out:
https://kartaverse.github.io/Kartaverse-for-Houdini/#/3dgrut/3dgrut

Attribute Create Variables:

"MINICONDA_ENV" is the folder pathwhere your active Anaconda Miniconda virtual environment exists at. This is typically a location inside your user accounts home folder like "$HOME/miniconda3/envs/Kartaverse/".

"WORKING_DIR" is the folder path where the 3dgrut Github repo contents are located. Typically this is a folder like "$HOME/3dgrut/".

"SCRIPT_NAME" is the "train.py" script filename.

"CONFIG_NAME" is a relative  YAML filepath. It specifies a .yaml file that exists in a folder like "$HOME/3dgrut/config/apps/". This folder has 3dgrt and 3dgut presets that are optimized for colmap, nerf_synthetic, and scannetpp datasets.

"SOURCE_DIR" is where the camera array source images are located. This could be a path like "$HIP/images/0001". No trailing slash needed.

"OUTPUT_DIR" is where the training run output date is saved. This could be a path like "$HIP/geo". No trailing slash needed.

"EXPERIMENT_NAME" is the sub-folder name for the current project. This folder will be created inside the OUTPUT_DIR folder. The trained model checkpoint file is saved inside this folder and it will typically have several other filename elements appened.

"PROXY_RESOLUTION" allows you to specify if a reduced resolution set of images should be used. To use the original images you can clear out this field. If you run low on GPU VRAM the CLI flag "dataset.downsample_factor=2" should be able to help you tune the memory usage. This attribute lets you hop between the a Colmap trained dataset's pre-computed "images_#" folders. These folders hold proxy pre-scaled resolution versions of your source footage. You can select which footage folder you want to use on a training task by adjusting the "dataset.downsample_factor=#" CLI parameter:

    specifying nothing uses the full resolution images in the "/images/" folder
    dataset.downsample_factor=2 uses the half resolution images in the "/images_2/" folder
    dataset.downsample_factor=4 uses the quarter resolution images in the "/images_4/" folder
    dataset.downsample_factor=8 uses the eighth resolution images in the "/images_8/" folder

3DGRUT Example CLI Syntax:
python train.py --config-name apps/colmap_3dgut.yaml path=data/bonsai out_dir=runs experiment_name=bonsai_3dgut dataset.downsample_factor=2
