# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: EqualScalePolygon.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2019-04-12 23:29

EMAIL: tianyuningmou2009@126.com

VERSION: : #1 
CHANGED By: : tianyuningmou
MODIFIED: : @Time : 2019-04-12 23:29
"""


import math


class Point2D(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


def add(p1, p2):
    """

    :param p1: Point2D type
    :param p2: Point2D type
    :return:
    """
    return Point2D(p1.x + p2.x, p1.y + p2.y)


def sub(p1, p2):
    """

    :param p1: Point2D type
    :param p2: Point2D type
    :return:
    """
    return Point2D(p1.x - p2.x, p1.y - p2.y)


def multi_n(p1, n):
    """

    :param p1: Point2D type
    :param n: Point2D type
    :return:
    """
    return Point2D(p1.x * n, p1.y * n)


def multi(p1, p2):
    """

    :param p1: Point2D type
    :param p2: Point2D type
    :return:
    """
    return p1.x * p2.x + p1.y * p2.y


def expon(p1, p2):
    """

    :param p1: Point2D type
    :param p2: Point2D type
    :return:
    """
    return p1.x * p2.y - p1.y * p2.x


def compute_line(polygon, scale):
    """

    :param polygon: polygon
    :param scale: scale
    :return:
    """
    tem_polygon = []
    for index in range(len(polygon)):
        tem_polygon.append(sub(polygon[0 if index == len(polygon) - 1 else index + 1], polygon[index]))
    mid_polygon = []
    for index in range(len(tem_polygon)):
        mid_polygon.append(multi_n(tem_polygon[index], 1.0 / math.sqrt(multi(tem_polygon[index], tem_polygon[index]))))

    length = len(polygon)
    new_polygon = []
    for index in range(length):
        start_index = length - 1 if index == 0 else index - 1
        end_index = index
        sina = expon(mid_polygon[start_index], mid_polygon[end_index])
        lens = scale / sina
        vector = sub(mid_polygon[end_index], mid_polygon[start_index])
        point = add(polygon[index], multi_n(vector, lens))
        new_polygon.append(point)
    return new_polygon


def change_point(datas):
    """

    :param datas:
    :return:
    """
    polygon = []
    for data in datas:
        point = (float(data[0]), float(data[1]))
        polygon.append(point)
    return polygon


def equal_scale_polygon(polygon, scale):
    """

    :param polygon: polygon
    :param scale: scale
    :return:
    """
    if isinstance(polygon, str):
        polygon = [x.split(',') for x in polygon.split(';')]
    polygon = change_point(polygon)
    polygon = [Point2D(i[0], i[1]) for i in polygon]
    new_polygon = compute_line(polygon, scale)
    new_polygon = [(i.x, i.y) for i in new_polygon]
    return new_polygon
