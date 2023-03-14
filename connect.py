import json
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="restaurant",
    user="postgres",
    password="Nirajan#0321"
)

# Open a cursor
cur = conn.cursor()
# cur.execute("ALTER SEQUENCE res_restaurant_id_seq RESTART WITH 1")
# cur.execute("ALTER SEQUENCE res_image_id_seq RESTART WITH 1")
# cur.execute("ALTER SEQUENCE res_cuisine_id_seq RESTART WITH 1")
# cur.execute("ALTER SEQUENCE res_restaurant_cuisine_id_seq RESTART WITH 1")
# cur.execute("ALTER SEQUENCE res_restaurant_rating_id_seq RESTART WITH 1")
# if conn:
#     print("Connection successful!")

# Read the JSON file
with open("C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/final data/test_sql.json",encoding="utf-8") as f:
    data = json.load(f)

# Loop through each restaurant in the data dictionary
for restaurant in data:
    # Insert a new row into the restaurants table
    cur.execute(
        "INSERT INTO res_restaurant (name, location, average_rating, number_of_reviews) VALUES (%s, %s, %s, %s) RETURNING id",
        (restaurant["name"], restaurant["location"], restaurant["average_rating"], restaurant["number_of_reviews"])
    )
    restaurant_id = cur.fetchone()[0]

    # Loop through each image URL and insert a new row into the images table
    for image_url in restaurant["image_url"]:
        cur.execute(
            "INSERT INTO res_image (url, restaurant_id) VALUES (%s, %s)",
            (image_url, restaurant_id)
        )

    # Loop through each cuisine and insert a new row into the cuisines and restaurant_cuisines tables
    for cuisine in restaurant["cuisine"]:
        cur.execute(
            "SELECT id FROM res_cuisine WHERE name = %s",
            (cuisine,)
        )
        cuisine_row = cur.fetchone()
        if cuisine_row:
            cuisine_id = cuisine_row[0]
        else:
            cur.execute(
                "INSERT INTO res_cuisine (name) VALUES (%s) RETURNING id",
                (cuisine,)
            )
            cuisine_id = cur.fetchone()[0]
        cur.execute(
            "INSERT INTO res_restaurant_cuisine (restaurant_id, cuisine_id) VALUES (%s, %s)",
            (restaurant_id, cuisine_id)
        )

    # Loop through each rating and insert a new row into the restaurant_ratings table
    for user_id, rating_data in restaurant["rating"].items():
        cur.execute(
            "INSERT INTO res_restaurant_rating (restaurant_id, user_id, rating, comment) VALUES (%s, %s, %s, %s)",
            (restaurant_id, user_id, rating_data["rated"][0], rating_data["comment"])
        )

# Commit the changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()
