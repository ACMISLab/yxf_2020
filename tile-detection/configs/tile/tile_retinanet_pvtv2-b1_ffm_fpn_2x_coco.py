_base_ = './tile_retinanet_pvtv2-b1_fpn_2x_coco.py'
model = dict(
    type='RetinaNet',
    backbone=dict(
        type='PVTv2SFM',
        embed_dims=64,
        num_layers=[3, 4, 6, 3],
        init_cfg=dict(checkpoint='https://github.com/whai362/PVT/releases/download/v2/pvt_v2_b2.pth')
    ),
    neck=dict(in_channels=[64, 256, 320, 512]),

)

find_unused_parameters = True