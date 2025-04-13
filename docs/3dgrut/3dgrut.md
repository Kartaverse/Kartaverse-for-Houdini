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

## 3DGRUT Command-Line Flags

If you want to start automating things with custom shell scripts it's handy to know what options exist in the 3DGRUT toolset.

### Train CLI Flags

The 3DGRUT Train CLI Parameters can be listed in the terminal using:

    conda activate Kartaverse
    cd $HOME/3dgrut/
    python train.py --h

The output is:

    usage: train.py [--help] [--hydra-help] [--version] [--cfg {job,hydra,all}] [--resolve] [--package PACKAGE] [--run]
                    [--multirun] [--shell-completion] [--config-path CONFIG_PATH] [--config-name CONFIG_NAME]
                    [--config-dir CONFIG_DIR] [--experimental-rerun EXPERIMENTAL_RERUN]
                    [--info [{all,config,defaults,defaults-tree,plugins,searchpath}]]
                    [overrides ...]
    
    python train.py --hydra-help
    Hydra (1.3.2)
    See https://hydra.cc for more info.
    
    == Flags ==
    --help,-h : Application's help
    --hydra-help : Hydra's help
    --version : Show Hydra's version and exit
    --cfg,-c : Show config instead of running [job|hydra|all]
    --resolve : Used in conjunction with --cfg, resolve config interpolations before printing.
    --package,-p : Config package to show
    --run,-r : Run a job
    --multirun,-m : Run multiple jobs with the configured launcher and sweeper
    --shell-completion,-sc : Install or Uninstall shell completion:
        Bash - Install:
        eval "$(python train.py -sc install=bash)"
        Bash - Uninstall:
        eval "$(python train.py -sc uninstall=bash)"
    
        Fish - Install:
        python train.py -sc install=fish | source
        Fish - Uninstall:
        python train.py -sc uninstall=fish | source
    
        Zsh - Install:
        Zsh is compatible with the Bash shell completion, see the [documentation](https://hydra.cc/docs/1.2/tutorials/basic/running_your_app/tab_completion#zsh-instructions) for details.
        eval "$(python train.py -sc install=bash)"
        Zsh - Uninstall:
        eval "$(python train.py -sc uninstall=bash)"
    
    --config-path,-cp : Overrides the config_path specified in hydra.main().
                        The config_path is absolute or relative to the Python file declaring @hydra.main()
    --config-name,-cn : Overrides the config_name specified in hydra.main()
    --config-dir,-cd : Adds an additional config dir to the config search path
    --experimental-rerun : Rerun a job from a previous config pickle
    --info,-i : Print Hydra information [all|config|defaults|defaults-tree|plugins|searchpath]
    Overrides : Any key=value arguments to override config values (use dots for.nested=overrides)
    
    == Configuration groups ==
    Compose your configuration from those groups (For example, append hydra/job_logging=disabled to command line)
    
    hydra: config
    hydra/env: default
    hydra/help: default
    hydra/hydra_help: default
    hydra/hydra_logging: default, disabled, hydra_debug, none
    hydra/job_logging: default, disabled, none, stdout
    hydra/launcher: basic
    hydra/output: default
    hydra/sweeper: basic
    
    
    Use '--cfg hydra' to Show the Hydra config.

### Playground CLI Flags

The 3DGRUT Playground CLI Parameters can be listed in the terminal using:

    conda activate Kartaverse
    cd $HOME/3dgrut/
    python playground.py --h

The output is:

    usage: playground.py [-h] --gs_object GS_OBJECT [--mesh_assets MESH_ASSETS] [--default_gs_config DEFAULT_GS_CONFIG]
                         [--buffer_mode {host2device,device2device}]
    
    options:
      -h, --help            show this help message and exit
      --gs_object GS_OBJECT
                            Path of pretrained 3dgrt checkpoint, as .pt / .ingp / .ply file.
      --mesh_assets MESH_ASSETS
                            Path to folder containing mesh assets of .obj or .glb format.
      --default_gs_config DEFAULT_GS_CONFIG
                            Name of default config to use for .ingp, .ply files, or .pt files not trained with 3dgrt.
      --buffer_mode {host2device,device2device}
                            Buffering mode for passing rendered data from CUDA to OpenGL screen buffer.Using device2device
                            is recommended.



## Houdini TOPs (Task Operator) Workflows

The next step is to hop into the deep end and explore 4D Gaussian Raytracing workflows. To do this we need to add a layer of workflow automation to the mix. We are going to do this with help of SideFX [Houdini TOPs](https://www.sidefx.com/docs/houdini/tops/index.html) (task operators) nodes. 

This approach makes it possible to create modular, reusable, node-graphs that control NVIDIA's 3DGRUT library using the command-line. The end goal is to create a fully templated system that can train a single static scene. The same nodes can be expanded to create a flexible 4D Gaussian Raytracing "video-grammetry" pipeline that can be run locally or in the cloud.

When using the 3DGRUT training system, it's possible to prepare your dataset and solve the camera pose using either [COLMAP](https://colmap.github.io/) (Free open-source), or a traditional photogrammetry program like [Metashape](https://www.agisoft.com/) or [Reality Capture](https://www.capturingreality.com/).

Note: When using COLMAP, it's worth highlighting the 3D Gaussian Raytracing "train.py" and Playgrounds toolsets are picky on the camera lens model used for the camera solve. At this time you cannot use the "SIMPLE_RADIAL" COLMAP camera model. This means you need to use undistorted datasets with a camera model like PINHOLE, SIMPLE_PINHOLE or OPENCV_FISHEYE.

### Examples

An example .hip file is provided help you get started with 3DGRUT workflows in Houdini:

#### /HoudiniProjects/TOPS_3DGRUT/
- TOPS_3DGRUT_Static_V001.hip


![Houdini Train](Images/tops_3dgrut_static_nodes.png)

This HIP file requires you to have launched Houdini/HQueue from inside a virtual environment session that has CUDA Toolkit, Python 3.11, and several other python packages pre-installed.

If you are using Miniconda, a new terminal session can be started up using:

    conda activate Kartaverse
    cd $HOME/3dgrut/
    houdini

### Parameter Customization

#### Attribute Create:

![Houdini Train](Images/tops_3dgrut_static_1_attribute_create.png)

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

#### Environment Edit:

![Houdini Train](Images/tops_3dgrut_static_2_env_vars.png)

The EnvironmentEdit node is used to customize the PYTHONHOME and PYTHONPATH environment variables. This helps redefine the Python version and site-packages used by 3dgrut.

    PYTHONHOME = `@MINICONDA_ENV`
    PYTHONPATH = `@MINICONDA_ENV`/lib/python3.11/site-packages

#### Generic Generator:

![Houdini Train](Images/tops_3dgrut_static_3_generator.png)

The GenericGenerator node runs the command-line job task. The variable we defined in the Attribute Create create node are referenced when building out the command-line flags that are passed to Python3 and the train.py script:

    "`@MINICONDA_ENV`/bin/python3" "`@WORKING_DIR`/`@SCRIPT_NAME`" --config-name "`@CONFIG_NAME`" path="`@SOURCE_DIR`" out_dir="`@OUTPUT_DIR`" experiment_name="`@EXPERIMENT_NAME`" `@PROXY_RESOLUTION`

### Running your first TOPs job

Click on the orange colored triangle button in the tasks toolbar to start cooking the houdini TOPs work item. This will being the batch rendering job. 

![Houdini Train](Images/tops_3dgrut_static_4_opcook.png)

The results of this opcook workflow can be seen in the node graph, and in the "Task Graph Table" panel. Double click on the Task Graph Table's "train_genericgenerator1" entry to display the cooking status.

![Houdini Train](Images/tops_3dgrut_static_4_taskgraph.png)

As your GPU fans spin up under load from the 3DGRUT training you can see the progress messages scroll by in the status window. The rendering process will take a while so be patient!

![Houdini Train](Images/tops_3dgrut_static_5_status.png)

![Houdini Train](Images/tops_3dgrut_static_5_complete.png)

When the training job is done you can close the status window. Take a moment to look at the TOPs node graph. If everything succeeded you should see green circles with checkmarks next to each of the nodes:

![Houdini Train](Images/tops_3dgrut_static_4_cooked_nodes.png)

You've now used Houdini TOPs to process your first dataset!
