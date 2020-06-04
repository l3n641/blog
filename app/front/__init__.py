from app.front.post import Post

def init(api):
    api.add_resource(Post,'/posts',endpoint="posts")