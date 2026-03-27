url = 'http://www.nostarch.com'

css = url.find("://")
scheme = url[0:css]

dot1 = url.find('.')
subdomain = url[css+3:dot1]
dot2 = url.find('.', dot1 +1)
tld = url[dot2 +1:]

domain = url[dot1+1:dot2]

print(domain)
