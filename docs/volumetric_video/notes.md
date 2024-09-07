# Videogrammetry Notes

Draft Section: This content will be error checked and re-formatted with detailed step-by-step screenshots and instructions.

## Reality Capture Batch Process

Batch processes a set of camera rig views using Reality Capture's command line interface.

Launch Reality Capture and create new project file

Variable: \`@rcCommand1\`  
 Command: \`@rctool\` \-addFolder \`@frameInputFolder\` \-align \-setReconstructionRegion \`@rcboxFile\` \-mvs \-simplify \`@polygonSimplify\` \-save \`@rcProjectAlignFile\` \-quit 

## Launch Reality Capture and create a new XYZ mesh output

Variable: \`@rcCommand2\`  
Command: \`@rctool\` \-load \`@rcProjectAlignFile\` \-calculateTexture \-exportModel "Model 2" \`@xyzMeshFile\` \`@xyzMeshPrefFile\` \-save \`@rcProjectXYZFile\` \-quit

## Launch Reality Capture and create a new OBJ mesh output

Variable: \`@rcCommand3\`  
Command: \`@rctool\` \-load \`@rcProjectXYZFile\` \-calculateTexture \-exportModel "Model 2" \`@objMeshFile\` \`@objMeshPrefFile\` \-save \`@rcProjectOBJFile\` \-quit

## Houdini TOPs Variables:

### RealityCapture.exe Program

Variable: \`@rctool\`  
Value: C:\\Program Files\\Capturing Reality\\RealityCapture\\RealityCapture.exe

### RealityCapture temporary folder

Variable: \`@cacheFolder\`  
Value: %TEMP%\\RealityCapture\\

### Input folder for image sequence data

Variable: \`@inputFolder\`  
Value: $HIP/images/

### Align Views project file

Variable: \`@rcProjectAlignFile\`  
Value: $HIP/images/\#\#\#\#/project\_align.rcproj

### Export final OBJ mesh project file

Variable: \`@rcProjectOBJFile\`  
Value: $HIP/images/\#\#\#\#/project\_obj.rcproj

### Export intermediate XYZ point cloud project file

Variable: \`@rcProjectXYZFile\`  
Value: $HIP/images/\#\#\#\#/project\_xyz.rcproj

### Frame specific Reality Capture XYZ point cloud output

Variable: \`@xyzMeshFile\`  
Value: $HIP/images/\#\#\#\#/mesh.xyz

### Frame specific Reality Capture OBJ mesh output

Variable: \`@objMeshFile\`  
Value: $HIP/images/\#\#\#\#/mesh.obj

### Frame specific .rcbox reconstruction region file

Variable: \`@rcboxFile\`  
Value: $HIP/images/\#\#\#\#/metadata/rec\_region.rcbox

### Frame specific preference file that is used when XYZ point clouds are exported

Variable: \`@xyzMeshPrefFile\`  
Value: $HIP/images/\#\#\#\#/metadata/xyz\_model\_export\_params.xml

### Frame specific preference file that is used when OBJ meshes are exported

Variable: \`@objMeshPrefFile\`  
Value: $HIP/images/\#\#\#\#/metadata/obj\_model\_export\_params.xml

### The default mesh reduction (polygon simplification) value is 5 million polygons.

Variable: \`@polygonSimplify\`  
Value: 5000000
