#!/usr/bin/env cwltool

cwlVersion: v1.2

class: CommandLineTool
id: convert
    #baseCommand: ["python", "-m", "convert_image"]
inputs:
  fn:
    type: string
    inputBinding:
      position: 1
  file_name:
    type: File
    inputBinding:
      position: 2
      prefix: --file
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
    dockerPull: tjellicoetpzuk/convert_new:latest
