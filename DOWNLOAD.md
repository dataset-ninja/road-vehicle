Dataset **Road Vehicle** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/L/i/nO/9LRvNCtujc6BJZbE5MU6rMA6pK0g16fMw1nycyzvu8PJZbC3jM66Lh2bq2u7fIyA5LoXDhTGPARajPzV7Na1FlWm8ftCnvaqG8yLGBfUQSJ2PXmaNO70sEiTg9pD.tar)

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