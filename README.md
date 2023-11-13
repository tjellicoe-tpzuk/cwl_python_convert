# Resize Image By Specified Scale-Factor Using CWL
## This package provides a command line tool that takes an input image and generates a resized image based on user-defined scale-factor using common workflow language and python

## How to use this application
The cwl file for this package requires a Docker container to run the required Python file. The cwl files make a call to an image contained on Docker Hub (`tjellicoetpzuk/convert`) and so no additional building is reuqired. However, to build this Docker container locally run the command:
`docker build -t <your_image_name> .`
in the current repo directory. You will then need to update each of the cwl files to point to this local Docker container instead:
`dockerPull: <your_image_name>:latest`

The python script `convert_image` takes a function operator (currently only `resize`) a file reference and a size definition (`Nnn%`) and converts the chosen image by the specified scale factor.
The inputs to the cwl command are provided via the respective yaml files depending on the type of file to be converted:
`input.yml` to be used alongside `convert-png-app.cwl`
`input_stac.yml` to be used alongside `convert-stac-app.cwl`
`input_url.yml` to be used alongside `convert-url-app.cwl`
Each of the yaml files can be updated to specify the input parameters so desired.

Once complete, an output file will be created in the current directory containing the updated image.

