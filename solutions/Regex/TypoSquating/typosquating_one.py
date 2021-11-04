import re


def typosquats(companyDomains, newDomains):
    output = []
    new_words = {}
    for word in companyDomains:
        new_words[re.sub(r'\.\w+', '', word)] = True

    for new_domain in newDomains:

        if re.sub(r'\.\w+', '', new_domain) in new_words and new_domain not in companyDomains:
            output.append(new_domain)
