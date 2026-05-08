# =============================================================================
# PROBLEM 03 — Dict of Lists by Distance
# =============================================================================
# What: group points by distance from origin into close/medium/far
# Concept: grouping with computed keys, nested dicts, per-group stats
# Done when:
#   [ ] grouping correct for all three categories
#   [ ] centroid computed correctly per group
#   [ ] return nested dict with points count centroid per group
#   [ ] no d.append() anywhere — always d[key].append()
# Hint: define the full nested structure in comments before any code
# =============================================================================

import math


def group_by_distance(points):
      """
      Group points by distance from origin:
      close  = distance < 2.0
      medium = 2.0 <= distance < 5.0
      far    = distance >= 5.0

      Return dict:
      # key   = category string 'close' 'medium' 'far'
      # value = dict with keys:
      #           'points'   -> list of points
      #           'count'    -> int
      #           'centroid' -> (mean_x, mean_y, mean_z) or None if empty
      """
      # key   =
      # value = { 'points': [], 'count': 0, 'centroid': None }

      d = {
            "close":{
                  "points": [],
                  "count": 0,
                  "centroid": ()
                  },
            "medium":{
                  "points": [],
                  "count": 0,
                  "centroid": ()
                  }, 
            "far": {
                  "points": [],
                  "count": 0,
                  "centroid": ()
                  }
      }

### this creates bugs 

      # for point in points:
      #       if math.sqrt(point[0]**2 + point[1]**2 + point[2]**2) < 2.0:
      #             d["close"]["points"].append(point)
      #             d["close"]["count"] =  len(d["close"]["points"])

      #             sum_x = sum_y = sum_z = 0

      #             for pts in d["close"]["points"]:
                  
      #                   sum_x += pts[0]
      #                   sum_y += pts[1]
      #                   sum_z += pts[2]

      #                   cluster = (pts[0]/len(d["close"]["points"]),
      #                   sum_y/len(d["close"]["points"]) ,
      #                   sum_z/len(d["close"]["points"]) )
      #                   d["close"]["centroid"] = cluster


      #       if 2.0 <= math.sqrt(point[0]**2 + point[1]**2 + point[2]**2) < 5.0:
      #             d["medium"]["points"].append(point)
      #             d["medium"]["count"] =  len(d["medium"]["points"])  

      #             sum_x = sum_y = sum_z = 0

      #             for pts in d["close"]["points"]:
                  
      #                   sum_x += pts[0]
      #                   sum_y += pts[1]
      #                   sum_z += pts[2]

      #             cluster = (sum_x/len(d["medium"]["points"]),
      #             sum_y/len(d["medium"]["points"]) ,
      #             sum_z/len(d["medium"]["points"]) )
      #             d["medium"]["centroid"] = cluster

      #       if math.sqrt(point[0]**2 + point[1]**2 + point[2]**2) >= 5.0:
      #             d["far"]["points"].append(point)
      #             d["far"]["count"] =  len(d["far"]["points"]) 

      #             sum_x = sum_y = sum_z = 0

      #             for pts in d["close"]["points"]:
                  
      #                   sum_x += pts[0]
      #                   sum_y += pts[1]
      #                   sum_z += pts[2]

      #             cluster = (sum_x/len(d["far"]["points"]),
      #             sum_y/len(d["far"]["points"]) ,
      #             sum_z/len(d["far"]["points"]) )
      #             d["far"]["centroid"] = cluster
      

      # print(d)
      # return d 


     # =====================================================
     # PASS 1 — GROUP POINTS
     # =====================================================

      for point in points:

            x, y, z = point

            distance = math.sqrt(x*x + y*y + z*z)

            if distance < 2.0:
                  d["close"]["points"].append(point)

            elif distance < 5.0:
                  d["medium"]["points"].append(point)

            else:
                  d["far"]["points"].append(point)

      # =====================================================
      # PASS 2 — COUNT + CENTROID
      # =====================================================

      for category in d:

            pts = d[category]["points"]

            # count
            d[category]["count"] = len(pts)

            # centroid
            if len(pts) > 0:

                  sum_x = 0
                  sum_y = 0
                  sum_z = 0

                  for point in pts:
                        sum_x += point[0]
                        sum_y += point[1]
                        sum_z += point[2]

                  centroid = (
                  sum_x / len(pts),
                  sum_y / len(pts),
                  sum_z / len(pts)
                  )

                  d[category]["centroid"] = centroid

      return d



# -----------------------------------------------------------------------------
if __name__ == "__main__":
    pts = [
        (0.5, 0.5, 0.5),
        (1.0, 0.0, 0.0),
        (3.0, 0.0, 0.0),
        (4.0, 0.0, 0.0),
        (6.0, 0.0, 0.0),
        (8.0, 0.0, 0.0),
        (0.0, 0.0, 1.5),
    ]

    result = group_by_distance(pts)

    print("PASS — returns dict" if isinstance(result, dict)
          else "FAIL — not a dict")
    print("PASS — has 3 keys"   if set(result.keys()) == {"close","medium","far"}
          else f"FAIL — keys: {result.keys()}")

    close = result.get("close", {})
    print("PASS — close count"  if close.get("count") == 3
          else f"FAIL — close count {close.get('count')}")

    far = result.get("far", {})
    print("PASS — far count"    if far.get("count") == 2
          else f"FAIL — far count {far.get('count')}")

    medium = result.get("medium", {})
    print("PASS — medium count" if medium.get("count") == 2
          else f"FAIL — medium count {medium.get('count')}")

    if close.get("centroid") is not None:
        cx = close["centroid"][0]
        print("PASS — centroid is tuple" if isinstance(close["centroid"], tuple)
              else "FAIL — centroid not tuple")
    else:
        print("FAIL — centroid is None for non-empty group")
