import math
from collections import Counter


# 计算熵，用于衡量一个数据集中类别的不确定性或混乱程度
def calculate_entropy(labels: list) -> float:
    counts = Counter(labels)
    entropy = 0
    total = len(labels)
    for i in counts.values():
        p = i / total
        entropy -= p * math.log2(p)
    return entropy


# 计算信息增益
def calculate_information_gain(
    examples: list[dict], attr: str, target_attr: str
) -> float:
    # 提取标签
    labels = [example[target_attr] for example in examples]
    # 计算初始熵
    H_before = calculate_entropy(labels=labels)
    # 提取当前属性的取值
    values = set(example[attr] for example in examples)
    values = sorted(values)
    # 按照属性划分数据集
    H_after = 0
    for value in values:
        sub_set = [example for example in examples if example[attr] == value]
        weight = len(sub_set) / len(examples)
        sub_labels = [example[target_attr] for example in sub_set]
        sub_entropy = calculate_entropy(sub_labels)
        H_after += weight * sub_entropy
    return H_before - H_after


def majority_class(examples: list[dict], target_attr: str) -> str:
    labels = [example[target_attr] for example in examples]
    counts = Counter(labels)
    max_count = max(counts.values())
    results = [label for label in counts if counts[label] == max_count]
    return min(results)


def learn_decision_tree(
    examples: list[dict], attributes: list[str], target_attr: str
) -> dict:
    # 判断是否停止划分
    labels = [example[target_attr] for example in examples]
    if len(set(labels)) == 1:
        return labels[0]
    if attributes == []:
        return majority_class(examples, target_attr)

    # 选择最佳划分属性
    best_attr = None
    best_gain = float("-inf")
    for attr in attributes:
        gain = calculate_information_gain(examples, attr, target_attr)
        if gain > best_gain:
            best_gain = gain
            best_attr = attr

    # 构造决策树节点
    tree = {best_attr: {}}

    # 按照属性划分数据
    values = sorted(set(example[best_attr] for example in examples))
    for value in values:
        sub_set = [example for example in examples if example[best_attr] == value]

        # 递归构建子树
        # 去除已使用的属性
        remaining_attributes = [attr for attr in attributes if attr != best_attr]
        sub_tree = learn_decision_tree(sub_set, remaining_attributes, target_attr)

        tree[best_attr][value] = sub_tree

    return tree
