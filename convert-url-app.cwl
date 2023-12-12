cwlVersion: v1.2


class: CommandLineTool
id: convert
inputs:
  fn:
    type: string
    inputBinding:
      position: 1
  url:
    type: string
    inputBinding:
      position: 2
      prefix: --url
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
  NetworkAccess:
    networkAccess: true
