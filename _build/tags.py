import random
import click
import build

@click.command()
@click.option('--posts_dir', default='.', help='Path to posts directory')
@click.option('--tags_dir', default='.', help='Path to output tags directory')
@click.option('--tags_file', default='.', help='Output tags file')
def tags(posts_dir, tags_dir, tags_file):
    with open(tags_file, 'w') as f:
        tags = build.tags(posts_dir)

        for tag in tags:
            f.write('{0}: {{}}\n'.format(tag))
        # colors = [c() for c in sorted(r, key=lambda k: random.random())]
        # color = '#%02X%02X%02X' % tuple(colors)
        # size = pow(len(items), .4)
        # style = 'style="background-color:{};font-size:{}em;"'.format(color, size)

        # tags.append('<a href="/tag/{}">'.format(tag))
        # tags.append('<span class="resizing-tag" {}>{}</span>'.format(style, tag))
        # tags.append('</a>')

    # with open(tags_file, 'w') as f:
    #     f.write(''.join(tags))


    # front matter for all files in tags/
    fm ='---\nlayout: by_tag\ntag: {0}\npermalink: /tag/{0}/\ntitle: {0}\nname: {0}\n---'

    for tag in tags:
        with open('{}/{}.md'.format(tags_dir, tag), 'w') as f:
            f.write(fm.format(tag))


if __name__ == '__main__':
    tags()
