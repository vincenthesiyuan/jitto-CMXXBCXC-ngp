## jittor-草莓小熊不吃香菜-NGP



### Install

1. install the requirements

```shell
pip install -r requirements.txt
```

2. reset jnerf

```
cd python
python -m pip install -e .
```



------

### Test

Two test mode,

1. run test.py for all competition datatset at once, and it will generate result image to the folder **./result**. 

```python
python test.py
```



2. run train.py with **--config-file** and **--task test**, but it just test one set.

**Example:**

```python
python train.py --config-file ./projects/ngp/configs/ngp_scar.py --task test
```



------

### Train

**Example:**

```
python train.py --config-file ./projects/ngp/configs/ngp_scar.py
```

After training , the checkpoint file and validated images will be generated to the folder **./logs**.



------

### Dataset

All the comptetition dataset is at the folder **./data/nerf_synthetic**, and you can modify it at the config file for each dataset.

(A) dataset download: [here](https://cloud.tsinghua.edu.cn/f/63016014a4ad410997f5/?dl=1)

(B) more test dataset: [here](https://cloud.tsinghua.edu.cn/f/d998312699ca45068ab1/?dl=1)



------

### TODO

* add reflected radiance model like [Ref-NeRF](https://dorverbin.github.io/refnerf/), improving NGP's ability to represent and render the glossy surfaces.

* add [BARF](https://github.com/chenhsuanlin/bundle-adjusting-NeRF) based on jittor framework.



------

### Acknowledgements

The original implementation comes from the following project:

* [JNeRF](https://github.com/Jittor/JNeRF)

* [Instant-NGP](https://github.com/NVlabs/instant-ngp)

  

------

### Citation

```
@article{hu2020jittor,
  title={Jittor: a novel deep learning framework with meta-operators and unified graph execution},
  author={Hu, Shi-Min and Liang, Dun and Yang, Guo-Ye and Yang, Guo-Wei and Zhou, Wen-Yang},
  journal={Science China Information Sciences},
  volume={63},
  number={222103},
  pages={1--21},
  year={2020}
}
@article{mueller2022instant,
    author = {Thomas M\"uller and Alex Evans and Christoph Schied and Alexander Keller},
    title = {Instant Neural Graphics Primitives with a Multiresolution Hash Encoding},
    journal = {ACM Trans. Graph.},
    issue_date = {July 2022},
    volume = {41},
    number = {4},
    month = jul,
    year = {2022},
    pages = {102:1--102:15},
    articleno = {102},
    numpages = {15},
    url = {https://doi.org/10.1145/3528223.3530127},
    doi = {10.1145/3528223.3530127},
    publisher = {ACM},
    address = {New York, NY, USA},
}
@inproceedings{mildenhall2020nerf,
  title={NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis},
  author={Ben Mildenhall and Pratul P. Srinivasan and Matthew Tancik and Jonathan T. Barron and Ravi Ramamoorthi and Ren Ng},
  year={2020},
  booktitle={ECCV},
}
```

