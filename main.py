from parsers import ThesaurusParser


def main():
    dict_path = "./dict/pl-dict/th_pl_PL_v2.dat"

    parser = ThesaurusParser(dict_path)
    parser.parse()


if __name__ == "__main__":
    main()
