from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "date": date(2025, 7, 21),
        "author": "Indranil Halder",
        "title": "Hike in The Mountains",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A, accusamus ad adipisci alias atque dolor dolorum, enim error harum id ipsam labore molestias necessitatibus nisi odit quo, vel velit voluptatem.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A, accusamus ad adipisci alias atque dolor dolorum, enim error harum id ipsam labore molestias necessitatibus nisi odit quo, vel velit voluptatem.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A, accusamus ad adipisci alias atque dolor dolorum, enim error harum id ipsam labore molestias necessitatibus nisi odit quo, vel velit voluptatem.
        """,
    },
    {
        "slug": "sunset-by-the-lake",
        "image": "coding.jpg",
        "date": date(2025, 8, 14),
        "author": "Indranil Halder",
        "title": "Sunset by The Lake",
        "excerpt": "The calm waves of the lake reflected the fiery sky as the sun went down. It was a peaceful moment that turned into an unexpected adventure.",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deleniti deserunt dolores ex exercitationem explicabo incidunt iusto maiores minima natus nesciunt nihil officia optio placeat possimus provident quae, qui quidem ratione.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores at dolorem eaque, eius eligendi enim esse excepturi exercitationem expedita hic maiores molestiae nesciunt numquam perspiciatis, placeat quas quasi quidem sed.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab accusamus ad amet animi asperiores, atque beatae blanditiis consectetur cupiditate deserunt distinctio dolor dolores harum ipsum neque, possimus rem repudiandae voluptatibus.
        """,
    },
    {
        "slug": "night-under-the-stars",
        "image": "woods.jpg",
        "date": date(2025, 9, 3),
        "author": "Indranil Halder",
        "title": "Night Under The Stars",
        "excerpt": "Lying beneath a sky full of stars reminded me how vast the universe is. It was one of those nights that makes you feel both tiny and infinite.",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet, asperiores atque consequatur cum distinctio doloremque eveniet explicabo facere, inventore itaque nisi nobis omnis perspiciatis, quas quis recusandae sequi tempore voluptates.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequuntur ducimus harum illum iure maxime minima nihil, nisi officiis perspiciatis placeat quaerat quia quidem ratione reprehenderit, sequi sunt tempora temporibus voluptates.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur assumenda atque consequatur dolorem eos magnam officia quam quas quasi quisquam repellendus, repudiandae saepe sapiente sint sit ut veritatis voluptate voluptates.
        """,
    },
]


def get_date(post):
    return post["date"]


# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_details(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(
        request,
        "blog/post-detail.html",
        {
            "post": identified_post,
        },
    )
