# Graphomania

This is supposed to be a backend serving a Thesaurus REST API.

It is supposed to be used with provided frontend to create a tool enabling and emphasizing one's
inner graphomaniac (pol. "grafoman" - *"literary wannabe", "prolific bad writer", "talentless
hack"*).

### Features *(in order of priority)*

- [ ] `.dat` (thesaurus dictionary) parser module *+ tests*
- [ ] Flask (?) API server *+ tests*
- [ ] Basic frontend *+ tests?*
- [ ] `.idx` (index file) parser module *+ tests*
- [ ] Pretty frontend (possibly separate repo)

## Requirements

- 

### Installing dictionaries

- 

## Notes

- OpenOffice dictionary packs:
  - come in `.oxt` extension, which is just a zip
  - `.idx` - index containing byte offset for a word in a corresponding `.dat` file.
  Format: `word|offset`. First line is encoding, second is number of following *index* lines.
  - `.dat` - First line is encoding.

### Links

- https://extensions.openoffice.org/en/project/polish-dictionary-pack
- https://dobryslownik.pl
