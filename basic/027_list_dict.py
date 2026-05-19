brands = [
    {
        "name":"dell",
        "country":"usa",
        "sells":[
            {"name":"china", "hq":"bejing"},
            {"name":"india", "hq":"delhi"},
        ]
    },
    {
        "name":"hp",
        "country":"usa",
        "sells":[
            {"name":"uae", "hq":"dubai"},
        ]
    },
    {
        "name":"apple",
        "country":"usa",
        "sells":[
            {"name":"japan", "hq":"tokiyo"},
            {"name":"germany", "hq":"berlin"},
        ]
    },
]

# task 1 print dubai
print(brands[1]["sells"][0]["hq"])

# task 2 print apple
print(brands[2]["name"])

# task 3 print germany
print(brands[2]["sells"][1]["name"])

# task 4 print india
print(brands[0]["sells"][1]["name"])





