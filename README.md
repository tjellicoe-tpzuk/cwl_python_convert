This is a first test to incorporate a python script into a CWL call.

The python convert_image script takes a funciton operator (currently only 'resize') a file reference and a size definition ('Nnn%') and converts the chosen image by the specified scale factor.

Please update the .yml files to specify the input parameters.

To build the docker image run
docker build -t <image_name> .

and then update the .cwl files to pull your created docker image.
The application currently pulls the docker image from the tjellicoetpzuk/convert directory.

To run the CWL script run
cwltool <convert_XXX_app.cwl> <input_XXX.yml>
depending on the type of file you wish to adjust.
