# Example HIP Files

Kartaverse for Houdini ships with a [collection of example .hip files](https://github.com/Kartaverse/Kartaverse-for-Houdini/tree/master/HoudiniProjects) you can use to learn data node workflows. The sample projects cover XR industry focused concepts that will help you prepare content for use in virtual production, XR, VR, and fulldome projects.

As always, more learning content is on the way! If you have something specific in mind for what you'd like to see for examples, feel free to [send me your requests](mailto:andrew@andrewhazelden.com) and I can likely accommodate what you need in short order.

## GitHub Repo Hosted Examples:

### /HoudiniProjects/TOPS_FusionStudio/
- TOPS_FusionStudio_Fusion_Render_Node_V001.hip

### /HoudiniProjects/TOPS_Panotools/
- TOPs_FFmpeg_Movies_to_Frameset_Images_V001.hip
- TOPs_PTS_to_Frameset_Folders_V001.hip
- TOPS_PTS_Batch_Stitcher_Single_Frame_V001.hip

### /HoudiniProjects/TOPS_RealityCapture/
- TOPs_XMP_Sequence_to_Frameset_XMP_V001.hip
- TOPs_FFmpeg_Movies_to_Frameset_Images_V001.hip
- TOPs_Frameset_Images_to_Image_Sequence_V001.hip
- TOPs_Frameset_Meshes_to_OBJ_Mesh_Sequence_V001.hip
- TOPs_OBJ_Mesh_Sequence_to_ZIP_Archive_V001.hip
- TOPs_RealityCapture_Align_Views_V001.hip
- TOPs_RealityCapture_XYZ_Output_V001.hip
- TOPs_RealityCapture_OBJ_Output_V001.hip

### Reality Capture Order of Operations

The Reality Capture workflow expects the "Align Views" task to happen first, followed by the "XYZ Output", and then finally the "OBJ Output". 

If you want to drop the "XYZ Output stage", simply edit the "OBJ Output" TOPS network and change the "rc_command node" to point to a different Realty Capture checkpoint project file on this part of the expression:``` -load `@rcProjectXYZFile` ```. You would change that entry to specify ``` -load  `@rcProjectAlignFile` ``` instead.

