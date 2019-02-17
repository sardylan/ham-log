class AdifParser:
    @staticmethod
    def parse(raw_content=""):
        adif = {}

        mode = 0
        buff = ""

        tag = ""
        len = 0

        for c in raw_content:
            if c == 0:
                if c == "<":
                    m = 1
                    buff = ""
                    continue

            if c == 1:
                if c == ":":
                    m = 2
                    tag = buff
                    buff = ""
                    continue

            if c == 2:
                if c == ">":
                    m = 4
                    continue

            buff += c

        return adif


if __name__ == "__main__":
    fd = open("C:\\QARTest\\Logs\\cqwwcw2018.adi", "r")
    raw_content = fd.read()
    fd.close()

    adif = AdifParser.parse(raw_content)
    print(adif)
