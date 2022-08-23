""" array_fast.py : programmers `행렬과 연산` lv 4 score: 41.7 / 100"""


from collections import deque

def solution(rc, operations):

    for op in operations:
        if op == 'ShiftRow':
            rc = shift_row(rc)
        elif op == 'Rotate':
            rc = rotate(rc)
        else:
            rc = rc

    return rc


def rotate(mat):
    row = len(mat)
    col = len(mat[0])
    cols = list(zip(*mat))  # transposed matrix
    # topleft, topright, bottomleft, bottomright
    edge00 = edge01 = edge10 = edge11 = None

    edge00 = mat[1][0]
    edge01 = mat[0][-2]
    edge10 = mat[-1][1]
    edge11 = mat[-2][-1]


    row_top = deque(mat[0], maxlen=col)
    row_bottom = deque(mat[-1], maxlen=col)
    row_top.appendleft(edge00)
    row_bottom.append(edge11)

    col_left = deque(cols[0], maxlen=row)
    col_right = deque(cols[-1], maxlen=row)
    col_left.append(edge10)
    col_right.appendleft(edge01)
    cols[0] = col_left
    cols[-1] = col_right
    orig_mat = list(zip(*cols))
    orig_mat[0] = list(row_top)
    orig_mat[-1] = list(row_bottom)
    return list(orig_mat)


def shift_row(mat):
    q = deque(mat)
    q.rotate(1)
    return list(q)


arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
op = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]
op = ["Rotate"]
res = solution(arr, op)
print(arr)
print(res)
