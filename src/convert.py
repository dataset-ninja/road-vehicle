# https://www.kaggle.com/datasets/ashfakyeafi/road-vehicle-images-dataset

import os

import supervisely as sly
import yaml
from supervisely.io.fs import get_file_name
from tqdm import tqdm


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/Users/almaz/Downloads/trafic_data"
    batch_size = 30

    def _create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        ann_path = os.path.join(annotations_pathes, get_file_name(image_path) + ".txt")

        with open(ann_path) as f:
            content = f.read().split("\n")

        for curr_data in content:
            if len(curr_data) != 0:
                ann_data = list(map(float, curr_data.split(" ")))
                curr_obj_class = idx_to_obj_class[int(ann_data[0])]
                left = int((ann_data[1] - ann_data[3] / 2) * img_wight)
                right = int((ann_data[1] + ann_data[3] / 2) * img_wight)
                top = int((ann_data[2] - ann_data[4] / 2) * img_height)
                bottom = int((ann_data[2] + ann_data[4] / 2) * img_height)
                rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                label = sly.Label(rectangle, curr_obj_class)
                labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    yaml_path = os.path.join(dataset_path, "data_1.yaml")
    idx_to_obj_class = {}
    with open(yaml_path, "r") as stream:
        yaml_data = yaml.safe_load(stream)
        for idx, class_name in enumerate(yaml_data["names"]):
            idx_to_obj_class[idx] = obj_class = sly.ObjClass(class_name, sly.Rectangle)

    obj_class_collection = sly.ObjClassCollection(list(idx_to_obj_class.values()))

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_class_collection)
    api.project.update_meta(project.id, meta.to_json())

    data = os.listdir(dataset_path)
    for ds_name in data:
        curr_item_path = os.path.join(dataset_path, ds_name)
        if os.path.isdir(curr_item_path):
            dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)
            images_pathes = os.path.join(curr_item_path, "images")
            annotations_pathes = os.path.join(curr_item_path, "labels")
            images_names = os.listdir(images_pathes)

            progress = tqdm(total=len(images_names), desc="Create dataset {}".format(ds_name))

            for img_names_batch in sly.batched(images_names, batch_size=batch_size):
                images_pathes_batch = [
                    os.path.join(images_pathes, image_path) for image_path in img_names_batch
                ]

                anns_batch = [_create_ann(image_path) for image_path in images_pathes_batch]

                img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                api.annotation.upload_anns(img_ids, anns_batch)

                progress.update(len(img_names_batch))

    return project
