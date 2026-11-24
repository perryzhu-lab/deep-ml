
## **学习计划**

以下月份按开始学习的时间安排。**加粗的是必须学习的小单元**，普通文字标注为选学。

### **第一阶段：经典机器学习**

2026 年 11 月—2027 年 1 月，共 3 个月

#### **2026 年 11 月：数学与线性回归**

**重点：建立数学和机器学习基础**

1. **向量与矩阵**（Vectors and Matrices）

2. **线性回归**（Linear Regression）

3. **数据、数据集划分与基线模型**（Data, Splits and Baselines）

4. **回归评估指标**（Regression Metrics）

**月末目标：** 能用 NumPy 独立实现线性回归，并正确划分训练集、验证集和测试集。

#### **2026 年 12 月：模型训练与评估**

1. **正则化与泛化**（Regularization and Generalization）
2. **逻辑回归**（Logistic Regression）
3. **分类评估指标**（Classification Metrics）
4. **假设检验与实验**（Hypothesis Testing and Experiments）

选学：线性回归的统计学解释（Linear Regression as Statistics）。

重点理解过拟合、L1/L2 正则化、交叉熵、Precision、Recall、F1、ROC-AUC，以及如何合理比较两个模型的实验结果。

**月末目标：** 独立完成一个分类任务，分析模型是否过拟合，并解释评估指标。

#### **2027 年 1 月：数据表示与无监督学习**

1. **信息论**（Information Theory）
2. **生成式分类器与最近邻方法**（Generative Classifiers and Nearest Neighbours）
3. **主成分分析与降维**（PCA and Dimensionality Reduction）
4. **聚类与混合模型**（Clustering and Mixture Models）

选学：决策树、集成学习与提升算法。

这一阶段尤其需要理解向量距离、特征相似性、PCA、K-Means 和高斯混合模型。它们对于理解图像特征匹配和特征空间很有帮助。

**月末目标：** 能解释 PCA 的数学原理，独立实现 KNN、K-Means 等基础算法。

### **第二阶段：深度学习**

2027 年 2—5 月，共 4 个月，是全年最重要的阶段

#### **2027 年 2 月：神经网络基础**

1. **神经元、激活函数与反向传播**（Neurons, Activations and Backprop）
2. **多层感知机训练**（Training an MLP）
3. **PyTorch**
4. **优化器与学习率调度**（Optimizers and Schedules）

重点放在计算图、链式法则、梯度下降、SGD、Momentum、Adam 与学习率调度上。

**月末目标：** 不依赖高级训练框架，用 PyTorch 编写完整的 MLP 训练循环，并能够解释 `loss.backward()` 和 `optimizer.step()` 背后发生了什么。

#### **2027 年 3 月：深度学习训练机制**

1. **归一化层**（Normalization Layers）
2. **深度神经网络的正则化与损失函数**（Regularization and Losses for Deep Nets）
3. **模型训练机制**（Training Mechanics）
4. **卷积神经网络与计算机视觉**（Convolutional Networks and Computer Vision，开始学习）

重点理解 BatchNorm、LayerNorm、Dropout、梯度累积、混合精度训练及 CNN 基础。

**月末目标：** 能自己搭建 CNN 模型并训练，理解训练中常见的数值稳定性问题。

#### **2027 年 4 月：计算机视觉与 Transformer**

1. **卷积神经网络与计算机视觉**（继续完成）
2. **注意力机制**（Attention）
3. **Transformer 模块**（The Transformer Block）

这一个月不追求学习数量，建议至少拿出两周深入研究 Attention。

重点理解 Q、K、V、Scaled Dot-Product Attention、Multi-Head Attention、位置编码以及 Transformer Block 结构。

**月末目标：** 使用 PyTorch 独立实现一个 Multi-Head Attention 模块，并能讲清楚它的输入输出形状、计算过程和梯度传递。

#### **2027 年 5 月：生成式网络与视觉项目**

1\. **自编码器、GAN 与对比学习**（Autoencoders, GANs and Contrastive Learning）

选学：知识蒸馏与模型剪枝（Distillation and Pruning）。

这个月故意只设置一个主要小单元，其余时间用于复习 2—4 月的深度学习内容，重点深入对比学习、特征表征以及 CNN/Attention 的实际使用。

**月末目标：** 结合 CRFT_B5 的图像匹配任务，选择一个模块，独立梳理其特征表示、损失计算和反向传播过程，并做一次小型消融实验。

### **第三阶段：大语言模型**

2027 年 6—7 月，共 2 个月

#### **2027 年 6 月：语言模型基础**

1. **分词与词元化**（Tokenization）
2. **词元嵌入与下一词元预测数据**（Token Embeddings and Next-Token Data）
3. **早期语言模型**（First Language Models）
4. **构建 GPT 并进行解码**（Build a GPT and Decode From It）

重点理解 Tokenizer、Embedding、Causal Mask、Autoregressive Generation 和 GPT 的训练方式。

**月末目标：** 跟随网站项目实现一个 Tiny GPT，能够完成简单的文本生成。

#### **2027 年 7 月：现代 LLM 技术**

1. **位置编码、长上下文、高效注意力与 Mamba**（Positions, Long Context, Efficient Attention and Mamba）
2. **监督微调与参数高效微调**（Supervised Fine-Tuning and PEFT）
3. **大语言模型评估**（Evaluating LLMs）
4. **嵌入模型、检索与 RAG**（Embedding Models, Retrieval and RAG）

选学：专家混合模型（MoE）与大规模预训练。

重点掌握 RoPE、LoRA、基本的模型评估和 RAG 工作流程。Mamba 和高级长上下文算法可以只了解思路。

**月末目标：** 理解一个大语言模型从预训练、微调到推理的完整过程，并完成一个小型 RAG 或 LoRA 实验。

### **第四阶段：生成模型与 GPU 工程**

2027 年 8—10 月，共 3 个月

#### **2027 年 8 月：扩散模型**

1\. **扩散模型：从 DDPM 到流匹配**（Diffusion: from DDPM to Flow Matching）

选学：图神经网络（Graph Neural Networks）。

本月以扩散模型为主，重点理解前向加噪、反向去噪、噪声预测网络以及 DDPM 的训练目标。流匹配先掌握基本思想即可。

**月末目标：** 能够解释扩散模型的完整流程，运行一个简单的扩散模型实验。

#### **2027 年 9 月：GPU 与计算性能**

1. **CUDA 编程**（CUDA）
2. **延迟、吞吐量与 Roofline 性能模型**（Latency, Throughput and the Roofline）
3. **模型量化**（Quantization）

选学：Triton 编程。

重点理解 CUDA Thread、Block、Grid、GPU 内存层次、计算瓶颈和 FP32/FP16/BF16 的区别。

**月末目标：** 能编写一个基础 CUDA Kernel，并尝试分析 PyTorch 模型中某个算子的性能瓶颈。

#### **2027 年 10 月：推理优化与全年复习**

1\. **KV 缓存、分页、批处理与前缀缓存**（KV Cache, Paging, Batching and Prefix Caching）

选学：推测解码（Speculative Decoding）、并行计算与推理服务解耦（Parallelism and Disaggregation）。

这一个月建议只用前两周学习推理工程，其余时间专门用于全年知识回顾和补漏。

**月末目标：** 整理一份自己的机器学习知识体系，重新实现几个重点算法，并回顾全年项目。

## **两小时分配**

每周学习六天，周日休息或自由安排。

**每日时间安排**

周一至周五周六复习

学习新知识

70 分钟

直觉题、数学推导、核心概念

复习旧知识

30 分钟

回忆昨天、3 天前、7 天前的内容

代码与笔记

20 分钟

独立实现、整理易错点和公式

每周预计投入

## **12 小时**

每个月最后 2—3 个学习日，用来复习当月内容、重做错题，而不是继续学习新知识。

建议采用 **1-3-7-30 复习法**：一个概念学完后，分别在第 1、3、7、30 天尝试不看笔记主动回忆。对于数学公式，先尝试自己推导；对于编程题，先尝试自己写代码。

## **可以推迟的小单元？**


| 大单元     | 暂时推迟的小单元                                                                  |
| ------- | ------------------------------------------------------------------------- |
| 经典机器学习  | 贝叶斯推断、生存分析、高斯推断、决策树、集成学习与提升算法、支持向量机与核方法、超越线性模型、异常检测、传统文本检索与排序、时间序列与金融机器学习 |
| 深度学习    | tinygrad 与 JAX、循环神经网络与序列建模                                                |
| 大语言模型   | 偏好对齐、LLM 强化学习、模型可解释性、持续学习                                                 |
| 强化学习    | 9 个小单元整体延后，之后按照网站顺序学习                                                     |
| 推理工程    | 推测解码、并行计算与推理服务解耦                                                          |
| 机器学习编译器 | 张量编译器                                                                     |
| AI 安全   | AI 安全与治理（可以抽时间了解基础概念）                                                     |

另外，部分选学内容，例如图神经网络、MoE、知识蒸馏、Triton，可以根据每个月的完成情况决定是否学习。**核心内容没学透时，优先复习，不必为了追求进度增加新内容。**

## **全年的阶段检查**

1. 2027 年 1 月

   **机器学习基础**

   能够实现回归、分类、KNN、PCA，并正确评估模型
2. 2027 年 5 月

   **深度学习核心**

   能够独立训练 CNN，理解反向传播和 Transformer
3. 2027 年 7 月

   **语言模型基础**

   实现 Tiny GPT，理解 LoRA 和 RAG
4. 2027 年 10 月

   **工程与知识整合**

   掌握基础 GPU 编程，并能分析深度学习模型的训练与推理过程

