
from itertools import starmap

GROUPINGS = ('theorie', 'exercice', 'pygame',
             'progra', 'gl', 'lecture', 'pdf',
             'projet', 'colorpicker', '')

EXTS = {
    '.pdf': 1,
    '.odp': 2,
    '.html': 3,
    '.css': 4,
    '.svg': 5,
    '.png': 6,
    '.jpg': 7,
    '.py': 8,
    '.php': 9,
    '.java': 10,
    '.js': 11,
}

def auto_lang_dict(basename, ext, sep=None):
    if sep is None:
        sep = '_' if ext == 'py' else '.'
    return {
        basename + '.' + ext: {
            lang: basename + sep + lang + '.' + ext
            for lang in ('fr', 'en')
        }
    }

def auto_lang_dict_list(*it):
    return list(starmap(auto_lang_dict, it))

TRANSLATION_LIST = [
    {'example_base_file.ext': {
        'fr': 'example_french_version.ext',
        'en': 'example_english_version.ext',
    }},
    
    {'projet.html': {
        'fr': 'projet.html',
        'en': 'projects.html',
    }},
    
    {'projet.html': {
        'fr': 'projet.html',
        'en': 'projects.html',
    }},
    
] + auto_lang_dict_list(
    ('theorie1_egal_if', 'py'),
    ('progra_equivalences', 'py'),
    ('progra_equivalences', 'html', '_'),
    
)
