treasure = {"clues": ["beach", "cave", "waterfall"],"locations": {"beach": {
            "items": ["compass", "shovel"], "hint": "dig here"}
            ,"cave": {"items": ["lantern", "gold coin"],
            "hint": "look behind rocks"} },
            "crew": ["First Mate", "Navigator"]}

treasure["crew"].append("Cook")
treasure["crew"].remove("Navigator")

treasure["locations"]["volcano"] = {"items": ["diamond", "lava boots"],
    "hint": "wear protection"}

treasure["clues"].append("volcano")

for location, data in treasure["locations"].items():
    if "gold coin" in data["items"]:
        print(f"Treasure! In {location}")

print("All Items by Location:")
for location, data in treasure["locations"].items():
    items = ", ".join(data["items"])
    print(f"{location}: {items}")