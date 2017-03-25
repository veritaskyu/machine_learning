
## 퍼셉트론

# 퍼셉트론은 다수의 입력을 통해 하나의 신호를 출력한다.
# 퍼셉트론 신호는 1, 0 두 가지 값을 가질 수 있다.
# 입력이 뉴런에 보내질 때는 각각 고유한 가중치가 곱해진다.
# 신호의 총합이 정해진 한계를 넘어설 때만 1을 출력한다.
# 가중치가 클수록 해당 신호가 그만큼 더 중요함을 뜻한다.

# 논리 게이트 구현
import numpy as np


def and_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def nand_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def xor_gate(x1, x2):
    s1 = nand_gate(x1, x2)
    s2 = or_gate(x1, x2)
    y = and_gate(s1, s2)
    return y

