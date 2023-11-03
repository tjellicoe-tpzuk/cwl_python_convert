cwlVersion: v1.0
class: CommandLineTool
id: convert
#baseCommand: ["python3", "-m", "convert_image"]
inputs:
  fn:
    type: string
    inputBinding:
      position: 1
  stac:
    type: Directory
    inputBinding:
      position: 2
      prefix: --stac
  size:
    type: string
    inputBinding:
      position: 3
outputs:
  results:
    type: Directory
    outputBinding:
      glob: .
requirements:
  DockerRequirement:
    dockerPull: tjellicoetpzuk/convert:latest
