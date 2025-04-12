# Kartaverse Workflows | Gaussian Raytracing on Linux

If you are interested in volumetric rendering and 3DGS (3D Gaussian Splatting) technology, NVIDIA has released a 3D Gaussian Raytracing library for Linux that provides model training and interactive rendering support. The software is available from the [3DGRUT GitHub](https://github.com/nv-tlabs/3dgrut) repository with a permissive Apache 2.0 open-source license.

## Gaussian Raytracing Screenshots

3DGRUT Screen Recording:

[Video](Images/NVIDIA_3dgrut_interactive_gaussian_raytracing.mp4 ':include :type=video controls width=100%')

3DGRUT Model Training:

![3DGRUT Train](Images/NVIDIA_3dgrut_training.png)

3DGRUT Playground RealTime Viewport:

![3DGRUT Playground Garden](Images/NVIDIA_3dgrut_playground_garden.png)

![3DGRUT Playground Bunny](Images/NVIDIA_3dgrut_playground_with_wavefront_obj_bunny.png)

![3DGRUT Playground Lego](Images/NVIDIA_3dgrut_playground_lego.png)

## Setup the Conda environment on MintOS Linux

The following commands can be entered in a new terminal session to install Conda, create a new virtual environment, and install the NVIDIA 3DGRUT libraries:

	sudo apt-get update
	sudo apt install git
	
	wget --no-check-certificate https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh
	chmod -v +x Miniconda*.sh
	./Miniconda3-py39_4.12.0-Linux-x86_64.sh
	
	conda create -y --name "Kartaverse" python==3.11 ipython
	conda activate Kartaverse
	
	cd $HOME
	git clone --recursive https://github.com/nv-tlabs/3dgrut.git
	cd 3dgrut
	chmod +x install_env.sh
	./install_env.sh Kartaverse
	
	conda install conda-forge::cuda-python	  
	pip install rich
	pip install hydra-core --upgrade
	pip install cupy

## Setup 3DGRUT Playground

After you have the NVIDIA 3DGRUT libraries installed, you can add the 3DGRUT interactive viewport called playground to your system:

	conda activate Kartaverse
	cd $HOME/3dgrut/
	pip install -r threedgrut_playground/requirements.txt

## Download the sample datasets:

	https://www.kaggle.com/datasets/nguyenhung1903/nerf-synthetic-dataset
	http://storage.googleapis.com/gresearch/refraw360/360_v2.zip
	https://storage.googleapis.com/gresearch/refraw360/360_extra_scenes.zip

## Download sample Wavefront OBJ models:

	https://github.com/alecjacobson/common-3d-test-models/

## Install the 3DGS benchmark datasets to:

	$HOME/3dgrut/data/

## Install Wavefront .obj formatted polygon 3D models to:

Playground allows you to add your own wavefront obj models to the 3D viewport. These models are rendered with a refractive glass shader.

	$HOME/3dgrut/threedgrut_playground/assets/

## Train a scene

Here is the syntax to train a 3D Gaussian Raytracing model. In this case we are using the classic "bonsai" reference scene:

	conda activate Kartaverse
	cd $HOME/3dgrut/
	python train.py --config-name apps/colmap_3dgut.yaml path=data/bonsai out_dir=runs experiment_name=bonsai_3dgut dataset.downsample_factor=2

Decoding the above shell commands:

The "--config-name" entry allows you to specify a YAML file that is found in the folder "$HOME/3dgrut/config/apps/". There are 3dgrt and 3dgut presets that are optimized for colmap, nerf_synthetic, and scannetpp datasets.

The "path=" entry defines the relative path to the source folder where the image data and camera pose information is loaded from.

The "out_dir=" entry is the relative path to the folder where the model output is saved. Inside this folder is a sub-directory that is defined by the "experiment_name=" entry.

For example, if the "out_dir=runs" and "experiment_name=bonsai_3dgut" CLI parameters are used, then the trained output is saved to the folder:

	$HOME/3dgrut/runs/bonsai_3dgut/

If you run low on GPU VRAM the CLI flag "dataset.downsample_factor=2" should be able to help you tune the memory usage. This attribute lets you hop between the a Colmap trained dataset's pre-computed "images_#" folders. These folders hold proxy pre-scaled resolution versions of your source footage. You can select which footage folder you want to use on a training task by adjusting the "dataset.downsample_factor=#" CLI parameter:

- specifying nothing uses the full resolution images in the "<colmap project>/images/" folder
- dataset.downsample_factor=2 uses the half resolution images in the "<colmap project>/images_2/" folder
- dataset.downsample_factor=4 uses the quarter resolution images in the  "<colmap project>/images_4/" folder
- dataset.downsample_factor=8 uses the eighth resolution images in the "<colmap project>/images_8/" folder

Example Colmap project folder hierarchy:

    project/images/
    project/images_2/
    project/images_4/
    project/images_8/
    project/masks/
    project/project.ini
    project/database.db
    project/sparse/0/cameras.bin
    project/sparse/0/cameras.txt
    project/sparse/0/images.bin
    project/sparse/0/images.txt
    project/sparse/0/points3d.bin
    project/sparse/0/points3d.txt

## View the pre-trained scene using Playground

Once a trained scene has been created, we can load this dataset into a Playground based realtime viewport session.

	conda activate Kartaverse
	cd $HOME/3dgrut/
	python playground.py --gs_object $HOME/3dgrut/runs/bonsai_3dgut/bonsai-1104_201100/ckpt_last.pt

