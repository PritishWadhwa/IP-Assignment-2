"""
CSE101: Introduction to Programming
Assignment 3

Name        : PRITISH WADHWA
Roll-no     : 2019440
"""

import math
import random


def dist(p1, p2):
    """
    Find the euclidean distance between two 2-D points 
    
    # Euclidean distance is defined as the distance between two points

    Args:
        p1: (p1_x, p1_y)
        p2: (p2_x, p2_y)

    Returns:
        Euclidean distance between p1 and p2
    """
    distance = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return distance
    pass


def sort_points_by_X(points):
    """
    Sort a list of points by their X coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        List of points sorted by X coordinate
    """
    points.sort()
    return points
    pass


def sort_points_by_Y(points):
    """
    Sort a list of points by their Y coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        List of points sorted by Y coordinate
    """
    points.sort(key=lambda points_y: points_y[1])
    return points
    pass


def naive_closest_pair(plane):
    """
    Find the closest pair of points in the plane using the brute
    force approach

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    size = len(plane)
    minimum_distance = math.inf
    required_data = []
    for i in range(size):
        for j in range(i + 1, size):
            if dist(plane[i], plane[j]) <= minimum_distance:
                minimum_distance = dist(plane[i], plane[j])
                required_data = [minimum_distance, plane[i], plane[j]]
    return required_data
    pass


def closest_pair_in_strip(points, d):
    """
    Find the closest pair of points in the given strip with a
    given upper bound. This function is called by
    efficient_closest_pair_routine

    Args:
        points: List of points in the strip of interest.
        d: Minimum distance already found found by
            efficient_closest_pair_routine

    Returns:
        Distance between closest pair of points and closest pair
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)] if
        distance between p1 and p2 is less than d. Otherwise
        return -1.
    """
    min_dis = math.inf
    points = sort_points_by_Y(points)
    points_size = len(points)
    for i in range(points_size):
        for j in range(i+1, points_size):
            if points[j][1] - points[i][1] < d:
                dis = dist(points[i], points[j])
                if dis <= min_dis:
                    min_dis = dis
                    p = [points[i], points[j]]
    if min_dis < d:
        return_statement = [min_dis, p[0], p[1]]
        return return_statement
    else:
        return -1


def efficient_closest_pair_routine(points):
    """
    This routine calls itself recursively to find the closest pair of
    points in the plane.

    Args:
        points: List of points sorted by X coordinate

    Returns:
        Distance between closest pair of points and closest pair
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    points_size = len(points)
    if points_size == 1:
        return [math.inf, points[0]]
    elif points_size == 2:
        return [dist(points[0], points[1]), points[0], points[1]]
    points1 = points[:(points_size//2)]
    points2 = points[(points_size//2):]
    d1 = efficient_closest_pair_routine(points1)
    d2 = efficient_closest_pair_routine(points2)
    if d1[0] < d2[0]:
        d = d1[0]
        required_points = d1[1:]
    else:
        d = d2[0]
        required_points = d2[1:]
    new_data = closest_pair_in_strip(points, d)
    if (new_data != -1) and (-1 < new_data[0] <= d):
        d = new_data[0]
        required_points[0] = new_data[1]
        required_points[1] = new_data[2]
    required_data = [d, required_points[0], required_points[1]]
    return required_data
    pass


def efficient_closest_pair(points):
    """
    Find the closest pair of points in the plane using the divide
    and conquer approach by calling efficient_closest_pair_routine.

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    points = sort_points_by_X(points)
    return efficient_closest_pair_routine(points)
    pass


def generate_plane(plane_size, num_pts):
    """
    Function to generate random points.

    Args:
        plane_size: Size of plane (X_max, Y_max)
        num_pts: Number of points to generate

    Returns:
        List of random points: [(p1_x, p1_y), (p2_x, p2_y), ...]
    """

    gen = random.sample(range(plane_size[0] * plane_size[1]), num_pts)
    random_points = [(i % plane_size[0] + 1, i // plane_size[1] + 1) for i in gen]

    return random_points


if __name__ == "__main__":
    # number of points to generate
    num_pts = 10
    # size of plane for generation of points
    plane_size = (10, 10)
    plane = generate_plane(plane_size, num_pts)
    print(plane)
    naive_closest_pair(plane)
    efficient_closest_pair(plane)
