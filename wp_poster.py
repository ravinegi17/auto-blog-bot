import requests
import os

WP_SITE = os.getenv("WP_SITE")
WP_USER = os.getenv("WP_USER")
WP_PASS = os.getenv("WP_PASS")

def get_jwt_token():
    r = requests.post(f"{WP_SITE}/wp-json/jwt-auth/v1/token", data={
        'username': WP_USER,
        'password': WP_PASS
    })
    return r.json()['token']

def upload_image(image_path, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Disposition": f"attachment; filename={os.path.basename(image_path)}"
    }
    with open(image_path, 'rb') as img:
        r = requests.post(f"{WP_SITE}/wp-json/wp/v2/media", headers=headers, files={"file": img})
    return r.json()['id']

def post_to_wordpress(blog, image_path):
    token = get_jwt_token()
    image_id = upload_image(image_path, token)

    data = {
        'title': blog['title'],
        'content': blog['html_body'],
        'status': 'publish',
        'excerpt': blog['meta_description'],
        'slug': blog['slug'],
        'featured_media': image_id
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    r = requests.post(f"{WP_SITE}/wp-json/wp/v2/posts", json=data, headers=headers)
    print("✅ Blog Posted:", r.json().get('link'))
