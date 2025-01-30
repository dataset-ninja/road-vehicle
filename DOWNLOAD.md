Dataset **Road Vehicle** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEwMDZfUm9hZCBWZWhpY2xlL3JvYWQtdmVoaWNsZS1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJCSloyTE1FSU8wVG5pYjN2MDVvUnBxTFh6dXhJWjZMRkdpZVo0SVQzcTZzPSJ9)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Road Vehicle', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/ashfakyeafi/road-vehicle-images-dataset/download?datasetVersionNumber=1).