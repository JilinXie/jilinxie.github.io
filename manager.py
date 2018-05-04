import os
import markdown2
from jinja2 import Template


def generate_index():
    with open('index.template', 'r') as f:
        template = Template(f.read())
    posts = os.walk('posts').next()[-1]
    posts = [{'url': 'posts/%s' % (x.rsplit('.', 1)[0] + '.html'),
              'title': x.rsplit('.', 1)[0]}
             for x in posts]
    index = template.render(posts=posts)
    with open('index.html', 'w') as f:
        f.write(index)


def generate_post():
    files = [x for x in os.walk('_posts').next()[-1] if x.endswith('md')]
    with open('post.template', 'r') as f:
        template = Template(f.read())
    for fn in files:
        fp = os.path.join('_posts', fn)
        with open(fp, 'r') as f:
            post = markdown2.markdown(f.read())
            post = template.render(post=post)
        fp = os.path.join('posts', fn.rsplit('.', 1)[0]+'.html')
        with open(fp, 'w') as f:
            f.write(post)


if __name__ == '__main__':
    generate_post()
    generate_index()
