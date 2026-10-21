import json

# doc file json trung gian
intermediate = open("intermediate.json", "r", encoding="utf-8")
all_data = json.load(intermediate)
intermediate.close()

# lay data tu file json trung gian
nodes = all_data["nodes"]
ways = all_data["ways"]
ways_nodes = all_data["ways_nodes"]


# tao file sql
command = open("command.sql", "w", encoding="utf-8")

# tao bang nodes
command.write("""
create table nodes (
    ordinal serial primary key,
    nodeID bigint,
    nodeLAT numeric,
    nodeLON numeric,
    nodeNAME varchar,
    nodeAMENITY varchar
    );\n\n""")

for i in range(len(nodes)):
    nodeID = nodes[i]["id"]
    nodeLAT = nodes[i]["lat"]
    nodeLON = nodes[i]["lon"]
    nodeNAME = ""
    nodeAMENITY = ""

    namee = nodes[i]["tag"].get("name")
    if namee != None:
        nodeNAME = f"'{namee}'"
    else:
        nodeNAME = "NULL"
    amenityy = nodes[i]["tag"].get("amenity")
    if amenityy != None:
        nodeAMENITY = f"'{amenityy}'"
    else:
        nodeAMENITY = "NULL"

    command.write(f"insert into nodes (nodeID, nodeLAT, nodeLON, nodeNAME, nodeAMENITY) values ({nodeID}, {nodeLAT}, {nodeLON}, {nodeNAME}, {nodeAMENITY});\n")

# tao bang ways
command.write("""
create table ways (
    ordinal serial primary key,
    wayID bigint,
    typeWAY varchar,
    nameWAY varchar
    );\n\n""")

for i in range(len(ways)):
    wayID = ways[i]["id"]
    typeWAY = ""
    nameWAY = ""

    typee = ways[i]["tag"].get("highway")
    if typee != None:
        typeWAY = f"'{typee}'"
    else:
        typeWAY = "NULL"
    namee = ways[i]["tag"].get("name")
    if namee != None:
        nameWAY = f"'{namee}'"
    else:
        nameWAY = "NULL"
    command.write(f"insert into ways (wayID, typeWAY, nameWAY) values ({wayID}, {typeWAY}, {nameWAY});\n")


# tao bang ways_nodes
command.write("""
create table ways_nodes (
    ordinal serial primary key,
    wayID bigint,
    nodeID bigint,
    orderNODE int
    );\n\n""")

for i in range(len(ways_nodes)):
    wayID = ways_nodes[i]["way_id"]
    nodeID = ways_nodes[i]["node_id"]
    orderNODE = ways_nodes[i]["order"]
    command.write(f"insert into ways_nodes (wayID, nodeID, orderNODE) values ({wayID}, {nodeID}, {orderNODE});\n")