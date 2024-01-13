def union(objectA, objectB):
    print(objectA, objectB)
    intersects = set()
    for x1, y1, z1, r1 in objectA:
        for x2, y2, z2, r2 in objectB:
            if ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5 <= r1+r2:  # they intersect
                intersects.update([(x1, y1, z1, r1), (x2, y2, z2, r2)])
    to_remove = set()
    for x1, y1, z1, r1 in intersects:
        for x2, y2, z2, r2 in intersects:
            if (x1, y1, z1, r1) != (x2, y2, z2, r2):  # not the same sphere
                if ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5 + r1 <= r2:  # inside
                    to_remove.add((x1, y1, z1, r1))

    for obj in to_remove:
        intersects.remove(obj)

    return intersects
