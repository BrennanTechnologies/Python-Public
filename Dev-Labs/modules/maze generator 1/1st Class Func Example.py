import builtins


def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text


# h1_tag
print_h1 = html_tag('h1')
print_h1('Test Headline!')


print_h1('Another Headline!')

# h2_tag
print_h2 = html_tag('h2')
print_h2('_H2 Headline_')

# p_tag
print_p = html_tag('p')
print_p('Test Paragraph!')

print_h1('')

''.__getitem__(0)

print_h1('H1 Headline')
print_h2('H2 Headline')
print_p('Paragraph')
# print(print_h1('Test Headline!'))
# print(print_h1('Another Headline!'))
# print(print_p('Test Paragraph!'))
