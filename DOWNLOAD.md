Dataset **Road Vehicle** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/Y/4/l3/yA5j13QxZXW5V16N8DUi3Rml4QIIBXMpA8tRtojPxw0HmzTJpv8pnppmASLkVAZPQpDMCy2L5opBxoAhsnwjwDPMkpG5ZSNTi81OqcIL5yAnSiPUbse4hu7Q3PVv.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Road Vehicle', dst_path='~/dtools/datasets/Road Vehicle.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/ashfakyeafi/road-vehicle-images-dataset/download?datasetVersionNumber=1)