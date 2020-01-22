## Face detection experiments

Here is a table representing experiments and its results

|  config | Backbone | Pretrained | FPN | Loss | Iterations | mAP@0.5 | Optimizer | Augmentation | Batch size | Resolution |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  config-001 | ssd_mobilenet_v2 0.25 | No | No | Hard negative mining | 122400 | 0.558 | Adam | horizontal flip, random crop | 24 | 128x128 |
|  config-002 | ssd_mobilenet_v2 0.5 | No | No | Focal loss | 90450 | 0.725 | RMS Prop | horizontal flip | 24 | 128x128 |
|  config-003 | ssd_mobilenet_v2_fpn | No | Yes | Focal loss | 131700 | 0.6512 | RMS Prop | horizontal flip | 24 | 128x128 |
|  config-004 | ssd_mobilenet_v2 | Yes | No | Focal loss | 125000 | 0.7729 | RMS Prop | horizontal flip | 24 | 128x128 |
|  config-005 | ssd_mobilenet_v2 | Yes | No | Focal loss | 290500 | **0.7756** | SGD + momentum | horizontal flip | 24 | 128x128 |
