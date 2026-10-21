import xml.etree.ElementTree as ET
import json

# doc file
tree = ET.parse("map.osm")
root = tree.getroot()

# doc cac node
nodes = []
for node in root.findall("node"):
    node_id = int(node.get("id"))
    lat = float(node.get("lat"))
    lon = float(node.get("lon"))

    node_tag = {}
    for tag in node.findall("tag"):
        key = tag.get("k")
        value = tag.get("v")
        node_tag[key] = value
    nodes.append({
        "id": node_id,
        "lat": lat,
        "lon": lon,
        "tag": node_tag
    })


#doc cac duong
ways = []
ways_nodes = []
for way in root.findall("way"):
    way_id = int(way.get("id"))

    order = 1
    for tag in way.findall("nd"):
       node_ref = tag.get("ref")
       ways_nodes.append({
           "way_id": way_id,
           "node_id": node_ref,
           "order": order
       })
       order += 1

    way_tag = {}
    for tag in way.findall("tag"):
        key = tag.get("k")
        value = tag.get("v")
        way_tag[key] = value

    ways.append({
        "id": way_id,
        "tag": way_tag
    })


#chuyen cac object sang json
all_data = {
    "nodes": nodes,
    "ways": ways,
    "ways_nodes": ways_nodes
}
intermediate = open("intermediate.json", "w", encoding="utf-8")
json.dump(all_data, intermediate, indent=2)
intermediate.close()