from torchvision.models.detection import fasterrcnn_mobilenet_v3_large_320_fpn
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

from ..config import NUM_CLASSES

def create_fasterrcnn_mobilenet_v3_large_320_fpn():
    model = fasterrcnn_mobilenet_v3_large_320_fpn(
        weights=None
    )

    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, NUM_CLASSES) 

    return model