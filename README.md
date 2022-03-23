# Graphomania

[**Graphomania**](https://en.wikipedia.org/wiki/Graphomania) (from Ancient Greek: γρᾰ́φειν,
*gráphein*, lit. 'to write'; and μᾰνῐ́ᾱ, *maníā*, lit. 'madness, frenzy') [...] *labels a morbid
mental condition which results in writing rambling and confused statements, often degenerating into
a meaningless succession of words or even nonsense then called
[graphorrhea](https://en.wikipedia.org/wiki/Graphorrhea).*

This is supposed to be a backend serving a Thesaurus REST API.

It is supposed to be used with provided frontend to create a tool enabling and emphasizing one's
inner *grafoman* (from Polish, lit. 'literary wannabe', 'prolific bad writer', 'talentless
hack').

### Features *(in order of priority)*

- [ ] `.dat` (thesaurus dictionary) parser module *+ tests*
- [ ] Flask (?) API server *+ tests*
- [ ] Basic frontend *+ tests?*
- [ ] Solve [inflection](https://en.wikipedia.org/wiki/Inflection) (i.e. convert word in any form to
its basic form so that lookup can be easily achieved)
- [ ] `.idx` (index file) parser module *+ tests* (multiple languages?)
- [ ] Pretty frontend (possibly separate repo)
- [ ] Analyze and classify data on how much a word is considered *'graphomaniacal'*

## Requirements

- Python 3.8.2

### Installing dictionaries

```shell
# Create folder for new dictionary, assuming current directory is project root.
$ mkdir -p ./dict/pl-dict

# Download an OpenOffice dictionary pack (see #Links for more details).
$ wget https://sourceforge.net/projects/aoo-extensions/files/806/4/pl-dict.oxt

# Check filetype, in this case Zip archive.
$ file pl-dict.oxt
pl-dict.oxt: Zip archive data, at least v2.0 to extract

# Extract it into `./dict` directory.
$ unzip pl-dict.oxt -d ./dict/pl-dict

# All done.
```

## Notes

### OpenOffice dictionary packs:

Come in `.oxt` extension, which is just a zip. *Graphomania*'s interest as of now lies only in
`.dat` and their corresponding index (`.idx`) files. For future features other dictionary files will
be more than helpful.

#### `.dat` - thesaurus dictionary file:

- First line: encoding (e.g. `ISO8859-2`),
- Followed by *entries*:
  - First line: word or phrase, followed by `|` character, ending with a positive number *G* of
  *meaning groups* (e.g. `abolicja|2`, in which case *G* is equal to 2)
  - *G* lines of *meaning groups* (e.g. `-|rezygnować|wyrzekać się|zrzekać się`).
    - Format: `-` character, then at least 1 meaning, each preceded by `|` character

Full example of an entry:
```
abolicja|2
-|dymisja|dymisjonowanie|odwołanie|unieważnienie|zdjęcie (pot.)|zniesienie|zwolnienie (pot.)
-|skasowanie|zniesienie
```

#### `.idx` - index containing byte offset for a word in a corresponding `.dat` file:

- First line: encoding (e.g. `ISO8859-2`),
- Second line: number of following *index* lines,
- Followed by: *index* lines in format: word or phrase, followed by `|` character, ending with a
positive number *B* indicating a byte offset from the beginning of corresponding `.dat` file (e.g.
`abiogeneza|3931`, in which case *B* is equal to 3931)

### Frontend

- Front end trzyma cache wyszukanych słów.
```
dict[psa] == None
  GET /api/psa => { keys: [pies, psa, psem, ...], meanings: [czworonog, najlepszy przyjaciel człowieka, sabaka] }
  dict[keys[0]] == dict[keys[1]] == ... == meanings
```

### Links

- https://extensions.openoffice.org/en/project/polish-dictionary-pack
- https://dobryslownik.pl
- https://hunspell.github.io
- https://github.com/hunspell/hunspell
- https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
- http://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html
- https://www.systutorials.com/docs/linux/man/4-hunspell/
- https://stackoverflow.com/questions/18852161/dic-line-format-definition
- https://typethinker.blogspot.com/2008/02/fun-with-aspell-word-lists.html
- http://aspell.net/man-html/
- https://wiki.documentfoundation.org/Development/Dictionaries
- https://synonim.net/synonim/wycieruch

## License

Graphomania is licensed under the GPL-3.0 license. For more information see: [LICENSE](/LICENSE).
