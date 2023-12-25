## Example codes

Sample code to generate the embedding space and predict drug-disease associations are provided in [`run_demo.ipynb`](../run_demo.ipynb).

## Input File formats  输入文件格式

### Hierarchy file  层级结构文件

The input hierarchy file for semantic similarity calculation should be a `.csv` file with following information: 

语义相似度计算的输入层次文件应该是一个' .csv '文件，包含以下信息:
| child | parent  |
| ------- | --- |
| child1 | parent1 |
| parent1 | parent2 |
| parent2 | disease |
| ... | ... | 
| parent n | drug |
| ... | ... | 

_Caution:_ All leafs should be branched out from root named as either 'disease' or 'drug'

注意:所有叶子都应该从根部分支出来，命名为“疾病”或“药物”。

### Network file

The input network file should be a tab- or space-separated `.txt` file with following orders:

输入的网络文件应该是一个tab或空格分隔的' .txt '文件，顺序如下:

```python
source target weight edge_type edge_id
```

### Node type label file

The input node type label file for heterogeneous Skip-gram should be a '.tsv' file with following information:
异构Skip-gram的输入节点类型标签文件应该是包含以下信息的'.tsv'文件:

| node   | type    |
| ------ | ------- |
| node 1 | gene    |
| node 2 | disease |
| node 3 | gene    |
| ...    | ...     |
| node n | drug    |
| ...    | ...     |

_Caution:_ The drug, disease and gene node types should be given as `drug`, `disease`, `gene` for the model to properly recognize its type.

注意:药物、疾病和基因节点类型应以药物、疾病、基因标示，以便模型正确识别其类型。

### Positive/negative drug-disease association file 阳性/阴性药物-疾病关联文件

Positive/negative pair information for drug-disease association prediction task should be input as a `.tsv` file with following structure:
药物-疾病关联预测任务的正/负对信息应以'.Tsv '文件的形式输入，结构如下:

| drug  | disease  | label |
| ----- | -------- | ----- |
| drug1 | disease1 | 1     |
| drug2 | disease2 | 0     |
| ...   | ...      | ...   |

where `label == 1` refers to positive pairs and `label == 0` refers to negative pairs.

其中label == 1表示正对，label == 0表示负对。
